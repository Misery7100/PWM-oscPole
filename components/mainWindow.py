from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
# from pymata4 import pymata4
from PyQt5.QtGui import QPixmap, QFont
from style.global_layout import *

class mainWindow(QWidget):


    def __init__(self, **kwargs):
        super().__init__()
        self.initWindow(**kwargs)

    def initWindow(self, components=None, title='Sample title'):

        self._layout = QVBoxLayout()

        if not components is None:
            for component in components:
                self._layout.addLayout(component.container)

        copyright = QLabel('© Saint Petersburg State University, 2020',self)
        copyright.setFont(COPYRIGHT_FONT)
        copyright.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        copyright.setFixedHeight(COPYRIGHT_HEIGHT)
        copyright.setStyleSheet('color: rgb(130, 130, 130);')

        copyright_ly = QHBoxLayout()
        copyright_ly.addWidget(copyright)
        copyright_ly.setContentsMargins(0,5,0,0)

        self._layout.addLayout(copyright_ly)
        self.setLayout(self._layout)
        self.setGeometry(*WIN_POS, *WIN_SIZE)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle(title)