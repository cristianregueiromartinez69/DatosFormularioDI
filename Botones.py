import random
import sys
import math
from cProfile import label

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout)
from setuptools.extern import names

class Botones(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.button_editar = QPushButton("Editar")
        self.button_aceptar = QPushButton("Aceptar")
        self.button_cancelar = QPushButton("Cancelar")

        self.addWidget(self.button_editar)
        self.addWidget(self.button_aceptar)
        self.addWidget(self.button_cancelar)