from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton)
from PyQt5.QtCore import Qt, QTimer
# from pymata4 import pymata4
from PyQt5.QtGui import QPixmap, QCursor, QFont

class sliderControl(QWidget):

    _TEXT_FONT = QFont("Roboto", 11, 500)
    _VALUE_FONT = QFont("Roboto", 12, 500)
    # _DESC_FONT = QFont('Helvetica [Cronyx]', 9)
    _DESC_FONT = QFont("Roboto", 10)

    __SMOOTH_VALUE = {False: lambda l, v, step: l.setText(str(step*(v // step))),
              True: lambda l, v, step: l.setText(str(v))}

    __SMOOTH_SLIDER = {False: lambda s, v, step: s.setValue(step*(v // step)),
              True: lambda s, v, step: None}

    # PWM_WRITE = {False: lambda b, pin, v, m: b.pwm_write(pin, v),
    #              True: lambda b, pin, v, m: b.pwm_write(pin, m - v)}

    def __init__(self, **kwargs):
        super().__init__()
        self.addSlider(**kwargs)
        self.__window = None

    def addSlider(self, pin=11, ptype='d', initial_value=0, range=(0,255,15), inverse=False,
                  name='Sample slider', smooth=True, desc='Sample text', last_item=False):
        # Link arduino pin and slider, define inversed or not
        self.__pin = pin
        self.__ptype = ptype
        self.__inverse = inverse

        # Add slider name label
        name_label = QPushButton(name, self)
        # name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        name_label.setMinimumWidth(120)
        name_label.setMaximumWidth(120)
        name_label.setFont(sliderControl._TEXT_FONT)
        name_label.setObjectName('nameLabel')
        name_label.setCursor(QCursor(Qt.PointingHandCursor))
        name_label.clicked.connect(self.__toggleVisible)
        # name_label.setStyleSheet('color: rgb(20, 20, 20); background-color: none; border: 0px none black; text-align: left;')

        # Add value displaying
        self._value_label = QLabel(str(initial_value), self)
        self._value_label.setAlignment(Qt.AlignCenter)
        self._value_label.setMinimumWidth(50)
        self._value_label.setFont(sliderControl._VALUE_FONT)
        self._value_label.setStyleSheet('color: rgb(30, 30, 30);')

        # Add slider
        self._slider = QSlider(Qt.Horizontal, self)
        self.__step = range[2]
        self.__smooth = smooth
        self._slider.setRange(range[0], range[1])
        self._slider.setFocusPolicy(Qt.NoFocus)
        self._slider.setPageStep(self.__step)
        self._slider.setValue(initial_value)
        self._slider.setTickInterval(self.__step if self.__step > 15 else 15)
        self._slider.setTickPosition(QSlider.TicksBothSides)
        self._slider.setSingleStep(self.__step)
        self._slider.valueChanged.connect(self.__changeValue)
        self._slider.setMaximumWidth(200)
        self._slider.setMinimumWidth(200)

        # Add +/- buttons with events
        plus_btn = QPushButton('+', self)
        plus_btn.setMaximumWidth(20)
        plus_btn.pressed.connect(self.__plusStart)
        plus_btn.released.connect(self.__plusStop)
        plus_btn.setCursor(QCursor(Qt.PointingHandCursor))

        minus_btn = QPushButton('-', self)
        minus_btn.setMaximumWidth(20)
        minus_btn.pressed.connect(self.__minusStart)
        minus_btn.released.connect(self.__minusStop)
        minus_btn.setCursor(QCursor(Qt.PointingHandCursor))

        # Add timers for +/- buttons
        self.__timers = [QTimer(), QTimer()]
        for timer in self.__timers:
            timer.setInterval(50)

        self.__timers[0].timeout.connect(lambda: self._slider.setValue(self._slider.value() - self.__step))
        self.__timers[1].timeout.connect(lambda: self._slider.setValue(self._slider.value() + self.__step))

        self.__delays = [QTimer(), QTimer()]
        for timer in self.__delays:
            timer.setSingleShot(True)
            timer.setInterval(600)

        self.__delays[0].timeout.connect(lambda: self.__timers[0].start())
        self.__delays[1].timeout.connect(lambda: self.__timers[1].start())

        # Add slider container and append components
        slider_box = QHBoxLayout()
        slider_box.addWidget(name_label)
        slider_box.addSpacing(15)
        slider_box.addWidget(self._slider)
        slider_box.addSpacing(15)
        slider_box.addWidget(minus_btn)
        slider_box.addWidget(self._value_label)
        slider_box.addWidget(plus_btn)

        self._description = QLabel(desc, self)
        self._description.setFont(sliderControl._DESC_FONT)
        self._description.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self._description.setMaximumWidth(500)
        self._description.setWordWrap(True)
        if last_item:
            self._description.setStyleSheet(
                                  'color: rgb(50, 50, 50); '
                                  'padding-top: 15px;'
                                  'padding-bottom: 10px;'
                                  )
        else:
            self._description.setStyleSheet(
                'color: rgb(50, 50, 50); '
                'border-top: 0px solid qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgb(230, 230, 230),'
                'stop:0.1 rgb(212, 212, 212), stop:0.9 rgb(212, 212, 212), stop:1 rgb(230, 230, 230));'
                'border-bottom: 1px solid qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgb(238, 238, 238),'
                'stop:0.2 rgb(212, 212, 212), stop:0.8 rgb(212, 212, 212), stop:1 rgb(238, 238, 238));'
                'padding-top: 15px;'
                'padding-bottom: 15px;'
            )

        self._description.setVisible(False)

        desc_box = QHBoxLayout()
        desc_box.addWidget(self._description)

        self.container = QVBoxLayout()
        self.container.addSpacing(15)
        self.container.addLayout(slider_box)
        self.container.addLayout(desc_box)
        # self.container.setAlignment(Qt.AlignTop)

    def __changeValue(self, value, board=None):

        # Smooth or not slider updating
        sliderControl.__SMOOTH_SLIDER[self.__smooth](self._slider, value, self.__step)
        sliderControl.__SMOOTH_VALUE[self.__smooth](self._value_label, value, self.__step)

        # This shit update pwm value for Arduino
        # sliderControl.PWM_WRITE[self.__inverse](self.board, self.pin, value, self.range[1])

    def __plusStart(self):
        self._slider.setValue(self._slider.value() + self.__step)
        self.__delays[1].start()

    def __minusStart(self):
        self._slider.setValue(self._slider.value() - self.__step)
        self.__delays[0].start()

    def __plusStop(self):
        self.__delays[1].stop()
        self.__timers[1].stop()

    def __minusStop(self):
        self.__delays[0].stop()
        self.__timers[0].stop()

    def __toggleVisible(self):
        if self._description.isVisible():
            self._description.setVisible(False)
        else:
            self._description.setVisible(True)
