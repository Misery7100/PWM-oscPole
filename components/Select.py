from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox)
from PyQt5.QtCore import Qt
# from pymata4 import pymata4

class Select(QWidget):

    def __init__(self, **kwargs):
        super().__init__()
        self.addSelect(**kwargs)

    def addSelect(self, name='Sample select', items=('Sample item')):

        self._select = QComboBox(self)
        self._select.addItems(items)

        self.container = QHBoxLayout()
        self.container.addWidget(self._select)