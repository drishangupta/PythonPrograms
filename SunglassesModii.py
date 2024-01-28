# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 12:16:56 2023

@author: drish
"""

import cv2
pic1=cv2.imread("narendramodi.jpg")
pic2=cv2.imread("sunglasses.png")
pic1[100:140,150:]=pic2[:,:]
cv2.imshow("hi",pic2)
cv2.waitKey()
cv2.destroyAllWindows()