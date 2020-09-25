from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
# from pymata4 import pymata4
from PyQt5.QtGui import QPixmap

class sliderControl(QWidget):

    TEXT_FONT = QtGui.QFont('Helvetica', 10)
    VALUE_FONT = QtGui.QFont('Helvetica', 11)
    DESC_FONT = QtGui.QFont('Helvetica', 8)

    SMOOTH_VALUE = {False: lambda l, v, step: l.setText(str(step*(v // step))),
              True: lambda l, v, step: l.setText(str(v))}

    SMOOTH_SLIDER = {False: lambda s, v, step: s.setValue(step*(v // step)),
              True: lambda s, v, step: None}

    # PWM_WRITE = {False: lambda b, pin, v, m: b.pwm_write(pin, v),
    #              True: lambda b, pin, v, m: b.pwm_write(pin, m - v)}

    def __init__(self, **kwargs):
        super().__init__()
        self.addSlider(**kwargs)

    def addSlider(self, pin=11, ptype='d', initial_value=0, range=(0,255,15), inverse=False, name='Sample slider', smooth=True, desc='Sample text'):

        # Link arduino pin and slider, define inversed or not
        self.pin = pin
        self.ptype = ptype
        self.inverse = inverse

        # Add slider name label
        self.name_label = QLabel(name, self)
        self.name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.name_label.setMinimumWidth(100)
        self.name_label.setFont(sliderControl.TEXT_FONT)

        # Add value displaying
        self.value_label = QLabel(str(initial_value), self)
        self.value_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.value_label.setMinimumWidth(80)
        self.value_label.setFont(sliderControl.VALUE_FONT)

        # Add slider
        self.slider = QSlider(Qt.Horizontal, self)
        self.range = (range[0], range[1])
        self.step = range[2]
        self.smooth = smooth

        self.slider.setRange(*self.range)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setPageStep(self.step)
        self.slider.setValue(initial_value)
        self.slider.setTickInterval(self.step if self.step > 15 else 15)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setSingleStep(self.step)
        self.slider.valueChanged.connect(self.changeValue)


        # Add slider container and append components
        self.container = QVBoxLayout()
        self.slider_box = QHBoxLayout()
        self.slider_box.addSpacing(15)
        self.slider_box.addWidget(self.name_label)
        self.slider_box.addSpacing(15)
        self.slider_box.addWidget(self.slider)
        self.slider_box.addSpacing(15)
        self.slider_box.addWidget(self.value_label)

        text_box = QHBoxLayout()
        test_text = QLabel(desc, self)
        test_text.setFont(sliderControl.DESC_FONT)
        test_text.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        test_text.setMaximumWidth(500)
        test_text.setWordWrap(True)
        text_box.addSpacing(15)
        text_box.addWidget(test_text)

        self.container.addLayout(self.slider_box)
        self.container.addLayout(text_box)

    def changeValue(self, value, board=None):

        # Smooth or not slider updating
        sliderControl.SMOOTH_SLIDER[self.smooth](self.slider, value, self.step)
        sliderControl.SMOOTH_VALUE[self.smooth](self.value_label, value, self.step)

        # This shit update pwm value for Arduino
        # sliderControl.PWM_WRITE[self.inverse](self.board, self.pin, value, self.range[1])