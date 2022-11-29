# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:53:28 2022

@author: Юрец
"""

print("Введите три целых числа x, y, z")

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

a = (((x ** 5 + 9) / (abs(-8) * y)) ** (1 / 3)) / (7 - z % y)

print(round(a, 3))