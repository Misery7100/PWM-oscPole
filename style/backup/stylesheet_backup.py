STYLE = '#windowFrame {\
  border: 1px solid rgb(184, 184, 184);\
  border-radius: 5px 5px 5px 5px;\
  background-color: palette(Window);\
}\
\
#titleBar {\
  border: 0px none palette(base);\
  border-top-left-radius: 5px;\
  border-top-right-radius: 5px;\
  background-color: palette(Window);\
  height: 24px;\
}\
\
#btnClose, #btnRestore, #btnMaximize, #btnMinimize {\
  min-width: 14px;\
  min-height: 14px;\
  max-width: 14px;\
  max-height: 14px;\
  border-radius: 7px;\
  margin: 5px;\
}\
\
#btnRestore, #btnMaximize {\
  background-color: hsv(123, 204, 198);\
}\
\
#btnRestore::hover, #btnMaximize::hover {\
  background-color: hsv(123, 204, 148);\
}\
\
#btnRestore::pressed, #btnMaximize::pressed {\
  background-color: hsv(123, 204, 98);\
}\
\
#btnMinimize {\
  background-color: hsv(38, 218, 253);\
}\
\
#btnMinimize::hover {\
  background-color: hsv(38, 218, 203);\
}\
\
#btnMinimize::pressed {\
  background-color: hsv(38, 218, 153);\
}\
\
#btnClose {\
  background-color: hsv(0, 182, 252);\
}\
\
#btnClose::hover {\
  background-color: hsv(0, 182, 202);\
}\
\
#btnClose::pressed {\
  background-color: hsv(0, 182, 152);\
}\
\
#btnClose::disabled, #btnRestore::disabled, #btnMaximize::disabled, #btnMinimize::disabled {\
  background-color: palette(midlight);}'