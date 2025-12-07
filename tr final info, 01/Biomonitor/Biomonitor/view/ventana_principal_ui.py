# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import logo_pricipal_rc

class Ui_ventana_principal(object):
    def setupUi(self, ventana_principal):
        if not ventana_principal.objectName():
            ventana_principal.setObjectName(u"ventana_principal")
        ventana_principal.resize(511, 869)
        ventana_principal.setStyleSheet(u"font: 8pt \"Sitka\";  background-color: rgb(249, 247, 245)")
        self.centralwidget = QWidget(ventana_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.boton_cerrar = QPushButton(self.centralwidget)
        self.boton_cerrar.setObjectName(u"boton_cerrar")
        self.boton_cerrar.setGeometry(QRect(350, 750, 121, 41))
        self.boton_cerrar.setStyleSheet(u"font: 10pt \"Calibri\"; background-color: rgb(159, 183, 190)")
        self.boton_cargar_img = QPushButton(self.centralwidget)
        self.boton_cargar_img.setObjectName(u"boton_cargar_img")
        self.boton_cargar_img.setGeometry(QRect(40, 160, 431, 71))
        self.boton_cargar_img.setStyleSheet(u"font: 10pt \"Calibri\";\n"
"\n"
"\n"
"background-color: rgb(9, 139, 148)")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(140, 10, 221, 71))
        self.logo.setMinimumSize(QSize(221, 0))
        self.logo.setStyleSheet(u"border-image: url(:/logo.png);")
        self.saludo = QLabel(self.centralwidget)
        self.saludo.setObjectName(u"saludo")
        self.saludo.setGeometry(QRect(40, 100, 391, 31))
        self.saludo.setStyleSheet(u"font: 75 20pt \"Calibri\";")
        self.boton_procesar_img = QPushButton(self.centralwidget)
        self.boton_procesar_img.setObjectName(u"boton_procesar_img")
        self.boton_procesar_img.setGeometry(QRect(40, 250, 431, 71))
        self.boton_procesar_img.setStyleSheet(u"font: 10pt \"Calibri\";background-color: rgb(9, 139, 148)")
        self.boton_ver_daton = QPushButton(self.centralwidget)
        self.boton_ver_daton.setObjectName(u"boton_ver_daton")
        self.boton_ver_daton.setGeometry(QRect(40, 340, 431, 71))
        self.boton_ver_daton.setStyleSheet(u"font: 10pt \"Calibri\";background-color: rgb(9, 139, 148)")
        ventana_principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ventana_principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 511, 25))
        ventana_principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ventana_principal)
        self.statusbar.setObjectName(u"statusbar")
        ventana_principal.setStatusBar(self.statusbar)

        self.retranslateUi(ventana_principal)

        QMetaObject.connectSlotsByName(ventana_principal)
    # setupUi

    def retranslateUi(self, ventana_principal):
        ventana_principal.setWindowTitle(QCoreApplication.translate("ventana_principal", u"MainWindow", None))
        self.boton_cerrar.setText(QCoreApplication.translate("ventana_principal", u"Cerrar Session", None))
        self.boton_cargar_img.setText(QCoreApplication.translate("ventana_principal", u"\U0001f4f7 Cargar Imagenes", None))
        self.logo.setText("")
        self.saludo.setText(QCoreApplication.translate("ventana_principal", u"Hola...", None))
        self.boton_procesar_img.setText(QCoreApplication.translate("ventana_principal", u"\u2699\ufe0f Procesar Imagenes", None))
        self.boton_ver_daton.setText(QCoreApplication.translate("ventana_principal", u"\U0001f4ca Ver datos", None))
    # retranslateUi

