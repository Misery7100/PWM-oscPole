from components import mainWindow, sliderControl, selectControl
from style import windows
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui
import sys


def main():

    # board = pymata4.Pymata4()
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    QtGui.QFontDatabase.addApplicationFont("style/Roboto-Light.ttf")

    slider_osc = sliderControl.sliderControl(pin=11, initial_value=0, name='Osc amplitude', range=(0,255,1),
                                          desc='PWM control for a torsion oscillator driving force. '
                                               'Click buttons or slide to increase or decrease value. '
                                               '\n\n ⦁ Smooth changing; '
                                               '\n ⦁ Tick step is 1/15 of PWM maximum value.', inverse=True)

    slider_damp = sliderControl.sliderControl(pin=6, initial_value=0, name='Damper', range=(0,255,1), last_item=True,
                                          desc='PWM control for a torsion oscillator damper (magnetic field). '
                                               'Click buttons or slide to increase or decrease value. '
                                               '\n\n ⦁ Smooth changing; '
                                               '\n ⦁ Tick step is 1/15 of PWM maximum value.')

    window = mainWindow.mainWindow(components = (slider_osc, slider_damp), title='PWM oscPole')
    mw = windows.ModernWindow(window)
    mw.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()