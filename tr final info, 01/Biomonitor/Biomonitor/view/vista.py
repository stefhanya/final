import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from . import logo_principal_rc
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_agg import FigureCanvasAgg


def ruta_ui(nombre_archivo):
    return os.path.join(os.path.dirname(__file__), nombre_archivo)

class VentanaPrincipal(QMainWindow):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi(ruta_ui("ventana_principal.ui"), self)
        self.setup()
    
    def setup(self):
        self.boton_cargar_img.clicked.connect(self.abrir_ventana_subir_png)
        self.boton_procesar_img.clicked.connect(self.abrir_ventana_cargar_senal)
        self.boton_ver_daton.clicked.connect(self.abrir_ventana_datos_tabulados)
        self.boton_cerrar.clicked.connect(self.cerrar_sesion)
    
    def abrir_ventana_subir_png(self):
        ventana_subir = VentanaSubirPNG(self)
        self.hide()
        ventana_subir.show()
    
    def abrir_ventana_cargar_senal(self):
        ventana_senal = VentanaCargarSenal(self)
        self.hide()
        ventana_senal.show()
    
    def abrir_ventana_datos_tabulados(self):
        ventana_datos = VentanaDatosTabulados(self)
        self.hide()
        ventana_datos.show()
    
    def cerrar_sesion(self):
        self.close()
    
    def setControlador(self, c):
        self._miCoordinador = c
    
    def actualizar_saludo(self, nombre_usuario):
        self.saludo.setText(f"Hola {nombre_usuario}...")

class VentanaSubirPNG(QMainWindow):
    def __init__(self, ppal=None):
        super(VentanaSubirPNG, self).__init__(ppal)
        loadUi(ruta_ui("ventana_subir_PNG.ui"), self)
        self.__ventanaPadre = ppal
        self.ruta_imagen = None
        self.setup()
    
    def setup(self):
        self.boton_subir_img.clicked.connect(self.subir_imagen)
        self.guardar.clicked.connect(self.guardar_imagen)
        self.atras.clicked.connect(self.volver_atras)
    
    def subir_imagen(self):
        archivo, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar Imagen", "", 
            "Archivos de Imagen (*.png *.jpg *.jpeg *.dcm *.nii *.nii.gz)"
        )
        if archivo:
            self.ruta_imagen = archivo
            QMessageBox.information(self, "Éxito", "Imagen cargada correctamente")
    
    def guardar_imagen(self):
        if self.ruta_imagen:
            self.__ventanaPadre._miCoordinador.cargar_imagen(self.ruta_imagen)

            ventana_cortes = VentanaVerCortes(self.__ventanaPadre)

            sagital, coronal, axial = self.__ventanaPadre._miCoordinador.obtener_cortes_imagen()

            ventana_cortes.mostrar_cortes(sagital, coronal, axial)

            self.close()
            ventana_cortes.show()
        else:
            QMessageBox.warning(self, "Advertencia", "Debe cargar una imagen primero")

    def volver_atras(self):
        self.__ventanaPadre.show()
        self.close()

