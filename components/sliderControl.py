from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton)
from PyQt5.QtCore import Qt, QTimer
# from pymata4 import pymata4
from PyQt5.QtGui import QCursor, QFont
from style.global_layout import *

class sliderControl(QWidget):

    __SMOOTH_VALUE = {False: lambda l, v, step: l.setText(str(step*(v // step))),
              True: lambda l, v, step: l.setText(str(v))}

    __SMOOTH_SLIDER = {False: lambda s, v, step: s.setValue(step*(v // step)),
              True: lambda s, v, step: None}

    # __INVERSE_PWM = {False: lambda b, pin, v, m: b.pwm_write(pin, v),
    #              True: lambda b, pin, v, m: b.pwm_write(pin, m - v)}

    def __init__(self, **kwargs):
        super().__init__()
        self.addSlider(**kwargs)
        self.__window = None

    def addSlider(self, pin=11, ptype='d', initial_value=SLIDER_RANGE[0], range=(*SLIDER_RANGE, SLIDER_TICK_MIN),
                  inverse=False, name='Sample slider', smooth=True, desc='Sample text', last_item=False):

        # Link arduino pin and slider, define inversed or not
        self.__pin = pin
        self.__ptype = ptype
        self.__inverse = inverse

        # Add slider name label
        name_label = QPushButton(name, self)
        name_label.setMinimumWidth(SLIDER_LABEL_WIDTH)
        name_label.setMaximumWidth(SLIDER_LABEL_WIDTH)
        name_label.setFont(TEXT_FONT)
        name_label.setObjectName('sliderLabel')
        name_label.setCursor(QCursor(Qt.PointingHandCursor))
        name_label.clicked.connect(self.__toggleVisible)

        # Add value displaying
        self._value_label = QLabel(str(initial_value), self)
        self._value_label.setAlignment(Qt.AlignCenter)
        self._value_label.setMinimumWidth(SLIDER_VALUE_WIDTH)
        self._value_label.setFont(VALUE_FONT)
        self._value_label.setObjectName('sliderValue')

        # Add slider
        self._slider = QSlider(Qt.Horizontal, self)
        self.__step = range[2]
        self._slider.setRange(range[0], range[1])
        self._slider.setFocusPolicy(Qt.NoFocus)
        self._slider.setPageStep(self.__step)
        self._slider.setValue(initial_value)
        self._slider.setTickInterval(self.__step if self.__step > SLIDER_TICK_MIN else SLIDER_TICK_MIN)
        self._slider.setTickPosition(QSlider.TicksBothSides)
        self._slider.setSingleStep(self.__step)
        self._slider.valueChanged.connect(self.__changeValue)
        self._slider.setMaximumWidth(SLIDER_WIDTH)
        self._slider.setMinimumWidth(SLIDER_WIDTH)
        self.__smooth = smooth

        # Add +/- buttons with events
        plus_btn = QPushButton('+', self)
        plus_btn.setMaximumWidth(INC_BUTTON_WIDTH)
        plus_btn.pressed.connect(self.__plusStart)
        plus_btn.released.connect(self.__plusStop)
        plus_btn.setCursor(QCursor(Qt.PointingHandCursor))

        minus_btn = QPushButton('-', self)
        minus_btn.setMaximumWidth(INC_BUTTON_WIDTH)
        minus_btn.pressed.connect(self.__minusStart)
        minus_btn.released.connect(self.__minusStop)
        minus_btn.setCursor(QCursor(Qt.PointingHandCursor))

        # Add timers for +/- buttons
        self.__timers = [QTimer(), QTimer()]
        for timer in self.__timers:
            timer.setInterval(ITERATE_INTERVAL)

        self.__timers[0].timeout.connect(lambda: self._slider.setValue(self._slider.value() - self.__step))
        self.__timers[1].timeout.connect(lambda: self._slider.setValue(self._slider.value() + self.__step))

        self.__delays = [QTimer(), QTimer()]
        for timer in self.__delays:
            timer.setSingleShot(True)
            timer.setInterval(DELAY_INTERVAL)

        self.__delays[0].timeout.connect(lambda: self.__timers[0].start())
        self.__delays[1].timeout.connect(lambda: self.__timers[1].start())

        # Add slider container and append components
        slider_box = QHBoxLayout()
        slider_box.addWidget(name_label)
        slider_box.addSpacing(H_SPACING)
        slider_box.addWidget(self._slider)
        slider_box.addSpacing(H_SPACING)
        slider_box.addWidget(minus_btn)
        slider_box.addWidget(self._value_label)
        slider_box.addWidget(plus_btn)

        self._description = QLabel(desc, self)
        self._description.setFont(DESCRIPRION_FONT)
        self._description.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self._description.setMaximumWidth(GLOBAL_WIDTH)
        self._description.setWordWrap(True)

        if last_item: self._description.setObjectName('descriptionLast')
        else: self._description.setObjectName('description')

        self._description.setVisible(False)

        desc_box = QHBoxLayout()
        desc_box.addWidget(self._description)

        self.container = QVBoxLayout()
        self.container.addSpacing(V_SPACING)
        self.container.addLayout(slider_box)
        self.container.addLayout(desc_box)

    def __changeValue(self, value, board=None):

        # Smooth or not slider updating
        sliderControl.__SMOOTH_SLIDER[self.__smooth](self._slider, value, self.__step)
        sliderControl.__SMOOTH_VALUE[self.__smooth](self._value_label, value, self.__step)

        # This shit update pwm value for Arduino
        # sliderControl.__INVERSE_PWM[self.__inverse](self.board, self.pin, value, self.range[1])

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
