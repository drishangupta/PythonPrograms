# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 00:15:52 2023

@author: drish
"""

import cv2
cap=cv2.VideoCapture(1)
stat,pic=cap.read()
cv2.imwrite("hiimg.jpg", pic)
cv2.imshow("mypic", pic)
cv2.waitKey()
cv2.destroyAllWindows()
cap.release()