class VentanaVerCortes(QMainWindow):
    def __init__(self, ppal=None):
        super(VentanaVerCortes, self).__init__(ppal)
        loadUi(ruta_ui("ver_cortez.ui"), self)
        self.__ventanaPadre = ppal
        self.setup()

    
    def setup(self):
        self.normalizar.clicked.connect(self.aplicar_normalizacion)
        self.filtrar.clicked.connect(self.aplicar_filtro)
        self.umbralizacin.clicked.connect(self.aplicar_umbralizacion)
        self.binarizacion.clicked.connect(self.aplicar_binarizacion)
        self.transformacion.clicked.connect(self.aplicar_transformacion)
        self.bordes.clicked.connect(self.aplicar_bordes)
        self.atras.clicked.connect(self.volver_atras)
    
    def aplicar_normalizacion(self):
        img = self.__ventanaPadre._miCoordinador.procesar_imagen("normalizar")
        self.actualizar_vista_procesada(img)

    def aplicar_filtro(self):
        img = self.__ventanaPadre._miCoordinador.procesar_imagen("filtrar")
        self.actualizar_vista_procesada(img)

    def aplicar_umbralizacion(self):
        img = self.__ventanaPadre._miCoordinador.procesar_imagen("umbralizar")
        self.actualizar_vista_procesada(img)

    def aplicar_binarizacion(self):
        img = self.__ventanaPadre._miCoordinador.procesar_imagen("binarizar")
        self.actualizar_vista_procesada(img)

    def aplicar_transformacion(self):
        img = self.__ventanaPadre._miCoordinador.procesar_imagen("transformacion")
        self.actualizar_vista_procesada(img)

    def aplicar_bordes(self):
        img = self.__ventanaPadre._miCoordinador.procesar_imagen("bordes")
        self.actualizar_vista_procesada(img)
    
    def actualizar_vista_procesada(self, imagen):
        if imagen is not None:
            self.mostrar_imagen_en_label(self.img_procesada, imagen)


    def mostrar_cortes(self, corte_sagital, corte_coronal, corte_axial):
            if corte_sagital is not None:
                self.mostrar_imagen_en_label(self.corte_sagital, corte_sagital)
        
            if corte_coronal is not None:
                self.mostrar_imagen_en_label(self.corte_coronal, corte_coronal)
        
            if corte_axial is not None:
                self.mostrar_imagen_en_label(self.corte_axial, corte_axial)

    def mostrar_imagen_en_label(self, label, imagen_array):
        """
        Método auxiliar para mostrar un array de numpy como imagen en un QLabel
        imagen_array: numpy array 2D (escala de grises)
        label: QLabel donde se mostrará la imagen
        """
        imagen_normalizada = ((imagen_array - imagen_array.min()) / 
                            (imagen_array.max() - imagen_array.min()) * 255).astype(np.uint8)
        
        altura, ancho = imagen_normalizada.shape
        
        bytes_por_linea = ancho
        q_imagen = QImage(imagen_normalizada.data, ancho, altura, 
                        bytes_por_linea, QImage.Format_Grayscale8)
        
        pixmap = QPixmap.fromImage(q_imagen)
        
        pixmap_escalado = pixmap.scaled(label.size(), Qt.KeepAspectRatio, 
                                        Qt.SmoothTransformation)
        label.setPixmap(pixmap_escalado)

    def volver_atras(self):
        self.close()
        self.__ventanaPadre.show()

class VentanaCargarSenal(QMainWindow):
        def __init__(self, ppal=None):
            super(VentanaCargarSenal, self).__init__(ppal)
            loadUi(ruta_ui("cargar_señal.ui"), self)
            self.__ventanaPadre = ppal
            self.ruta_senal = None
            self.setup()
        
        def setup(self):
            self.boton_subir_seal.clicked.connect(self.subir_senal)
            self.guardar.clicked.connect(self.guardar_senal)
            self.ir_analisis.clicked.connect(self.ir_a_analisis)
            self.atras.clicked.connect(self.volver_atras)
        
        def subir_senal(self):
            archivo, _ = QFileDialog.getOpenFileName(
                self, "Seleccionar Señal", "", 
                "Archivos MAT (*.mat)"
            )
            if archivo:
                self.ruta_senal = archivo
                QMessageBox.information(self, "Éxito", "Señal cargada correctamente")

        def guardar_senal(self):
            if self.ruta_senal:
                exito, mensaje = self.__ventanaPadre._miCoordinador.cargar_senal(self.ruta_senal, frecuencia_muestreo=250)
                if exito:
                    self.__ventanaPadre._miCoordinador.calcular_fft()
                    QMessageBox.information(self, "Éxito", "Señal guardada y FFT calculada correctamente")
                else:
                    QMessageBox.warning(self, "Error", mensaje)
            else:
                QMessageBox.warning(self, "Advertencia", "Debe cargar una señal primero")


        def ir_a_analisis(self):
            if self.ruta_senal:
                ventana_resultados = VentanaResultadosSenal(self.__ventanaPadre)
                self.close()
                ventana_resultados.show()
            else:
                QMessageBox.warning(self, "Advertencia", "Debe cargar y guardar una señal primero")
        
        def volver_atras(self):
            self.__ventanaPadre.show()
            self.close()

