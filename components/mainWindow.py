from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
# from pymata4 import pymata4
from PyQt5.QtGui import QPixmap

class mainWindow(QWidget):


    def __init__(self, **kwargs):
        super().__init__()
        self.initWindow(**kwargs)

    def initWindow(self, components=None, title='Sample title'):

        mainWindow = QVBoxLayout()

        if not components is None:
            for component in components:
                mainWindow.addLayout(component.container)

        self.setLayout(mainWindow)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle(title)