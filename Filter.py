import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap1= cv2.VideoCapture(1)

while(True):
    ret, frame = cap.read()
    ret1, frame1=cap1.read()
    scale_percent = 30 # percent of original size
    width = int(frame1.shape[1] * scale_percent / 100)
    height = int(frame1.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized=cv2.resize(frame1, dim,interpolation = cv2.INTER_AREA)
    frame[0:144,0:192]=resized
    #framenew=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)
    framenew=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    cv2.imshow("frme2",framenew)
    offkey=cv2.waitKey(10)
    if offkey == 13:
        break

cap.release()
cv2.destroyAllWindows()