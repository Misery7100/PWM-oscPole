from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
# from pymata4 import pymata4
from PyQt5.QtGui import QPixmap, QFont

class mainWindow(QWidget):


    def __init__(self, **kwargs):
        super().__init__()
        self.initWindow(**kwargs)

    def initWindow(self, components=None, title='Sample title'):

        self._layout = QVBoxLayout()

        if not components is None:
            for component in components:
                self._layout.addLayout(component.container)

        cr = QLabel('© Saint Petersburg State University, 2020',self)
        cr.setFont(QFont('Roboto', 8))
        cr.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        cr.setFixedHeight(20)
        cr.setStyleSheet('color: rgb(130, 130, 130);')
        cr_ly = QHBoxLayout()
        cr_ly.addWidget(cr)
        cr_ly.setContentsMargins(0,5,0,0)
        self._layout.addLayout(cr_ly)
        self.setLayout(self._layout)
        self.setGeometry(600, 200, 550, 250)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle(title)