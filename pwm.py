from components import mainWindow, sliderControl, selectControl
from style import windows
from PyQt5.QtWidgets import QApplication
import sys


def main():

    # board = pymata4.Pymata4()
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    slider_osc = sliderControl.sliderControl(pin=11, initial_value=0, name='Osc amplitude',
                                          desc='PWM control for a torsion oscillator driving force. Smooth changing.'
                                               'Click on right or left slider side to increase or decrease value by'
                                               'tick step. Tick step is 1/15 of PWM maximum value.', inverse=True)

    slider_damp = sliderControl.sliderControl(pin=6, initial_value=0, name='Damper',
                                          desc='PWM control for a torsion oscillator damper (magnetic field). Step '
                                               'changing. Click on right or left slider side to increase or decrease value '
                                               'by tick step. Tick step is 1/15 of PWM maximum value.', smooth=False)

    window = mainWindow.mainWindow(components = (slider_osc, slider_damp), title='PWM oscPole')
    mw = windows.ModernWindow(window)
    mw.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()