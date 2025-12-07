# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cargar_señal.ui'
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


class Ui_cargar_senal(object):
    def setupUi(self, cargar_senal):
        if not cargar_senal.objectName():
            cargar_senal.setObjectName(u"cargar_senal")
        cargar_senal.resize(500, 869)
        cargar_senal.setStyleSheet(u" background-color: rgb(249, 247, 245)")
        self.centralwidget = QWidget(cargar_senal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(150, 10, 221, 71))
        self.logo.setMinimumSize(QSize(221, 0))
        self.logo.setStyleSheet(u"border-image: url(:/logos/img proy inf/logo.png);")
        self.subtitulo = QLabel(self.centralwidget)
        self.subtitulo.setObjectName(u"subtitulo")
        self.subtitulo.setGeometry(QRect(40, 100, 391, 41))
        self.subtitulo.setStyleSheet(u"font: 75 20pt \"Calibri\";")
        self.boton_subir_seal = QPushButton(self.centralwidget)
        self.boton_subir_seal.setObjectName(u"boton_subir_seal")
        self.boton_subir_seal.setGeometry(QRect(40, 360, 431, 71))
        self.boton_subir_seal.setStyleSheet(u"font: 10pt \"Calibri\";\n"
"\n"
"background-color: rgb(9, 139, 148)")
        self.guardar = QPushButton(self.centralwidget)
        self.guardar.setObjectName(u"guardar")
        self.guardar.setGeometry(QRect(70, 740, 121, 41))
        self.guardar.setStyleSheet(u"font: 10pt \"Calibri\";background-color: rgb(159, 183, 190)")
        self.atras = QPushButton(self.centralwidget)
        self.atras.setObjectName(u"atras")
        self.atras.setGeometry(QRect(350, 740, 121, 41))
        self.atras.setStyleSheet(u"font: 10pt \"Calibri\";background-color: rgb(159, 183, 190)")
        self.ir_analisis = QPushButton(self.centralwidget)
        self.ir_analisis.setObjectName(u"ir_analisis")
        self.ir_analisis.setGeometry(QRect(210, 740, 121, 41))
        self.ir_analisis.setStyleSheet(u"font: 10pt \"Calibri\";background-color: rgb(159, 183, 190)")
        cargar_senal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(cargar_senal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 26))
        cargar_senal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(cargar_senal)
        self.statusbar.setObjectName(u"statusbar")
        cargar_senal.setStatusBar(self.statusbar)

        self.retranslateUi(cargar_senal)

        QMetaObject.connectSlotsByName(cargar_senal)
    # setupUi

    def retranslateUi(self, cargar_senal):
        cargar_senal.setWindowTitle(QCoreApplication.translate("cargar_senal", u"MainWindow", None))
        self.logo.setText("")
        self.subtitulo.setText(QCoreApplication.translate("cargar_senal", u"Cargar se\u00f1al biomedica:", None))
        self.boton_subir_seal.setText(QCoreApplication.translate("cargar_senal", u"Subir se\u00f1al", None))
        self.guardar.setText(QCoreApplication.translate("cargar_senal", u"Guardar", None))
        self.atras.setText(QCoreApplication.translate("cargar_senal", u"Atras", None))
        self.ir_analisis.setText(QCoreApplication.translate("cargar_senal", u"Ir a analisis", None))
    # retranslateUi

