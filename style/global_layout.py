from PyQt5.QtGui import QFont

# ------ App -------

GLOBAL_STYLE = 'Fusion'

# -- Main Window ---

WIN_POS = (600, 200)
WIN_SIZE = (550, 250)

# ---- Elements ----

GLOBAL_WIDTH = int(WIN_SIZE[0]*0.9)
INC_BUTTON_WIDTH = 20
SLIDER_WIDTH = 200
SLIDER_LABEL_WIDTH = 120
SLIDER_VALUE_WIDTH = 50
SLIDER_TICK_MIN = 15
SLIDER_RANGE = (0, 255)
COPYRIGHT_HEIGHT = 20

# ------ Text ------

TEXT_FONT = QFont("Roboto", 11, 500)
VALUE_FONT = QFont("Roboto", 12, 500)
DESCRIPRION_FONT = QFont("Roboto", 10)
COPYRIGHT_FONT = QFont('Roboto', 8)

# ---- Spacings ----

H_SPACING = 15
V_SPACING = 15

# ----- Timers -----

ITERATE_INTERVAL = 50
DELAY_INTERVAL = 600