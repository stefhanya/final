# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ver_cortez.ui'
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


class Ui_ver_cortez(object):
    def setupUi(self, ver_cortez):
        if not ver_cortez.objectName():
            ver_cortez.setObjectName(u"ver_cortez")
        ver_cortez.resize(510, 869)
        ver_cortez.setMouseTracking(False)
        ver_cortez.setStyleSheet(u" background-color: rgb(249, 247, 245)")
        self.centralwidget = QWidget(ver_cortez)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(130, 10, 221, 71))
        self.logo.setMinimumSize(QSize(221, 0))
        self.logo.setStyleSheet(u"border-image: url(:/logos/img proy inf/logo.png);")
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(30, 90, 391, 41))
        self.titulo.setStyleSheet(u"font: 75 20pt \"Calibri\";")
        self.corte_sagital = QLabel(self.centralwidget)
        self.corte_sagital.setObjectName(u"corte_sagital")
        self.corte_sagital.setGeometry(QRect(30, 130, 201, 201))
        self.corte_sagital.setStyleSheet(u"border-image: url(:/imagenes/img proy inf/truncfinal01.png);")
        self.corte_coronal = QLabel(self.centralwidget)
        self.corte_coronal.setObjectName(u"corte_coronal")
        self.corte_coronal.setGeometry(QRect(280, 130, 201, 201))
        self.corte_coronal.setStyleSheet(u"border-image: url(:/imagenes/img proy inf/truncfinal01.png);")
        self.corte_axial = QLabel(self.centralwidget)
        self.corte_axial.setObjectName(u"corte_axial")
        self.corte_axial.setGeometry(QRect(30, 370, 201, 201))
        self.corte_axial.setStyleSheet(u"border-image: url(:/imagenes/img proy inf/truncfinal01.png);")
        self.normalizar = QPushButton(self.centralwidget)
        self.normalizar.setObjectName(u"normalizar")
        self.normalizar.setGeometry(QRect(50, 630, 121, 41))
        self.normalizar.setStyleSheet(u"font: 10pt \"Calibri\"; background-color: rgb(9, 139, 148)")
        self.filtrar = QPushButton(self.centralwidget)
        self.filtrar.setObjectName(u"filtrar")
        self.filtrar.setGeometry(QRect(200, 630, 121, 41))
        self.filtrar.setStyleSheet(u"font: 10pt \"Calibri\";  background-color: rgb(9, 139, 148)")
        self.umbralizacin = QPushButton(self.centralwidget)
        self.umbralizacin.setObjectName(u"umbralizacin")
        self.umbralizacin.setGeometry(QRect(50, 680, 121, 41))
        self.umbralizacin.setStyleSheet(u"font: 10pt \"Calibri\"; background-color: rgb(9, 139, 148)")
        self.atras = QPushButton(self.centralwidget)
        self.atras.setObjectName(u"atras")
        self.atras.setGeometry(QRect(370, 750, 121, 41))
        self.atras.setStyleSheet(u"font: 10pt \"Calibri\"; background-color: rgb(159, 183, 190)")
        self.texto_sagital = QLabel(self.centralwidget)
        self.texto_sagital.setObjectName(u"texto_sagital")
        self.texto_sagital.setGeometry(QRect(30, 330, 201, 41))
        self.texto_sagital.setStyleSheet(u"\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.texto_coronal = QLabel(self.centralwidget)
        self.texto_coronal.setObjectName(u"texto_coronal")
        self.texto_coronal.setGeometry(QRect(280, 330, 201, 41))
        self.texto_coronal.setStyleSheet(u"\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.texto_axial = QLabel(self.centralwidget)
        self.texto_axial.setObjectName(u"texto_axial")
        self.texto_axial.setGeometry(QRect(30, 570, 201, 41))
        self.texto_axial.setStyleSheet(u"\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.binarizacion = QPushButton(self.centralwidget)
        self.binarizacion.setObjectName(u"binarizacion")
        self.binarizacion.setGeometry(QRect(350, 630, 121, 41))
        self.binarizacion.setStyleSheet(u"font: 10pt \"Calibri\"; background-color: rgb(9, 139, 148)")
        self.transformacion = QPushButton(self.centralwidget)
        self.transformacion.setObjectName(u"transformacion")
        self.transformacion.setGeometry(QRect(200, 680, 121, 41))
        self.transformacion.setStyleSheet(u"font: 10pt \"Calibri\";  background-color: rgb(9, 139, 148)")
        self.bordes = QPushButton(self.centralwidget)
        self.bordes.setObjectName(u"bordes")
        self.bordes.setGeometry(QRect(350, 680, 121, 41))
        self.bordes.setStyleSheet(u"font: 10pt \"Calibri\";  background-color: rgb(9, 139, 148)")
        self.img_procesada = QLabel(self.centralwidget)
        self.img_procesada.setObjectName(u"img_procesada")
        self.img_procesada.setGeometry(QRect(280, 370, 201, 201))
        self.img_procesada.setStyleSheet(u"border-image: url(:/imagenes/img proy inf/truncfinal01.png);")
        self.texto_img_procesada = QLabel(self.centralwidget)
        self.texto_img_procesada.setObjectName(u"texto_img_procesada")
        self.texto_img_procesada.setGeometry(QRect(280, 570, 201, 41))
        self.texto_img_procesada.setStyleSheet(u"\n"
"font: 11pt \"MS Shell Dlg 2\";")
        ver_cortez.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ver_cortez)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 510, 26))
        ver_cortez.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ver_cortez)
        self.statusbar.setObjectName(u"statusbar")
        ver_cortez.setStatusBar(self.statusbar)

        self.retranslateUi(ver_cortez)

        QMetaObject.connectSlotsByName(ver_cortez)
    # setupUi

    def retranslateUi(self, ver_cortez):
        ver_cortez.setWindowTitle(QCoreApplication.translate("ver_cortez", u"MainWindow", None))
        self.logo.setText("")
        self.titulo.setText(QCoreApplication.translate("ver_cortez", u"Cortes de imagenes:", None))
        self.corte_sagital.setText("")
        self.corte_coronal.setText("")
        self.corte_axial.setText("")
        self.normalizar.setText(QCoreApplication.translate("ver_cortez", u"Normalizar", None))
        self.filtrar.setText(QCoreApplication.translate("ver_cortez", u"Filtrar", None))
        self.umbralizacin.setText(QCoreApplication.translate("ver_cortez", u"Umbralizaci\u00f3n", None))
        self.atras.setText(QCoreApplication.translate("ver_cortez", u"Atras", None))
        self.texto_sagital.setText(QCoreApplication.translate("ver_cortez", u"<html><head/><body><p align=\"center\">Corte sagital</p></body></html>", None))
        self.texto_coronal.setText(QCoreApplication.translate("ver_cortez", u"<html><head/><body><p align=\"center\">Corte coronal</p></body></html>", None))
        self.texto_axial.setText(QCoreApplication.translate("ver_cortez", u"<html><head/><body><p align=\"center\">Corte axial</p></body></html>", None))
        self.binarizacion.setText(QCoreApplication.translate("ver_cortez", u"Binarizaci\u00f3n", None))
        self.transformacion.setText(QCoreApplication.translate("ver_cortez", u"Tranformaci\u00f3n", None))
        self.bordes.setText(QCoreApplication.translate("ver_cortez", u"Bordes", None))
        self.img_procesada.setText("")
        self.texto_img_procesada.setText(QCoreApplication.translate("ver_cortez", u"<html><head/><body><p align=\"center\">Imagen procesada</p></body></html>", None))
    # retranslateUi

