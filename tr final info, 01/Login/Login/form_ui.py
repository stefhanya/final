# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(342, 296)
        Login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.user = QLineEdit(Login)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(110, 60, 151, 31))
        self.user.setStyleSheet(u"color: rgb(118, 118, 118);")
        self.password = QLineEdit(Login)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(110, 110, 151, 31))
        self.password.setStyleSheet(u"color: rgb(118, 118, 118);")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.enter = QPushButton(Login)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(80, 160, 181, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.enter.setFont(font)
        self.enter.setStyleSheet(u"color: rgb(0,0, 0);\n"
"background-color: rgb(118, 208, 98);")
        self.icuser = QLabel(Login)
        self.icuser.setObjectName(u"icuser")
        self.icuser.setGeometry(QRect(80, 60, 31, 31))
        self.icuser.setStyleSheet(u"background-color: rgb(118, 209, 98);")
        self.icuser.setPixmap(QPixmap(u"iconos/user_456283.png"))
        self.icuser.setScaledContents(True)
        self.icpass = QLabel(Login)
        self.icpass.setObjectName(u"icpass")
        self.icpass.setGeometry(QRect(80, 110, 31, 31))
        self.icpass.setStyleSheet(u"background-color: rgb(118, 209, 98);")
        self.icpass.setPixmap(QPixmap(u"iconos/padlock_1153364.png"))
        self.icpass.setScaledContents(True)
        self.fondito = QLabel(Login)
        self.fondito.setObjectName(u"fondito")
        self.fondito.setGeometry(QRect(50, 30, 241, 191))
        self.fondito.setAutoFillBackground(False)
        self.fondito.setStyleSheet(u"background-color: rgb(179, 179, 179);")
        self.msj = QLabel(Login)
        self.msj.setObjectName(u"msj")
        self.msj.setGeometry(QRect(50, 240, 241, 31))
        self.fondito.raise_()
        self.password.raise_()
        self.enter.raise_()
        self.icpass.raise_()
        self.user.raise_()
        self.icuser.raise_()
        self.msj.raise_()

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.user.setText("")
        self.user.setPlaceholderText(QCoreApplication.translate("Login", u"Usuario", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
        self.enter.setText(QCoreApplication.translate("Login", u"Ingresar", None))
        self.icuser.setText("")
        self.icpass.setText("")
        self.fondito.setText("")
        self.msj.setText("")
    # retranslateUi

