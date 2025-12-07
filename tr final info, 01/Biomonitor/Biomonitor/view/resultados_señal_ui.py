# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resultados_señal.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)


class Ui_resultados_senal(object):
    def setupUi(self, resultados_senal):
        if not resultados_senal.objectName():
            resultados_senal.setObjectName(u"resultados_senal")
        resultados_senal.resize(507, 896)
        resultados_senal.setStyleSheet(u"background-color: rgb(249, 247, 245)")
        self.centralwidget = QWidget(resultados_senal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tablaFrecSEC = QTableWidget(self.centralwidget)
        if (self.tablaFrecSEC.columnCount() < 3):
            self.tablaFrecSEC.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaFrecSEC.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaFrecSEC.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaFrecSEC.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tablaFrecSEC.setObjectName(u"tablaFrecSEC")
        self.tablaFrecSEC.setGeometry(QRect(60, 150, 371, 181))
        self.tablaFrecSEC.setRowCount(0)
        self.tablaFrecSEC.setColumnCount(3)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(130, 10, 221, 71))
        self.logo.setMinimumSize(QSize(221, 0))
        self.logo.setStyleSheet(u"border-image: url(:/logos/img proy inf/logo.png);")
        self.subtitulo = QLabel(self.centralwidget)
        self.subtitulo.setObjectName(u"subtitulo")
        self.subtitulo.setGeometry(QRect(30, 100, 391, 31))
        self.subtitulo.setStyleSheet(u"font: 75 20pt \"Calibri\";")
        self.boton_espectro = QPushButton(self.centralwidget)
        self.boton_espectro.setObjectName(u"boton_espectro")
        self.boton_espectro.setGeometry(QRect(110, 390, 121, 41))
        self.boton_espectro.setStyleSheet(u"font: 10pt \"Calibri\"; background-color: rgb(9, 139, 148)")
        self.boton_desviacion = QPushButton(self.centralwidget)
        self.boton_desviacion.setObjectName(u"boton_desviacion")
        self.boton_desviacion.setGeometry(QRect(250, 390, 121, 41))
        self.boton_desviacion.setStyleSheet(u"font: 10pt \"Calibri\"; background-color: rgb(9, 139, 148)")
        self.Grafica_espectro = QLabel(self.centralwidget)
        self.Grafica_espectro.setObjectName(u"Grafica_espectro")
        self.Grafica_espectro.setGeometry(QRect(40, 460, 201, 201))
        self.Grafica_espectro.setStyleSheet(u"border-image: url(:/imagenes/img proy inf/truncfinal01.png);")
        self.desviacion = QLabel(self.centralwidget)
        self.desviacion.setObjectName(u"desviacion")
        self.desviacion.setGeometry(QRect(260, 460, 201, 201))
        self.desviacion.setStyleSheet(u"border-image: url(:/imagenes/img proy inf/truncfinal01.png);")
        self.atras = QPushButton(self.centralwidget)
        self.atras.setObjectName(u"atras")
        self.atras.setGeometry(QRect(360, 780, 121, 41))
        self.atras.setStyleSheet(u"font: 10pt \"Calibri\"; background-color: rgb(159, 183, 190)")
        self.texto_axial = QLabel(self.centralwidget)
        self.texto_axial.setObjectName(u"texto_axial")
        self.texto_axial.setGeometry(QRect(40, 670, 201, 41))
        self.texto_axial.setStyleSheet(u"\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.texto_axial_2 = QLabel(self.centralwidget)
        self.texto_axial_2.setObjectName(u"texto_axial_2")
        self.texto_axial_2.setGeometry(QRect(260, 670, 201, 41))
        self.texto_axial_2.setStyleSheet(u"\n"
"font: 11pt \"MS Shell Dlg 2\";")
        resultados_senal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(resultados_senal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 507, 26))
        resultados_senal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(resultados_senal)
        self.statusbar.setObjectName(u"statusbar")
        resultados_senal.setStatusBar(self.statusbar)

        self.retranslateUi(resultados_senal)

        QMetaObject.connectSlotsByName(resultados_senal)
    # setupUi

    def retranslateUi(self, resultados_senal):
        resultados_senal.setWindowTitle(QCoreApplication.translate("resultados_senal", u"MainWindow", None))
        ___qtablewidgetitem = self.tablaFrecSEC.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("resultados_senal", u"Canal", None));
        ___qtablewidgetitem1 = self.tablaFrecSEC.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("resultados_senal", u"Fracuencia (HZ)", None));
        ___qtablewidgetitem2 = self.tablaFrecSEC.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("resultados_senal", u"Magnitud", None));
        self.logo.setText("")
        self.subtitulo.setText(QCoreApplication.translate("resultados_senal", u"Resultados", None))
        self.boton_espectro.setText(QCoreApplication.translate("resultados_senal", u"Graficar espectro", None))
        self.boton_desviacion.setText(QCoreApplication.translate("resultados_senal", u"Desviaci\u00f3n ", None))
        self.Grafica_espectro.setText("")
        self.desviacion.setText("")
        self.atras.setText(QCoreApplication.translate("resultados_senal", u"Atras", None))
        self.texto_axial.setText(QCoreApplication.translate("resultados_senal", u"<html><head/><body><p align=\"center\">Grafica del espectro</p></body></html>", None))
        self.texto_axial_2.setText(QCoreApplication.translate("resultados_senal", u"<html><head/><body><p align=\"center\">Histograma Desviacion</p></body></html>", None))
    # retranslateUi

