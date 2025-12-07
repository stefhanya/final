# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from form_ui import Ui_Login
import xml.etree.ElementTree as ET




# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py



class Login(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.enter.clicked.connect(self.verificarLogin)

    def verificarLogin(self):
        usuario = self.ui.user.text()
        contraseña = self.ui.password.text()

        try:
            tree = ET.parse("credenciales.xml")
            root = tree.getroot()

            valido = False

            for user in root.findall("users/user"):
                username = user.find("username").text
                password = user.find("password").text

                if usuario == username and contraseña == password:
                    valido = True
                    break

            if valido:
                self.ui.msj.setStyleSheet("color: green;")
                self.ui.msj.setText("¡¡¡BIENVENIDO AL SISTEMA!!!") #TOCA PORNERLE NOMBRE**

                self.ventana_camara = VentanaCamara()
                self.ventana_camara.show()
                self.close()


                
            else:
                self.ui.msj.setStyleSheet("color: red;")
                self.ui.msj.setText("Usuario o contraseña incorrectos")

        except Exception as e:
            self.ui.msj.setStyleSheet("color: red;")
            self.ui.msj.setText("Error al leer credenciales")





if __name__ == "__main__":
    app = QApplication(sys.argv)

    from camara import VentanaCamara

    widget = Login()
    widget.show()
    sys.exit(app.exec())
