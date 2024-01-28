# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:36:48 2023

@author: drish
"""

from cx_freeze import setup, Executable

setup(
    name="MyWindow",
    version="1.0",
    description="A summer project which integrates all of our technologies",
    executables=[Executable("MainSummerProject.py")]
)