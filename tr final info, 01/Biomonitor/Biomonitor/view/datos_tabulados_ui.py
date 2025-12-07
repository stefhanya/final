# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datos_tabulados.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)


class Ui_datos_tabulados(object):
    def setupUi(self, datos_tabulados):
        if not datos_tabulados.objectName():
            datos_tabulados.setObjectName(u"datos_tabulados")
        datos_tabulados.resize(510, 898)
        datos_tabulados.setStyleSheet(u"background-color: rgb(249, 247, 245)")
        self.centralwidget = QWidget(datos_tabulados)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(160, 10, 221, 71))
        self.logo.setMinimumSize(QSize(221, 0))
        self.logo.setStyleSheet(u"border-image: url(:/logos/img proy inf/logo.png);")
        self.tabla_datos = QTableWidget(self.centralwidget)
        self.tabla_datos.setObjectName(u"tabla_datos")
        self.tabla_datos.setGeometry(QRect(30, 220, 441, 141))
        self.tabla_datos.setRowCount(0)
        self.tabla_datos.setColumnCount(0)
        self.boton_graficar = QPushButton(self.centralwidget)
        self.boton_graficar.setObjectName(u"boton_graficar")
        self.boton_graficar.setGeometry(QRect(40, 560, 431, 71))
        self.boton_graficar.setStyleSheet(u"font: 10pt \"Calibri\";\n"
"background-color: rgb(9, 139, 148)")
        self.atras = QPushButton(self.centralwidget)
        self.atras.setObjectName(u"atras")
        self.atras.setGeometry(QRect(360, 800, 121, 41))
        self.atras.setStyleSheet(u"font: 10pt \"Calibri\";background-color: rgb(9, 139, 148)")
        self.subtitulo = QLabel(self.centralwidget)
        self.subtitulo.setObjectName(u"subtitulo")
        self.subtitulo.setGeometry(QRect(20, 80, 441, 41))
        self.subtitulo.setStyleSheet(u"font: 75 20pt \"Calibri\";")
        self.boton_subir_CSV = QPushButton(self.centralwidget)
        self.boton_subir_CSV.setObjectName(u"boton_subir_CSV")
        self.boton_subir_CSV.setGeometry(QRect(40, 120, 431, 71))
        self.boton_subir_CSV.setStyleSheet(u"font: 10pt \"Calibri\";\n"
"\n"
"background-color: rgb(9, 139, 148)")
        self.lista_columnas = QListWidget(self.centralwidget)
        self.lista_columnas.setObjectName(u"lista_columnas")
        self.lista_columnas.setGeometry(QRect(40, 420, 431, 141))
        self.name_archivo = QLabel(self.centralwidget)
        self.name_archivo.setObjectName(u"name_archivo")
        self.name_archivo.setGeometry(QRect(20, 190, 321, 21))
        self.name_archivo.setStyleSheet(u"font:  15pt \"Calibri\";")
        self.subtitulo_2 = QLabel(self.centralwidget)
        self.subtitulo_2.setObjectName(u"subtitulo_2")
        self.subtitulo_2.setGeometry(QRect(20, 380, 391, 21))
        self.subtitulo_2.setStyleSheet(u"font:  15pt \"Calibri\";")
        self.grafica = QLabel(self.centralwidget)
        self.grafica.setObjectName(u"grafica")
        self.grafica.setGeometry(QRect(80, 640, 201, 201))
        self.grafica.setStyleSheet(u"border-image: url(:/imagenes/img proy inf/truncfinal01.png);")
        datos_tabulados.setCentralWidget(self.centralwidget)
        self.logo.raise_()
        self.tabla_datos.raise_()
        self.boton_graficar.raise_()
        self.atras.raise_()
        self.subtitulo.raise_()
        self.name_archivo.raise_()
        self.subtitulo_2.raise_()
        self.grafica.raise_()
        self.boton_subir_CSV.raise_()
        self.lista_columnas.raise_()
        self.menubar = QMenuBar(datos_tabulados)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 510, 26))
        datos_tabulados.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(datos_tabulados)
        self.statusbar.setObjectName(u"statusbar")
        datos_tabulados.setStatusBar(self.statusbar)

        self.retranslateUi(datos_tabulados)

        QMetaObject.connectSlotsByName(datos_tabulados)
    # setupUi

    def retranslateUi(self, datos_tabulados):
        datos_tabulados.setWindowTitle(QCoreApplication.translate("datos_tabulados", u"MainWindow", None))
        self.logo.setText("")
        self.boton_graficar.setText(QCoreApplication.translate("datos_tabulados", u"Graficar columna seleecionada", None))
        self.atras.setText(QCoreApplication.translate("datos_tabulados", u"Atras", None))
        self.subtitulo.setText(QCoreApplication.translate("datos_tabulados", u"<html><head/><body><p>Escoger CSV:</p></body></html>", None))
        self.boton_subir_CSV.setText(QCoreApplication.translate("datos_tabulados", u"Subir CSV", None))
        self.name_archivo.setText(QCoreApplication.translate("datos_tabulados", u"Archivo:", None))
        self.subtitulo_2.setText(QCoreApplication.translate("datos_tabulados", u"Selecione una columna para graficar:", None))
        self.grafica.setText("")
    # retranslateUi

