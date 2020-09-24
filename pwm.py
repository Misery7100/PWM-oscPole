from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from pymata4 import pymata4
from PyQt5.QtGui import QPixmap
import sys

class pwmUI(QWidget):

    OUTPUT_PIN = 11
    DESCRIPTION = 'With this software you can manipulate some ' \
                           'parameters.'

    def __init__(self, board):
        super().__init__()
        self.board = board
        self.board.set_pin_mode_pwm_output(pwmUI.OUTPUT_PIN)
        self.initUI()

    def initUI(self):

        boxed = QVBoxLayout()
        box0 = QHBoxLayout()
        box1 = QHBoxLayout()

        sld = QSlider(Qt.Horizontal, self)
        sld.setRange(0, 255)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setPageStep(1)

        sld.valueChanged.connect(self.updateLabel)

        self.label = QLabel('0', self)
        self.text = QLabel(pwmUI.DESCRIPTION, self)
        self.text.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.text.setMinimumWidth(80)

        self.label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.label.setMinimumWidth(80)

        box1.addWidget(sld)
        box1.addSpacing(15)
        box1.addWidget(self.label)

        box0.addWidget(self.text)

        boxed.addLayout(box0)
        boxed.addLayout(box1)

        self.setLayout(boxed)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle('PWM changer')
        self.show()

    def updateLabel(self, value):

        self.label.setText(str(value))
        self.board.pwm_write(pwmUI.OUTPUT_PIN, value)

def main():

    board = pymata4.Pymata4()
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = pwmUI(board=board)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()