"""
Coordinador/Controlador Principal para BioMonitor
Gestiona la comunicación entre las vistas y los modelos
Compatible con vista.py (PyQt5)
"""

import sys
import os
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QMessageBox

# Agregar path para importar modelos
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from model.paciente import Paciente
from model.imagenes_modelo import ImagenesModelo
from model.señales_modelo import SenalesModelo


class Coordinador:
    """
    Coordinador central que gestiona todas las operaciones
    entre las vistas y los modelos
    """
    
    def __init__(self):
        # Modelos
        self.modelo_imagenes = ImagenesModelo()
        self.modelo_senales = SenalesModelo()
        
        # Lista de pacientes
        self.pacientes = []
        
        # Datos CSV
        self.datos_csv = None
        
        # Usuario actual
        self.usuario_actual = None
        
        # Imágenes y señales cargadas
        self.imagen_actual = None
        self.senal_actual = None
    
    # ==================== GESTIÓN DE USUARIOS ====================
    
    def set_usuario(self, nombre_usuario):
        """Establece el usuario actual"""
        self.usuario_actual = nombre_usuario
    
    def get_usuario(self):
        """Obtiene el usuario actual"""
        return self.usuario_actual
    
    # ==================== GESTIÓN DE PACIENTES ====================
    
    def agregar_paciente(self, nombre, id_paciente, edad, bpm, spo2, temperatura):
        """
        Agrega un nuevo paciente al sistema
        
        Returns:
            tuple: (exito: bool, mensaje: str)
        """
        try:
            # Validar que el ID no exista
            if any(p.get_id() == id_paciente for p in self.pacientes):
                return False, "Ya existe un paciente con ese ID"
            
            # Crear paciente
            paciente = Paciente(nombre, id_paciente, edad, bpm, spo2, temperatura)
            self.pacientes.append(paciente)
            
            return True, f"Paciente {nombre} agregado exitosamente"
        
        except Exception as e:
            return False, f"Error al agregar paciente: {str(e)}"
    
    def actualizar_paciente(self, indice, nombre, edad, bpm, spo2, temperatura):
        """
        Actualiza los datos de un paciente
        
        Args:
            indice: Índice del paciente en la lista
        """
        try:
            if 0 <= indice < len(self.pacientes):
                paciente = self.pacientes[indice]
                paciente.set_nombre(nombre)
                paciente.set_edad(edad)
                paciente.set_bpm(bpm)
                paciente.set_spo2(spo2)
                paciente.set_temperatura(temperatura)
                return True, "Paciente actualizado exitosamente"
            else:
                return False, "Índice de paciente inválido"
        
        except Exception as e:
            return False, f"Error al actualizar: {str(e)}"
    
    def eliminar_paciente(self, indice):
        """Elimina un paciente del sistema"""
        try:
            if 0 <= indice < len(self.pacientes):
                paciente = self.pacientes.pop(indice)
                return True, f"Paciente {paciente.get_nombre()} eliminado"
            else:
                return False, "Índice inválido"
        
        except Exception as e:
            return False, f"Error al eliminar: {str(e)}"
    
    def obtener_pacientes(self):
        """Retorna la lista de pacientes"""
        return self.pacientes
    
    def obtener_paciente(self, indice):
        """Obtiene un paciente específico"""
        if 0 <= indice < len(self.pacientes):
            return self.pacientes[indice]
        return None
    
    def simular_signos_paciente(self, indice):
        """Genera signos vitales aleatorios para un paciente"""
        import random
        
        try:
            if 0 <= indice < len(self.pacientes):
                paciente = self.pacientes[indice]
                paciente.set_bpm(random.randint(50, 120))
                paciente.set_spo2(round(random.uniform(85, 100), 1))
                paciente.set_temperatura(round(random.uniform(35.5, 39.5), 1))
                return True, "Signos vitales simulados"
            else:
                return False, "Paciente no encontrado"
        
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    # ==================== GESTIÓN DE IMÁGENES ====================
    
    def cargar_imagen(self, ruta_archivo):
        """
        Carga una imagen médica (DICOM, NIFTI, PNG, JPG)
        
        Args:
            ruta_archivo: Ruta al archivo de imagen
        
        Returns:
            tuple: (exito: bool, mensaje: str)
        """
        try:
            volumen, metadatos = self.modelo_imagenes.cargar_archivo(ruta_archivo)
            self.imagen_actual = {
                'volumen': volumen,
                'metadatos': metadatos,
                'ruta': ruta_archivo
            }
            return True, "Imagen cargada exitosamente"
        
        except Exception as e:
            return False, f"Error al cargar imagen: {str(e)}"
    
    def procesar_imagen(self, tipo_procesamiento):
        """
        Aplica un procesamiento a la imagen cargada
        
        Args:
            tipo_procesamiento: "normalizar", "filtrar", "umbralizar", 
                               "binarizar", "transformacion", "bordes"
        
        Returns:
            imagen procesada o None
        """
        try:
            if self.imagen_actual is None:
                return None
            
            # Obtener un corte para procesar (primer corte axial)
            corte = self.modelo_imagenes.obtener_corte_axial(0)
            
            if tipo_procesamiento == "normalizar":
                return self.modelo_imagenes.normalizar_0_1(corte)
            
            elif tipo_procesamiento == "filtrar":
                return self.modelo_imagenes.filtro_gaussiano(corte)
            
            elif tipo_procesamiento == "umbralizar":
                corte_norm = self.modelo_imagenes.normalizar_0_1(corte)
                corte_uint8 = np.uint8(corte_norm * 255)
                return self.modelo_imagenes.umbralizar(corte_uint8)
            
            elif tipo_procesamiento == "binarizar":
                return self.modelo_imagenes.segmentar_otsu(corte)
            
            elif tipo_procesamiento == "transformacion":
                # Erosión + Dilatación
                corte_norm = self.modelo_imagenes.normalizar_0_1(corte)
                corte_uint8 = np.uint8(corte_norm * 255)
                erosionado = self.modelo_imagenes.erosion(corte_uint8)
                return self.modelo_imagenes.dilatacion(erosionado)
            
            elif tipo_procesamiento == "bordes":
                corte_norm = self.modelo_imagenes.normalizar_0_1(corte)
                corte_uint8 = np.uint8(corte_norm * 255)
                return self.modelo_imagenes.bordes_canny(corte_uint8)
            
            else:
                return None
        
        except Exception as e:
            print(f"Error en procesamiento: {e}")
            return None
    
    def obtener_cortes_imagen(self):
        """
        Obtiene los tres cortes principales de la imagen
        
        Returns:
            tuple: (sagital, coronal, axial) o None
        """
        try:
            if self.imagen_actual is None:
                return None
            
            dims = self.modelo_imagenes.obtener_dimensiones()
            if dims is None:
                return None
            
            # Cortes en el centro del volumen
            indice_z = dims[0] // 2
            indice_y = dims[1] // 2
            indice_x = dims[2] // 2
            
            sagital = self.modelo_imagenes.obtener_corte_sagital(indice_x)
            coronal = self.modelo_imagenes.obtener_corte_coronal(indice_y)
            axial = self.modelo_imagenes.obtener_corte_axial(indice_z)
            
            return sagital, coronal, axial
        
        except Exception as e:
            print(f"Error al obtener cortes: {e}")
            return None
    
    # ==================== GESTIÓN DE SEÑALES ====================
    
    def cargar_senal(self, ruta_archivo, frecuencia_muestreo=250):
        """
        Carga una señal desde archivo .mat
        
        Args:
            ruta_archivo: Ruta al archivo .mat
            frecuencia_muestreo: Frecuencia de muestreo en Hz
        
        Returns:
            tuple: (exito: bool, mensaje: str)
        """
        try:
            senales = self.modelo_senales.cargar_mat(
                ruta_archivo,
                nombre_variable="val",
                frecuencia_muestreo=frecuencia_muestreo
            )
            self.senal_actual = senales
            return True, "Señal cargada exitosamente"
        
        except Exception as e:
            return False, f"Error al cargar señal: {str(e)}"
    
    def aplicar_filtro_senal(self, freq_baja=0.5, freq_alta=50):
        """Aplica filtro pasa banda a la señal"""
        try:
            if self.senal_actual is None:
                return False, "No hay señal cargada"
            
            self.modelo_senales.filtrar_pasabanda(freq_baja, freq_alta)
            return True, "Filtro aplicado"
        
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def calcular_fft(self):
        """Calcula la FFT de la señal"""
        try:
            if self.senal_actual is None:
                return False, "No hay señal cargada"
            
            self.modelo_senales.calcular_fft()
            return True, "FFT calculada"
        
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def obtener_resultados_fft(self):
        """Obtiene los resultados de la FFT"""
        if self.modelo_senales.resultados_fft is not None:
            return self.modelo_senales.resultados_fft
        return None
    
    def generar_grafica_espectro(self, canal=0):
        """
        Genera datos para graficar el espectro de un canal
        
        Returns:
            tuple: (frecuencias, espectro) o None
        """
        try:
            if self.senal_actual is None:
                return None
            
            return self.modelo_senales.obtener_espectro_canal(canal)
        
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def generar_histograma_desviacion(self):
        """
        Genera datos para histograma de desviación estándar
        
        Returns:
            array de desviaciones o None
        """
        try:
            if self.senal_actual is None:
                return None
            
            return self.modelo_senales.calcular_desviacion_estandar(eje=0)
        
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    # ==================== GESTIÓN DE CSV ====================
    
    def cargar_csv(self, ruta_archivo):
        """
        Carga un archivo CSV
        
        Args:
            ruta_archivo: Ruta al archivo CSV
        
        Returns:
            tuple: (exito: bool, mensaje: str)
        """
        try:
            self.datos_csv = pd.read_csv(ruta_archivo)
            return True, "CSV cargado exitosamente"
        
        except Exception as e:
            return False, f"Error al cargar CSV: {str(e)}"
    
    def obtener_datos_csv(self):
        """Retorna los datos del CSV cargado"""
        return self.datos_csv
    
    def graficar_columna_csv(self, nombre_columna):
        """
        Obtiene los datos de una columna para graficar
        
        Args:
            nombre_columna: Nombre de la columna
        
        Returns:
            array con los datos o None
        """
        try:
            if self.datos_csv is None:
                return None
            
            if nombre_columna in self.datos_csv.columns:
                return self.datos_csv[nombre_columna].values
            else:
                return None
        
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    # ==================== EXPORTACIÓN ====================
    
    def exportar_reporte_paciente(self, indice):
        """
        Exporta un reporte del paciente a PDF
        
        Args:
            indice: Índice del paciente
        
        Returns:
            tuple: (exito: bool, mensaje: str, ruta_archivo: str)
        """
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas
            from reportlab.lib.units import inch
            from datetime import datetime
            
            if indice < 0 or indice >= len(self.pacientes):
                return False, "Paciente no encontrado", None
            
            paciente = self.pacientes[indice]
            
            # Crear carpeta de reportes
            os.makedirs("reportes", exist_ok=True)
            
            # Nombre del archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"reportes/reporte_{paciente.get_id()}_{timestamp}.pdf"
            
            # Crear PDF
            c = canvas.Canvas(filename, pagesize=letter)
            width, height = letter
            
            # Título
            c.setFont("Helvetica-Bold", 20)
            c.drawString(1*inch, height - 1*inch, "REPORTE BIOMÉDICO - BioMonitor")
            
            # Información
            c.setFont("Helvetica-Bold", 14)
            c.drawString(1*inch, height - 1.8*inch, "Información del Paciente")
            
            c.setFont("Helvetica", 12)
            y_pos = height - 2.2*inch
            
            datos = [
                f"Nombre: {paciente.get_nombre()}",
                f"ID: {paciente.get_id()}",
                f"Edad: {paciente.get_edad()} años",
                "",
                "Signos Vitales:",
                f"  • Frecuencia Cardíaca: {paciente.get_bpm()} BPM",
                f"  • Saturación de Oxígeno: {paciente.get_spo2()}%",
                f"  • Temperatura: {paciente.get_temperatura()}°C",
                "",
                f"Estado de Riesgo: {paciente.calcular_riesgo()}",
                "",
                f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            ]
            
            for linea in datos:
                c.drawString(1*inch, y_pos, linea)
                y_pos -= 0.3*inch
            
            c.save()
            
            return True, "Reporte generado exitosamente", filename
        
        except Exception as e:
            return False, f"Error al exportar: {str(e)}", None