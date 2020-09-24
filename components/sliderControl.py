from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
# from pymata4 import pymata4
from PyQt5.QtGui import QPixmap

class sliderControl(QWidget):

    FONT = QtGui.QFont('Comic Sans MS', 12)

    SMOOTH_VALUE = {False: lambda l, v, step: l.setText(str(step*(v // step))),
              True: lambda l, v, step: l.setText(str(v))}

    SMOOTH_SLIDER = {False: lambda s, v, step: s.setValue(step*(v // step)),
              True: lambda s, v, step: None}

    # PWM_WRITE = {False: lambda b, pin, v, m: b.pwm_write(pin, v),
    #              True: lambda b, pin, v, m: b.pwm_write(pin, m - v)}

    def __init__(self, **kwargs):
        super().__init__()
        self.addSlider(**kwargs)

    def addSlider(self, pin=11, ptype='d', initial_value=0, range=(0,255,1), inverse=False, name='Sample slider', smooth=True):

        # Link arduino pin and slider, define inversed or not
        self.pin = pin
        self.ptype = ptype
        self.inverse = inverse

        # Add slider name label
        self.name_label = QLabel(name, self)
        self.name_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.name_label.setMinimumWidth(100)
        self.name_label.setFont(sliderControl.FONT)

        # Add value displaying
        self.value_label = QLabel(str(initial_value), self)
        self.value_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.value_label.setMinimumWidth(80)
        self.value_label.setFont(sliderControl.FONT)

        # Add slider
        self.slider = QSlider(Qt.Horizontal, self)
        self.range = (range[0], range[1])
        self.step = range[2]
        self.smooth = smooth

        self.slider.setRange(*self.range)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setPageStep(self.step)
        self.slider.setValue(initial_value)
        self.slider.setTickInterval(self.step if self.step > 16 else 16)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setSingleStep(self.step)
        self.slider.valueChanged.connect(self.changeValue)


        # Add slider container and append components
        self.container = QHBoxLayout()
        self.container.addWidget(self.name_label)
        self.container.addSpacing(15)
        self.container.addWidget(self.slider)
        self.container.addSpacing(15)
        self.container.addWidget(self.value_label)

    def changeValue(self, value, board=None):

        # Smooth or not slider updating
        sliderControl.SMOOTH_SLIDER[self.smooth](self.slider, value, self.step)
        sliderControl.SMOOTH_VALUE[self.smooth](self.value_label, value, self.step)

        # This shit update pwm value for Arduino
        # sliderControl.PWM_WRITE[self.inverse](self.board, self.pin, value, self.range[1])