from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QComboBox,
                             QPushButton)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
# from pymata4 import pymata4
from PyQt5.QtGui import QPixmap

class Select(QWidget):

    def __init__(self, **kwargs):
        super().__init__()
        self.addSelect(**kwargs)

    def addSelect(self, name='Sample select', items=('Sample item')):

        self._select = QComboBox(self)
        self._select.addItems(items)

        self.container = QHBoxLayout()
        self.container.addWidget(self._select)