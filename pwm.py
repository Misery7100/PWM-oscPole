from components.mainWindow import mainWindow
from components.sliderControl import sliderControl
from components.selectControl import selectControl
from style.windows import ModernWindow
from assets import required
from assets.app_text import *
from style.global_layout import GLOBAL_STYLE

from PyQt5.QtWidgets import QApplication
import sys

def main():

    # board = pymata4.Pymata4()

    app = QApplication(sys.argv)
    app.setStyle(GLOBAL_STYLE)

    required.addRequired()

    slider_osc = sliderControl(pin=11, initial_value=0, name='Osc amplitude', range=(0,255,1),
                               desc=OSC_SLIDER_DESC, inverse=True)

    slider_damp = sliderControl(pin=6, initial_value=0, name='Damper', range=(0,255,1),
                                desc=DAMP_SLIDER_DESC, last_item=True)

    window = ModernWindow(mainWindow(components = (slider_osc, slider_damp), title='PWM oscPole'))
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()