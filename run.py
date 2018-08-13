import win32print
import win32ui
from PIL import Image, ImageWin
import cv2
import numpy as np
import time

global pic_countdown
pic_countdown = -1
def foo(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global pic_countdown
        if pic_countdown == -1:
            pic_countdown = 10



window_name = 'frame'
file_names = ["filename_0.png", "filename_1.png","filename_2.png","filename_3.png"]
cam = cv2.VideoCapture(0)
frame = np.zeros((512,512,3), np.uint8)
capture_index = 0

fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)


cv2.namedWindow(window_name)
cv2.imshow(window_name, frame)
cv2.setMouseCallback(window_name, foo)

while(True) :
 # Capture frame-by-frame
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)

    # Display the resulting frame
    if(0 < pic_countdown) :
        cv2.putText(frame,"Ready?" + str(pic_countdown), (100, 100), fontface, fontscale, fontcolor)
        pic_countdown = pic_countdown - 1
    elif(pic_countdown == 0):
        frame = cv2.flip(frame, 1)
        file_name = str(time.time()) + ".png"
        cv2.imwrite(file_name, frame)
        pic_countdown = pic_countdown - 1
    else :
        cv2.putText(frame,"Slaap" + str(pic_countdown), (100,100), fontface, fontscale, fontcolor)

    cv2.imshow(window_name, frame)
    if cv2.waitKey(14) & 0xFF == ord('q'):
        break
#
# cv2.destroyAllWindows()
# while(True):
#     ret, frame = cam.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)
#         # write the flipped frame
#         cv2.imshow(window_name, frame)
#         cv2.setMouseCallback(window_name, foo)
#     else:
#         print('read failed')
#
# cv2.namedWindow(window_name)
# cv2.setMouseCallback(window_name, foo)
