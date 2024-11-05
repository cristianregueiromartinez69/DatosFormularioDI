import random
import sys
import math
from cProfile import label

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit)
from setuptools.extern import names
from Botones import Botones

from Datos import DatosWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Formulario')
        self.setFixedSize(300, 400)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("aquaMarine"))
        self.setPalette(paleta)
        central_layout = QVBoxLayout()

        grid_datos = DatosWidget()
        boxBotones = Botones()
        central_layout.addLayout(grid_datos)
        central_layout.addLayout(boxBotones)

        container = QWidget()
        container.setLayout(central_layout)

        self.setCentralWidget(container)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fiestra = MainWindow()
    app.exec()
