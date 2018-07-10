import win32print
import win32ui
from PIL import Image, ImageWin
import cv2

file_names = ["filename_0.png", "filename_1.png","filename_2.png","filename_3.png"]
cam = cv2.VideoCapture(0)

capture_index = 0
while(True) :
 # Capture frame-by-frame
    ret, frame = cam.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):

        gray = cv2.transpose(gray)
        gray = cv2.flip(gray, 0)  # transpose+flip(0)=CCW
        cv2.imwrite(file_names[capture_index], gray)
        capture_index = capture_index + 1
        if (capture_index == 4):
            break

PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111
printer_name = win32print.GetDefaultPrinter ()


hDC = win32ui.CreateDC ()
hDC.CreatePrinterDC (printer_name)
printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)

#dest_size =

hDC.StartDoc ('tmp.png')
hDC.StartPage ()

margin = 80
sizeX = int(frame.shape[0] * 1.8)
sizeY = int(frame.shape[1] * 1.8)
print("x: " + str(sizeX) )
print("y: " + str(sizeY) )

for indexX in range(4):
    bmp = Image.open (file_names[indexX])
    dib = ImageWin.Dib(bmp)
    startX = margin + (indexX * (margin + sizeX))
    startY = margin
    endX = (margin + sizeX) + (indexX * (margin + sizeX))
    endY = (margin + sizeY)
    dib.draw (hDC.GetHandleOutput (), (startX,startY, endX, endY))


hDC.EndPage ()
hDC.EndDoc ()
hDC.DeleteDC ()