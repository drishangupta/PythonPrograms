# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:45:09 2023

@author: drish
"""

import cv2
import numpy as np
pic1=cv2.imread("mamtause.jpg")
pic01=pic1[75:400,80:350]
pic2=cv2.imread("narendramodi.jpg")
pic1[75:400,80:350]=pic2[75:400,80:350]
cv2.imshow("modi",pic1)
cv2.waitKey()
cv2.destroyAllWindows()
