from PyQt5.QtGui import QFont

# ------ App -------

GLOBAL_STYLE = 'Fusion'

# -- Main Window ---

WIN_POS = (600, 200)
WIN_SIZE = (400, 300)

# ---- Elements ----

GLOBAL_WIDTH = int(WIN_SIZE[0])
INC_BUTTON_WIDTH = 20
SLIDER_WIDTH = int(WIN_SIZE[0]*0.5)
SLIDER_LABEL_WIDTH = int(WIN_SIZE[0]*0.27)
SLIDER_VALUE_WIDTH = int(WIN_SIZE[0]*0.1)
SLIDER_TICK_MIN = 15
SLIDER_RANGE = (0, 255)
COPYRIGHT_HEIGHT = 20

# ------ Text ------

MAIN_FONT = 'Calibri'

TEXT_FONT = QFont(MAIN_FONT, 13, QFont.Bold)
VALUE_FONT = QFont(MAIN_FONT, 14, QFont.Bold)
DESCRIPRION_FONT = QFont(MAIN_FONT, 11, QFont.Light)
COPYRIGHT_FONT = QFont(MAIN_FONT, 10, QFont.ExtraLight)

# ---- Spacings ----

H_SPACING = int(WIN_SIZE[0]*0.03)
V_SPACING = int(WIN_SIZE[0]*0.03)

# ----- Timers -----

ITERATE_INTERVAL = 40
DELAY_INTERVAL = 600