# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 13:40:43 2022

@author: Юрец
"""

x = float(input("Введите вещественное число x: "))

if x >= 0:
    y = x**0.5 + x**2
else:
    y = 1 / x
    
print("При x={} y={}".format(x, y))