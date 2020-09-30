from components.Window import Window
from components.Slider import Slider
from components.Select import Select
from style.windows import ModernWindow
from assets.app_text import *
from style.global_layout import GLOBAL_STYLE
from PyQt5.QtWidgets import QApplication
from assets.pymata.pymata4 import pymata4
import sys

def main():

    board = pymata4.Pymata4(arduino_wait=1)

    app = QApplication(sys.argv)
    app.setStyle(GLOBAL_STYLE)

    slider_osc = Slider(pin=10, initial_value=0, name='Внешняя сила', range=(0, 255, 1),
                               desc=OSC_SLIDER_DESC, inverse=True, board=board, ptype='pwm')

    slider_damp = Slider(pin=9, initial_value=0, name='Затухание', range=(0, 255, 1),
                                desc=DAMP_SLIDER_DESC, last_item=True, board=board, ptype='pwm')

    window = ModernWindow(Window(components = (slider_osc, slider_damp), title='Маятник Поля', cright=True))
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()