class VentanaResultadosSenal(QMainWindow):
    def __init__(self, ppal=None):
        super(VentanaResultadosSenal, self).__init__(ppal)
        loadUi(ruta_ui("resultados_señal.ui"), self)
        self.__ventanaPadre = ppal
        self.setup()
    
    def setup(self):
        self.boton_espectro.clicked.connect(self.graficar_espectro)
        self.boton_desviacion.clicked.connect(self.graficar_desviacion)
        self.atras.clicked.connect(self.volver_atras)
        self.cargar_tabla_frecuencias()
    
    def cargar_tabla_frecuencias(self):
        datos_fft = self.__ventanaPadre._miCoordinador.obtener_resultados_fft()
        if datos_fft is not None:
            self.tablaFrecSEC.setRowCount(len(datos_fft))
            for i, fila in datos_fft.iterrows():
                self.tablaFrecSEC.setItem(i, 0, QTableWidgetItem(str(fila['canal'])))
                self.tablaFrecSEC.setItem(i, 1, QTableWidgetItem(str(fila['frecuencia_dominante_Hz'])))
                self.tablaFrecSEC.setItem(i, 2, QTableWidgetItem(str(fila['magnitud'])))
    
    def graficar_espectro(self):
        resultado = self.__ventanaPadre._miCoordinador.generar_grafica_espectro()
        if resultado is None:
            return
        frecuencias, espectro = resultado

        fig, ax = plt.subplots(figsize=(2,2), dpi=100)
        ax.plot(frecuencias, espectro)
        ax.set_title("Espectro de la señal")
        ax.set_xlabel("Frecuencia (Hz)")
        ax.set_ylabel("Magnitud")
        fig.tight_layout()

        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        width, height = fig.get_size_inches() * fig.get_dpi()
        image = QPixmap.fromImage(
            QImage(canvas.buffer_rgba(), int(width), int(height), QImage.Format_RGBA8888)
        )
        self.Grafica_espectro.setPixmap(image)


    
    def graficar_desviacion(self):
        desvio = self.__ventanaPadre._miCoordinador.generar_histograma_desviacion()
        if desvio is None or len(desvio) == 0:
            return

        fig, ax = plt.subplots(figsize=(2,2), dpi=100)
        ax.hist(desvio, bins=20)
        ax.set_title("Histograma de desviación")
        ax.set_xlabel("Valor")
        ax.set_ylabel("Frecuencia")
        fig.tight_layout()

        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        width, height = fig.get_size_inches() * fig.get_dpi()
        image = QPixmap.fromImage(
            QImage(canvas.buffer_rgba(), int(width), int(height), QImage.Format_RGBA8888)
        )
        self.desviacion.setPixmap(image)


    def volver_atras(self):
        self.__ventanaPadre.show()
        self.close()

class VentanaDatosTabulados(QMainWindow):
    def __init__(self, ppal=None):
        super(VentanaDatosTabulados, self).__init__(ppal)
        loadUi(ruta_ui("datos_tabulados.ui"), self)
        self.__ventanaPadre = ppal
        self.ruta_csv = None
        self.setup()
    
    def setup(self):
        self.boton_subir_CSV.clicked.connect(self.subir_csv)
        self.boton_graficar.clicked.connect(self.graficar_columna)
        self.atras.clicked.connect(self.volver_atras)
    
    def subir_csv(self):
        archivo, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar CSV", "", 
            "Archivos CSV (*.csv)"
        )
        if archivo:
            self.ruta_csv = archivo
            self.name_archivo.setText(f"Archivo: {archivo.split('/')[-1]}")
            self.__ventanaPadre._miCoordinador.cargar_csv(archivo)
            self.cargar_datos_tabla()
            self.cargar_lista_columnas()
    
    def cargar_datos_tabla(self):
        datos = self.__ventanaPadre._miCoordinador.obtener_datos_csv()
        if datos is None:
            return

        filas, columnas = datos.shape

        self.tabla_datos.setRowCount(filas)
        self.tabla_datos.setColumnCount(columnas)
        self.tabla_datos.setHorizontalHeaderLabels(datos.columns)

        for i in range(filas):
            for j in range(columnas):
                valor = QTableWidgetItem(str(datos.iloc[i, j]))
                self.tabla_datos.setItem(i, j, valor)
    
    def cargar_lista_columnas(self):
        datos = self.__ventanaPadre._miCoordinador.obtener_datos_csv()
        if datos is not None:
            self.lista_columnas.clear()
            self.lista_columnas.addItems(datos.columns.tolist())

    def graficar_columna(self):
        item_seleccionado = self.lista_columnas.currentItem()
        if item_seleccionado:
            columna = item_seleccionado.text()
            datos = self.__ventanaPadre._miCoordinador.graficar_columna_csv(columna)
            if datos is not None:
                fig = Figure(figsize=(3,3))
                canvas = FigureCanvas(fig)
                ax = fig.add_subplot(111)
                ax.plot(datos)
                ax.set_title(columna)
                ax.grid(True)

                if self.grafica.layout() is None:
                    self.grafica.setLayout(QVBoxLayout())

                layout = self.grafica.layout()
                for i in reversed(range(layout.count())):
                    widget_to_remove = layout.itemAt(i).widget()
                    layout.removeWidget(widget_to_remove)
                    widget_to_remove.setParent(None)

                self.grafica.layout().addWidget(canvas)
                canvas.draw()
            else:
                QMessageBox.warning(self, "Error", "No se pudieron obtener los datos de la columna")
        else:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una columna")

    def volver_atras(self):
        self.__ventanaPadre.show()
        self.close()
