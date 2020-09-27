from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QLabel, QPushButton)
from PyQt5.QtCore import Qt, QTimer
# from pymata4 import pymata4
from PyQt5.QtGui import QCursor, QFont
from style.global_layout import *

class Slider(QWidget):

    __SMOOTH_VALUE = {False: lambda l, v, step: l.setText(str(step*(v // step))),
              True: lambda l, v, step: l.setText(str(v))}

    __SMOOTH_SLIDER = {False: lambda s, v, step: s.setValue(step*(v // step)),
              True: lambda s, v, step: None}

    # __SMOOTH_PWM = {True: lambda b, pin, v, m, step, inv: Slider.__INVERSE_PWM[inv](b, pin, v, m),
    #                 False: lambda b, pin, v, m, step, inv: Slider.__INVERSE_PWM[inv](b, pin, step*(v // step), m)}
    #
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
        name_label = ToggleButton(name, self, clicked=self.__toggleVisible, style='sliderLabel', width=SLIDER_LABEL_WIDTH)

        # Add value displaying
        self._value_label = SliderText(str(initial_value), self, width=SLIDER_VALUE_WIDTH, style='sliderValue', lim=True)

        # Add slider
        self.__step = range[-1]
        self.__max_val = range[1]
        self.__smooth = smooth
        self._slider = SliderControl(type=Qt.Horizontal, widget=self, range=range[:-1], step=self.__step,
                                     width=SLIDER_WIDTH, changed=self.__changeValue, in_val=initial_value)

        # Add +/- buttons
        plus_btn = ControlButton('+', self, released=self.__plusStop, pressed=self.__plusStart)
        minus_btn = ControlButton('-', self, released=self.__minusStop, pressed=self.__minusStart)

        # Add timers for +/- buttons
        self.__plus_timer = TimerWithDelay(object=self._slider, step=self.__step, direction='+')
        self.__minus_timer = TimerWithDelay(object=self._slider, step=self.__step, direction='-')

        self._description = SliderText(desc, self, align=Qt.AlignLeft | Qt.AlignTop, font=DESCRIPRION_FONT,
                                       width=GLOBAL_WIDTH, lim=True, word_wrap=True, desc=True, last=last_item)

        slider_box = QHBoxLayout()
        slider_box.addWidget(name_label)
        slider_box.addSpacing(H_SPACING)
        slider_box.addWidget(self._slider)
        slider_box.addSpacing(H_SPACING)
        slider_box.addWidget(minus_btn)
        slider_box.addWidget(self._value_label)
        slider_box.addWidget(plus_btn)
        slider_box.setAlignment(Qt.AlignJustify)

        desc_box = QHBoxLayout()
        desc_box.addWidget(self._description)
        desc_box.setAlignment(Qt.AlignLeft)

        self.container = QVBoxLayout()
        self.container.addSpacing(V_SPACING)
        self.container.addLayout(slider_box)
        self.container.addLayout(desc_box)

    def __changeValue(self, value, board=None):

        # Smooth or not slider updating
        Slider.__SMOOTH_SLIDER[self.__smooth](self._slider, value, self.__step)
        Slider.__SMOOTH_VALUE[self.__smooth](self._value_label, value, self.__step)

        # This shit update pwm value for Arduino
        # Slider.__SMOOTH_PWM[self.__smooth](self.board, self.__pin, value, self.__max_val, self.__step, self.__inverse)

    def __plusStart(self):
        self._slider.setValue(self._slider.value() + self.__step)
        self.__plus_timer.delay.start()

    def __minusStart(self):
        self._slider.setValue(self._slider.value() - self.__step)
        self.__minus_timer.delay.start()

    def __plusStop(self):
        self.__plus_timer.delay.stop()
        self.__plus_timer.timer.stop()

    def __minusStop(self):
        self.__minus_timer.delay.stop()
        self.__minus_timer.timer.stop()

    def __toggleVisible(self):
        if self._description.isVisible():
            self._description.setVisible(False)
        else:
            self._description.setVisible(True)

class ControlButton(QPushButton):

    def __init__(self, label, widget, **kwargs):
        super().__init__(label, widget)
        self.addButton(**kwargs)

    def addButton(self, released=None, pressed=None, cursor=None, width=INC_BUTTON_WIDTH):

        self.setMaximumWidth(width)
        self.pressed.connect(pressed)
        self.released.connect(released)

        if not cursor is None:
            self.setCursor(cursor)
        else:
            self.setCursor(QCursor(Qt.PointingHandCursor))

class ToggleButton(QPushButton):

    def __init__(self, label, widget, **kwargs):
        super().__init__(label, widget)
        self.addButton(**kwargs)

    def addButton(self, clicked=None, cursor=None, width=SLIDER_LABEL_WIDTH, style=None):

        self.setMaximumWidth(width)
        self.clicked.connect(clicked)
        self.setMinimumWidth(width)
        self.setMaximumWidth(width)
        self.setFont(TEXT_FONT)

        if not style is None: self.setObjectName(style)

        if not cursor is None:
            self.setCursor(cursor)
        else:
            self.setCursor(QCursor(Qt.PointingHandCursor))

class SliderText(QLabel):

    __LIMITED = {True: lambda text, w: (text.setMaximumWidth(w), text.setMinimumWidth(w)),
               False: lambda text, w: text.setMinimumWidth(w)}

    __DESCRIPRION_LAST = {True: lambda text: text.setObjectName('descriptionLast'),
                        False: lambda text: text.setObjectName('description')}

    __DESCRIPTION = {True: lambda text, last: (SliderText.__DESCRIPRION_LAST[last](text), text.setVisible(False)),
                   False: lambda text, last: None}

    def __init__(self, label, widget, **kwargs):
        super().__init__(label, widget)
        self.addText(**kwargs)

    def addText(self, align=Qt.AlignCenter, width=0, style=None, font=VALUE_FONT, lim=False, word_wrap=False,
                last=False, desc=False):

        self.setAlignment(align)
        self.setObjectName(style)
        self.setFont(font)
        self.setWordWrap(word_wrap)

        SliderText.__LIMITED[lim](self, width)
        SliderText.__DESCRIPTION[desc](self, last)

class SliderControl(QSlider):

    def __init__(self, type, widget, **kwargs):
        super().__init__(type, widget)
        self.addControl(**kwargs)

    def addControl(self, range=(0,1), step=1, in_val=0, changed=None, width=0):

        self.setRange(*range)
        self.setFocusPolicy(Qt.NoFocus)
        self.setPageStep(step)
        self.setSingleStep(step)

        self.setValue(in_val)
        self.setTickInterval(step if step > SLIDER_TICK_MIN else SLIDER_TICK_MIN)
        self.setTickPosition(QSlider.TicksBothSides)

        self.setMinimumWidth(width)
        self.setMaximumWidth(width)

        self.valueChanged.connect(changed)

class TimerWithDelay():

    __SLIDER_EVENT = {
        '+': lambda obj, step: lambda: obj.setValue(obj.value() + step),
        '-': lambda obj, step: lambda: obj.setValue(obj.value() - step)
    }

    def __init__(self, **kwargs):
        self.addTimer(**kwargs)

    def addTimer(self, object, step, timer_int=ITERATE_INTERVAL, delay_int=DELAY_INTERVAL, direction='+'):

        self.timer = QTimer()
        self.timer.setInterval(timer_int)

        timeout_event = TimerWithDelay.__SLIDER_EVENT[direction](object, step)
        self.timer.timeout.connect(timeout_event)

        self.delay = QTimer()
        self.delay.setSingleShot(True)
        self.delay.setInterval(delay_int)

        self.delay.timeout.connect(lambda: self.timer.start())
