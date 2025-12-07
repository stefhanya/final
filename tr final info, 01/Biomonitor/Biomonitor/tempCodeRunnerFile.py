"""
BioMonitor - Sistema de Gestión de Pacientes
Aplicación principal con arquitectura MVC

Punto de entrada del programa
"""

import sys
from PyQt5.QtWidgets import QApplication

# Importar vista y controlador
from view import VentanaPrincipal
from controller.coordinador import Coordinador
from model.paciente import Paciente


def main():
    """Función principal que inicia la aplicación"""
    
    # Crear aplicación Qt
    app = QApplication(sys.argv)
    
    # Crear coordinador/controlador
    coordinador = Coordinador()
    
    # Establecer usuario (puede venir de un login previo)
    coordinador.set_usuario("admin")
    
    # Crear ventana principal
    ventana_principal = VentanaPrincipal()
    
    # Conectar el coordinador con la ventana
    ventana_principal.setControlador(coordinador)
    
    # Actualizar saludo con el nombre del usuario
    ventana_principal.actualizar_saludo(coordinador.get_usuario())
    
    # Mostrar ventana
    ventana_principal.show()
    
    # Ejecutar aplicación
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()