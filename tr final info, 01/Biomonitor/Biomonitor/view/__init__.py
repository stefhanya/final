"""
Módulo de la Vista (View) en arquitectura MVC
Contiene todas las interfaces gráficas de usuario con PyQt5
"""

# Importar las clases principales de vista
from .vista import (
    VentanaPrincipal,
    VentanaSubirPNG,
    VentanaVerCortes,
    VentanaCargarSenal,
    VentanaResultadosSenal,
    VentanaDatosTabulados
)

__all__ = [
    'VentanaPrincipal',
    'VentanaSubirPNG',
    'VentanaVerCortes',
    'VentanaCargarSenal',
    'VentanaResultadosSenal',
    'VentanaDatosTabulados'
]