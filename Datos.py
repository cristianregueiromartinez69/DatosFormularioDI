import random
import sys
import math
from cProfile import label

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QGridLayout)
from setuptools.extern import names

class DatosWidget(QGridLayout):
    def __init__(self):
        super().__init__()
        self.labelNombre = QLabel("Nombre")
        self.nombreTexto = QLineEdit()

        self.labelApellidos = QLabel("Apellidos")
        self.apellidosTexto = QLineEdit()

        self.labelDni = QLabel("DNI")
        self.dniTexto = QLineEdit()

        self.labelEdad = QLabel("Edad")
        self.edadTexto = QLineEdit()

        self.addWidget(self.labelNombre, 0, 0, 1, 1)
        self.addWidget(self.nombreTexto, 0, 1, 1, 1)

        self.addWidget(self.labelApellidos, 1, 0, 1, 1)
        self.addWidget(self.apellidosTexto, 1, 1, 1, 1)

        self.addWidget(self.labelDni, 2, 0, 1, 1)
        self.addWidget(self.dniTexto, 2, 1, 1, 1)

        self.addWidget(self.labelEdad, 3, 0, 1, 1)
        self.addWidget(self.edadTexto, 3, 1, 1, 1)


