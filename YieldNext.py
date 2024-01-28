# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 15:19:27 2023

@author: drish
"""
#generator 
def lw():
        for j in ["vimal","rahul","jack"]:
            yield(j)
x=lw()
for i in range(3):
    print(next(x))