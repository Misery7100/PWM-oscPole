from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
# from pymata4 import pymata4
from PyQt5.QtGui import QPixmap, QFont
from style.global_layout import *

class Window(QWidget):

    COPYRIGHT = {True: lambda w: Copyright(w),
                 False: lambda w: None}

    def __init__(self, **kwargs):
        super().__init__()
        self.initWindow(**kwargs)

    def initWindow(self, components=None, title='Sample title', pos=(WIN_POS[0], WIN_POS[1]),
                   size=(WIN_SIZE[0], WIN_SIZE[1]), cright=False):

        self._layout = QVBoxLayout()

        if not components is None:
            if not isinstance(components, (tuple, list)): self._layout.addLayout(components.container)
            else:
                for component in components:
                    self._layout.addLayout(component.container)

        Window.COPYRIGHT[cright](self)

        self.setLayout(self._layout)
        self.setGeometry(*pos, *size)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle(title)

class Copyright(QLabel):

    CR = '© Saint Petersburg State University, 2020'

    def __init__(self, widget):
        super().__init__(Copyright.CR, widget)
        self.addCR(widget)

    def addCR(self, widget):

        self.setFont(COPYRIGHT_FONT)
        self.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.setFixedHeight(COPYRIGHT_HEIGHT)
        self.setStyleSheet('color: rgb(130, 130, 130);')
        copyright_ly = QHBoxLayout()
        copyright_ly.addWidget(self)
        copyright_ly.setContentsMargins(0, 5, 0, 0)
        widget._layout.addLayout(copyright_ly)