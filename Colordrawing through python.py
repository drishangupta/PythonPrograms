import numpy as np
import cv2
canvas=np.zeros((100,100,3))
canvas[0:33]=[0,0,255]
canvas[33:68]=[255,255,255]
canvas[34:67,34:67]=[255,0,0]
canvas[68:100]=[0,255,0]
cv2.imshow('hi',canvas)
cv2.waitKey()
cv2.destroyAllWindows()

