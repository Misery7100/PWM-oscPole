STYLE = '#windowFrame {\
  border: 1px solid rgb(194, 194, 194);\
  border-radius: 8px 8px 8px 8px;\
  background-color: palette(Window);\
}\
\
#titleBar {\
  border: 0px none palette(base);\
  border-top-left-radius: 5px;\
  border-top-right-radius: 5px;\
  background-color: palette(Window);\
  height: 30px;\
}\
\
#btnClose, #btnRestore, #btnMaximize, #btnMinimize {\
  min-width: 16px;\
  min-height: 16px;\
  max-width: 16px;\
  max-height: 16px;\
  border-radius: 8px;\
  margin: 7px;\
}\
\
#btnMinimize {\
  background-color: hsv(38, 218, 253);\
  margin-right: 3px;\
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