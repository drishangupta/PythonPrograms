# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 01:01:01 2023

@author: drish
"""

import cv2
import numpy as np
blank=np.zeros((100,100,3))#making a black canvas with numpy zero
cv2.imwrite("Blank.jpg", blank)
photo=cv2.imread("Blank1.jpg")#edited blank in paint and opening it in python 
blank=photo                         #and copied its color schemes into blank variable
cv2.imshow("hi",blank)
cv2.waitKey()
cv2.destroyAllWindows()