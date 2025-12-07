# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_subir_PNG.ui'
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


class Ui_ventana_subir_PNG(object):
    def setupUi(self, ventana_subir_PNG):
        if not ventana_subir_PNG.objectName():
            ventana_subir_PNG.setObjectName(u"ventana_subir_PNG")
        ventana_subir_PNG.resize(509, 869)
        ventana_subir_PNG.setStyleSheet(u" background-color: rgb(249, 247, 245)")
        self.centralwidget = QWidget(ventana_subir_PNG)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(120, 10, 221, 71))
        self.logo.setMinimumSize(QSize(221, 0))
        self.logo.setStyleSheet(u"border-image: url(:/logos/img proy inf/logo.png);")
        self.subtitulo = QLabel(self.centralwidget)
        self.subtitulo.setObjectName(u"subtitulo")
        self.subtitulo.setGeometry(QRect(40, 90, 391, 41))
        self.subtitulo.setStyleSheet(u"font: 75 20pt \"Calibri\";")
        self.boton_subir_img = QPushButton(self.centralwidget)
        self.boton_subir_img.setObjectName(u"boton_subir_img")
        self.boton_subir_img.setGeometry(QRect(40, 360, 431, 71))
        self.boton_subir_img.setStyleSheet(u"\n"
"font: 10pt \"Calibri\";  background-color: rgb(9, 139, 148)")
        self.guardar = QPushButton(self.centralwidget)
        self.guardar.setObjectName(u"guardar")
        self.guardar.setGeometry(QRect(340, 750, 121, 41))
        self.guardar.setStyleSheet(u"font: 10pt \"Calibri\"; background-color: rgb(159, 183, 190)")
        self.atras = QPushButton(self.centralwidget)
        self.atras.setObjectName(u"atras")
        self.atras.setGeometry(QRect(190, 750, 121, 41))
        self.atras.setStyleSheet(u"font: 10pt \"Calibri\"; background-color: rgb(159, 183, 190)")
        ventana_subir_PNG.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ventana_subir_PNG)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 509, 26))
        ventana_subir_PNG.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ventana_subir_PNG)
        self.statusbar.setObjectName(u"statusbar")
        ventana_subir_PNG.setStatusBar(self.statusbar)

        self.retranslateUi(ventana_subir_PNG)

        QMetaObject.connectSlotsByName(ventana_subir_PNG)
    # setupUi

    def retranslateUi(self, ventana_subir_PNG):
        ventana_subir_PNG.setWindowTitle(QCoreApplication.translate("ventana_subir_PNG", u"MainWindow", None))
        self.logo.setText("")
        self.subtitulo.setText(QCoreApplication.translate("ventana_subir_PNG", u"Cargar imagen para visualizar:", None))
        self.boton_subir_img.setText(QCoreApplication.translate("ventana_subir_PNG", u"Subir imagen", None))
        self.guardar.setText(QCoreApplication.translate("ventana_subir_PNG", u"Guardar", None))
        self.atras.setText(QCoreApplication.translate("ventana_subir_PNG", u"Atras", None))
    # retranslateUi

