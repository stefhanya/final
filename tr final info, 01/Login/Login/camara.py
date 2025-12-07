# This Python file uses the following encoding: utf-8


import cv2
import os
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage, QPixmap
from camara_ui import Ui_camara
import mysql.connector
from datetime import datetime


class VentanaCamara(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_camara()
        self.ui.setupUi(self)
        self.foto_contador = 0

        
        self.ui.flash.clicked.connect(self.capturar_imagen)


    def capturar_imagen(self):
        cam = cv2.VideoCapture(0)

        if not cam.isOpened():
            self.ui.photo.setText("No se pudo acceder a la cámara")
            return

        ret, frame = cam.read()
        cam.release()

        if not ret:
            self.ui.photo.setText("Error al capturar imagen")
            return

        
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ruta = f"usuarios/usuario.png"

        cv2.imwrite(ruta, gris)

        self.registrar_en_bd("admin", ruta)


        h, w = gris.shape
        bytes_per_line = w
        imagen_qt = QImage(gris.data, w, h, bytes_per_line, QImage.Format_Grayscale8)

        self.ui.photo.setPixmap(QPixmap.fromImage(imagen_qt))

    def registrar_en_bd(self, usuario, ruta):

        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin12345",   
                database="sistema_login"
            )

            cursor = conexion.cursor()

            query = """
            INSERT INTO actividad_usuarios (usuario, fecha_hora, accion, ruta_imagen)
            VALUES (%s, %s, %s, %s)
            """

            datos = (usuario, datetime.now(), "Captura biométrica", ruta)

            cursor.execute(query, datos)
            conexion.commit()
            cursor.close()
            conexion.close()

        except Exception as e:
            print("Error al registrar:", e)

        

