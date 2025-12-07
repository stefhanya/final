import os
import csv
import numpy as np
import cv2
import pydicom
import nibabel as nib
from datetime import datetime
import pandas as pd
from scipy.io import loadmat
from numpy.fft import rfft, rfftfreq
from scipy.signal import butter, filtfilt, find_peaks

class SenalesModelo:
    """
    Clase para manejar:
    - Carga de señales desde .mat
    - Filtrado pasa banda
    - FFT y frecuencia dominante
    - Análisis de picos (frecuencia estimada en el tiempo)
    - Cálculo de desviación estándar
    """

    def __init__(self, carpeta_resultados="resultados_senales"):
        self.carpeta_resultados = carpeta_resultados
        os.makedirs(self.carpeta_resultados, exist_ok=True)

        self.senales = None          # np.ndarray (n_muestras, n_canales)
        self.frecuencia_muestreo = None  # fs
        self.resultados_fft = None   # DataFrame con frecuencia dominante por canal

    # =========================================================
    #  CARGA DE SEÑAL DESDE .MAT
    # =========================================================
    def cargar_mat(self, ruta_archivo, nombre_variable="data",
                   frecuencia_muestreo=250, canales_en_filas=True):
        """
        ruta_archivo: path del archivo .mat
        nombre_variable: clave dentro del .mat que contiene la señal
        frecuencia_muestreo: Hz
        canales_en_filas:
            True  -> array en el .mat tiene forma (n_canales, n_muestras)
            False -> array en el .mat tiene forma (n_muestras, n_canales)
        """
        datos_mat = loadmat(ruta_archivo)

        if nombre_variable not in datos_mat:
            raise KeyError(f"La variable '{nombre_variable}' no está en el archivo .mat")

        datos = datos_mat[nombre_variable]

        # Asegurar forma (n_muestras, n_canales)
        if canales_en_filas:
            datos = datos.T   # de (n_canales, n_muestras) a (n_muestras, n_canales)

        self.senales = datos.astype(np.float32)
        self.frecuencia_muestreo = float(frecuencia_muestreo)

        return self.senales

    # =========================================================
    #  FILTRADO PASA BANDA (BUTTERWORTH)
    # =========================================================
    def filtrar_pasabanda(self, frecuencia_baja_hz, frecuencia_alta_hz, orden=4):
        """
        Aplica un filtro Butterworth pasa banda a TODAS las señales (cada canal).
        Modifica self.senales y retorna la señal filtrada.

        frecuencia_baja_hz: frecuencia de corte inferior (Hz)
        frecuencia_alta_hz: frecuencia de corte superior (Hz)
        orden: orden del filtro
        """
        if self.senales is None or self.frecuencia_muestreo is None:
            raise ValueError("No hay señal cargada o no se ha definido la frecuencia de muestreo.")

        frecuencia_nyquist = 0.5 * self.frecuencia_muestreo
        baja_norm = frecuencia_baja_hz / frecuencia_nyquist
        alta_norm = frecuencia_alta_hz / frecuencia_nyquist

        if baja_norm <= 0 or alta_norm >= 1 or baja_norm >= alta_norm:
            raise ValueError("Frecuencias de corte inválidas para el filtro pasa banda.")

        b, a = butter(orden, [baja_norm, alta_norm], btype="band")
        # Filtrar a lo largo del eje del tiempo (axis=0)
        self.senales = filtfilt(b, a, self.senales, axis=0)

        return self.senales

    # =========================================================
    #  FFT Y FRECUENCIA DOMINANTE
    # =========================================================
    def calcular_fft(self):
        """
        Calcula la FFT de cada canal y obtiene la frecuencia dominante
        (la de mayor magnitud, ignorando la componente DC).

        Retorna:
            DataFrame con columnas: canal, frecuencia_dominante_Hz, magnitud
        y guarda un CSV en carpeta_resultados.
        """
        if self.senales is None or self.frecuencia_muestreo is None:
            raise ValueError("No hay señal cargada o no se ha definido la frecuencia de muestreo.")

        n_muestras, n_canales = self.senales.shape
        frecuencias = rfftfreq(n_muestras, d=1.0 / self.frecuencia_muestreo)

        resultados = []

        for indice_canal in range(n_canales):
            senal_canal = self.senales[:, indice_canal]
            espectro = np.abs(rfft(senal_canal))

            # Ignorar componente 0 (DC) para la frecuencia dominante
            indice_max = np.argmax(espectro[1:]) + 1
            frecuencia_dom = frecuencias[indice_max]
            magnitud_dom = espectro[indice_max]

            resultados.append({
                "canal": indice_canal,
                "frecuencia_dominante_Hz": float(frecuencia_dom),
                "magnitud": float(magnitud_dom)
            })

        self.resultados_fft = pd.DataFrame(resultados)

        ruta_csv = os.path.join(self.carpeta_resultados, "frecuencias_dominantes.csv")
        self.resultados_fft.to_csv(ruta_csv, index=False)

        return self.resultados_fft

    # =========================================================
    #  ESPECTRO COMPLETO DE UN CANAL (PARA GRAFICAR)
    # =========================================================
    def obtener_espectro_canal(self, indice_canal):
        """
        Devuelve (frecuencias, espectro) de un canal específico,
        para que luego la VISTA lo grafique.
        """
        if self.senales is None or self.frecuencia_muestreo is None:
            raise ValueError("No hay señal cargada o no se ha definido la frecuencia de muestreo.")

        n_muestras, n_canales = self.senales.shape
        if indice_canal < 0 or indice_canal >= n_canales:
            raise IndexError("Índice de canal fuera de rango.")

        senal_canal = self.senales[:, indice_canal]
        frecuencias = rfftfreq(n_muestras, d=1.0 / self.frecuencia_muestreo)
        espectro = np.abs(rfft(senal_canal))

        return frecuencias, espectro

    # =========================================================
    #  ANÁLISIS DE PICOS EN UN CANAL
    # =========================================================
    def analizar_picos_canal(self, indice_canal, altura_minima=None,
                             distancia_minima_muestras=None):
        """
        Detecta picos en un canal y estima la frecuencia de aparición de los picos.

        indice_canal: canal a analizar
        altura_minima: valor mínimo de amplitud para considerar un pico (None = automáticamente)
        distancia_minima_muestras: separación mínima entre picos en número de muestras

        Retorna un diccionario con:
            - n_picos
            - frecuencia_estimada_Hz (a partir del tiempo entre picos)
            - amplitud_media_picos
        """
        if self.senales is None or self.frecuencia_muestreo is None:
            raise ValueError("No hay señal cargada o no se ha definido la frecuencia de muestreo.")

        n_muestras, n_canales = self.senales.shape
        if indice_canal < 0 or indice_canal >= n_canales:
            raise IndexError("Índice de canal fuera de rango.")

        senal = self.senales[:, indice_canal]

        indices_picos, propiedades = find_peaks(
            senal,
            height=altura_minima,
            distance=distancia_minima_muestras
        )

        # Si hay menos de 2 picos, no se puede estimar bien la frecuencia temporal
        if indices_picos.size < 2:
            amplitud_media = float(propiedades["peak_heights"].mean()) if "peak_heights" in propiedades and len(propiedades["peak_heights"]) > 0 else 0.0
            return {
                "n_picos": int(indices_picos.size),
                "frecuencia_estimada_Hz": 0.0,
                "amplitud_media_picos": amplitud_media
            }

        tiempos_picos = indices_picos / float(self.frecuencia_muestreo)
        intervalos = np.diff(tiempos_picos)
        frecuencia_estimada = 1.0 / np.mean(intervalos)

        amplitud_media = float(propiedades["peak_heights"].mean() if "peak_heights" in propiedades else 0.0)

        return {
            "n_picos": int(indices_picos.size),
            "frecuencia_estimada_Hz": float(frecuencia_estimada),
            "amplitud_media_picos": amplitud_media
        }

    # =========================================================
    #  DESVIACIÓN ESTÁNDAR (PARA HISTOGRAMA)
    # =========================================================
    def calcular_desviacion_estandar(self, eje=0):
        """
        Calcula la desviación estándar de la señal.

        eje = 0 → desviación a lo largo del tiempo, por canal
                  (devuelve un valor por canal)
        eje = 1 → desviación a lo largo de canales, por instante de tiempo
                  (devuelve un valor por muestra)

        Retorna: array de desviaciones estándar.
        """
        if self.senales is None:
            raise ValueError("No hay señal cargada.")

        valores_desviacion = np.std(self.senales, axis=eje)
        return valores_desviacion