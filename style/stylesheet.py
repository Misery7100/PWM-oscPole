# background-color: palette(Window); - for #windowFrame
# border: 1px solid rgb(218, 218, 218); - for #windowFrame
# background-color: hsv(38, 218, 253); - minimize btn; hsv(0, 182, 252); - close btn

STYLE = '#windowFrame {\
  border: 0px solid rgb(218, 218, 218);\
  border-radius: 8px 8px 8px 8px;\
  background: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 rgb(243, 243, 243), stop:1 rgb(226, 226, 226));\
}\
#nameLabel {\
  color: rgb(20, 20, 20);\
  background-color: none;\
  border: 0px none black;\
  text-align: left;}\
\
#titleBar {\
  border: 0px none palette(base);\
  border-top-left-radius: 8px;\
  border-top-right-radius: 8px;\
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
  background: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 #fac467, stop:1 #fdae25);\
  margin-right: 3px;\
}\
\
#btnMinimize::hover {\
  background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 #de9a25, stop:1 #cf9023);\
}\
\
#btnMinimize::pressed {\
  background-color: hsv(38, 218, 153);\
}\
\
#btnClose {\
  background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 #f67878, stop:1 #fc4848);\
}\
\
#btnClose::hover {\
  background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 #d64040, stop:1 #bc3636);\
}\
\
#btnClose::pressed {\
  background-color: hsv(0, 182, 152);\
}\
\
#btnClose::disabled, #btnRestore::disabled, #btnMaximize::disabled, #btnMinimize::disabled {\
  background-color: palette(midlight);}'