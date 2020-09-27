from components.Window import Window
from components.Slider import Slider
from components.Select import Select
from style.windows import ModernWindow
from assets.app_text import *
from style.global_layout import GLOBAL_STYLE
from PyQt5.QtWidgets import QApplication
import sys

def main():

    # board = pymata4.Pymata4()

    app = QApplication(sys.argv)
    app.setStyle(GLOBAL_STYLE)

    slider_osc = Slider(pin=11, initial_value=0, name='Osc amp', range=(0, 255, 1),
                               desc=OSC_SLIDER_DESC, inverse=True)

    slider_damp = Slider(pin=6, initial_value=0, name='Damper', range=(0, 255, 1),
                                desc=DAMP_SLIDER_DESC, last_item=True)

    window = ModernWindow(Window(components = (slider_osc, slider_damp), title='PWM oscPole', cright=True))
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()