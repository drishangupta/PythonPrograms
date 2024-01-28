# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 11:19:15 2023

@author: drish
"""

from threading import Thread
import time
def lwa():
    while True:
        print("aaaaaa")
def lwb():
    while True:
        print("bbbbbb")
thr1=Thread(target=lwa)
thr1.start()
time.sleep(3)
lwb()