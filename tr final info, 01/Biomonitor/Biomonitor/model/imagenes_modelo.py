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



class ImagenesModelo:
    def __init__(self, carpeta_pacientes="data_pacientes"):
        self.carpeta_pacientes = carpeta_pacientes
        os.makedirs(self.carpeta_pacientes, exist_ok=True)

        # Datos principales
        self.volumen = None        # np.ndarray 3D con la imagen (cortes, alto, ancho)
        self.metadatos = {}        # diccionario con info del estudio
        self.es_tomografia = False # True si es CT (para Hounsfield)

    # =========================================================
    #  CARGA DE IMÁGENES MÉDICAS
    # =========================================================
    def cargar_archivo(self, ruta_archivo):
        extension = os.path.splitext(ruta_archivo)[1].lower()

        if extension == ".dcm":
            return self._cargar_dicom(ruta_archivo)
        elif extension in [".nii", ".gz"]:
            return self._cargar_nifti(ruta_archivo)
        elif extension in [".jpg", ".jpeg", ".png"]:
            return self._cargar_imagen_simple(ruta_archivo)
        else:
            raise ValueError(f"Formato no soportado: {extension}")

    def _cargar_dicom(self, ruta_archivo):
        ds = pydicom.dcmread(ruta_archivo)
        imagen = ds.pixel_array.astype(np.float32)

        # Saber si es tomografía (CT)
        self.es_tomografia = getattr(ds, "Modality", "") == "CT"

        # Asegurar volumen 3D (n_cortes, alto, ancho)
        if imagen.ndim == 2:
            self.volumen = imagen[np.newaxis, :, :]   # (1, H, W)
        elif imagen.ndim == 3:
            self.volumen = imagen                     # (Z, H, W)
        else:
            raise ValueError("Dimensión de DICOM no soportada")

        # Guardar metadatos básicos en español
        self.metadatos = {
            "id_paciente": getattr(ds, "PatientID", "NA"),
            "nombre_paciente": str(getattr(ds, "PatientName", "NA")),
            "fecha_estudio": getattr(ds, "StudyDate", "NA"),
            "modalidad": getattr(ds, "Modality", "NA"),
            "descripcion_estudio": getattr(ds, "StudyDescription", "NA"),
            "descripcion_serie": getattr(ds, "SeriesDescription", "NA"),
            "pendiente_reescalado": float(getattr(ds, "RescaleSlope", 1.0)),
            "intercepto_reescalado": float(getattr(ds, "RescaleIntercept", 0.0)),
            "ruta_archivo": ruta_archivo,
            "fecha_carga": datetime.now().isoformat()
        }

        # Leer spacing de píxel y guardarlo
        self._extraer_espaciado_pixel(ds)

        # Si es CT, convertir a unidades Hounsfield
        if self.es_tomografia:
            self._convertir_a_hu()

        # Guardar metadatos en CSV
        self._guardar_metadatos_csv()

        return self.volumen, self.metadatos

    def _cargar_nifti(self, ruta_archivo):
        img_nifti = nib.load(ruta_archivo)
        datos = img_nifti.get_fdata().astype(np.float32)  # normalmente (X, Y, Z)

        # Reordenar a (Z, H, W) para tener consistencia
        self.volumen = np.transpose(datos, (2, 0, 1))
        self.es_tomografia = False

        self.metadatos = {
            "id_paciente": "Anon",
            "nombre_paciente": "Anon",
            "fecha_estudio": "NA",
            "modalidad": "NIFTI",
            "descripcion_estudio": "NA",
            "descripcion_serie": "NA",
            "pendiente_reescalado": 1.0,
            "intercepto_reescalado": 0.0,
            "ruta_archivo": ruta_archivo,
            "fecha_carga": datetime.now().isoformat()
        }

        self._guardar_metadatos_csv()
        return self.volumen, self.metadatos

    def _cargar_imagen_simple(self, ruta_archivo):
        imagen = cv2.imread(ruta_archivo, cv2.IMREAD_GRAYSCALE)
        if imagen is None:
            raise ValueError("No se pudo leer la imagen")

        # Tratarla como un volumen con un corte
        self.volumen = imagen[np.newaxis, :, :]

        self.metadatos = {
            "modalidad": "JPG/PNG",
            "ruta_archivo": ruta_archivo,
            "fecha_carga": datetime.now().isoformat()
        }
        self.es_tomografia = False

        self._guardar_metadatos_csv()
        return self.volumen, self.metadatos

    # =========================================================
    #  CONVERSIÓN A HOUNSFIELD (solo si es CT)
    # =========================================================
    def _convertir_a_hu(self):
        pendiente = self.metadatos.get("pendiente_reescalado", 1.0)
        intercepto = self.metadatos.get("intercepto_reescalado", 0.0)
        self.volumen = self.volumen * pendiente + intercepto

    # =========================================================
    #  METADATOS → CSV
    # =========================================================
    def _guardar_metadatos_csv(self):
        ruta_csv = os.path.join(self.carpeta_pacientes, "estudios_pacientes.csv")
        existe = os.path.isfile(ruta_csv)
        campos = list(self.metadatos.keys())

        with open(ruta_csv, mode="a", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=campos)
            if not existe:
                escritor.writeheader()
            escritor.writerow(self.metadatos)

    # =========================================================
    #  CORTES DEL VOLUMEN (AXIAL, CORONAL, SAGITAL)
    # =========================================================
    def obtener_corte_axial(self, indice):
        indice = np.clip(indice, 0, self.volumen.shape[0] - 1)
        return self.volumen[indice, :, :]

    def obtener_corte_coronal(self, indice):
        indice = np.clip(indice, 0, self.volumen.shape[1] - 1)
        return self.volumen[:, indice, :]

    def obtener_corte_sagital(self, indice):
        indice = np.clip(indice, 0, self.volumen.shape[2] - 1)
        return self.volumen[:, :, indice]

    def obtener_dimensiones(self):
        if self.volumen is None:
            return None
        # (n_cortes, alto, ancho)
        return self.volumen.shape

    # =========================================================
    #  ESPACIADO Y MEDICIONES
    # =========================================================
    def _extraer_espaciado_pixel(self, ds):
        """
        Lee PixelSpacing del DICOM y lo guarda en metadatos como (sx, sy).
        """
        espaciado = getattr(ds, "PixelSpacing", [1.0, 1.0])
        try:
            sx = float(espaciado[0])
            sy = float(espaciado[1])
        except Exception:
            sx, sy = 1.0, 1.0

        self.metadatos["espaciado_pixel_mm"] = [sx, sy]

    def distancia_en_mm(self, punto1, punto2):
        """
        Calcula distancia entre dos puntos (x1,y1), (x2,y2) en:
        - píxeles
        - milímetros (usando el espaciado de píxel)
        """
        if self.volumen is None:
            raise ValueError("No hay volumen cargado")

        dx = float(punto2[0] - punto1[0])
        dy = float(punto2[1] - punto1[1])
        distancia_pixeles = np.sqrt(dx**2 + dy**2)

        espaciado = self.metadatos.get("espaciado_pixel_mm", [1.0, 1.0])
        sx, sy = float(espaciado[0]), float(espaciado[1])
        distancia_mm = distancia_pixeles * (sx + sy) / 2.0  # promedio de ambos ejes

        return distancia_pixeles, distancia_mm

    def estadisticas_roi(self, corte_2d, mascara_binaria):
        """
        corte_2d: slice 2D del volumen
        mascara_binaria: 0 y 1 (o 0 y 255).
        Calcula estadísticos dentro de la región.
        """
        mascara = (mascara_binaria > 0)
        valores_roi = corte_2d[mascara]

        if valores_roi.size == 0:
            return None

        return {
            "intensidad_media": float(np.mean(valores_roi)),
            "desviacion_estandar": float(np.std(valores_roi)),
            "intensidad_minima": float(np.min(valores_roi)),
            "intensidad_maxima": float(np.max(valores_roi)),
            "numero_pixeles": int(valores_roi.size)
        }

    # =========================================================
    #  PROCESAMIENTO BÁSICO (FILTROS / SEGMENTACIÓN)
    # =========================================================
    def normalizar_0_1(self, imagen):
        imagen = imagen.astype(np.float32)
        minimo, maximo = imagen.min(), imagen.max()
        if maximo - minimo == 0:
            return np.zeros_like(imagen)
        return (imagen - minimo) / (maximo - minimo)

    def filtro_gaussiano(self, imagen, tam_kernel=5):
        return cv2.GaussianBlur(imagen, (tam_kernel, tam_kernel), 0)

    def segmentar_otsu(self, corte_2d):
        """
        Segmentación automática con Otsu sobre un corte 2D.
        """
        corte_norm = self.normalizar_0_1(corte_2d)
        corte_uint8 = np.uint8(corte_norm * 255)

        _, mascara = cv2.threshold(
            corte_uint8, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        return mascara

    def umbralizar(self, imagen, umbral=128):
        _, th = cv2.threshold(imagen, umbral, 255, cv2.THRESH_BINARY)
        return th

    def erosion(self, imagen, tam_kernel=3, iteraciones=1):
        kernel = np.ones((tam_kernel, tam_kernel), np.uint8)
        return cv2.erode(imagen, kernel, iterations=iteraciones)

    def dilatacion(self, imagen, tam_kernel=3, iteraciones=1):
        kernel = np.ones((tam_kernel, tam_kernel), np.uint8)
        return cv2.dilate(imagen, kernel, iterations=iteraciones)

    def apertura(self, imagen, tam_kernel=3):
        kernel = np.ones((tam_kernel, tam_kernel), np.uint8)
        return cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel)

    def cierre(self, imagen, tam_kernel=3):
        kernel = np.ones((tam_kernel, tam_kernel), np.uint8)
        return cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)

    def bordes_canny(self, imagen, t1=50, t2=150):
        return cv2.Canny(imagen, t1, t2)