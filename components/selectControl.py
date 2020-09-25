from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
# from pymata4 import pymata4
from PyQt5.QtGui import QPixmap

class selectControl(QWidget):

    def __init__(self, **kwargs):
        super().__init__()
        self.addSlider(**kwargs)

    def addSelect(self, name='Sample select', items=('Sample item')):
        pass