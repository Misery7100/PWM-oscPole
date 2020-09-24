from components import mainWindow, sliderControl
from PyQt5.QtWidgets import QApplication
import sys

def main():

    # board = pymata4.Pymata4()
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    slider1 = sliderControl.sliderControl(pin=10, initial_value=64, name='Something', range=(0, 128, 16), smooth=False)
    slider2 = sliderControl.sliderControl(pin=9, initial_value=0, name='Osc amplitude')
    slider3 = sliderControl.sliderControl(pin=9, initial_value=256, name='Damper')
    window = mainWindow.mainWindow(components = (slider1, slider2, slider3))
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()