# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:03:07 2022

@author: Юрец
"""

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

if a == b:
    print("\nЧисла a и b равны!")
elif a > b:
    print("\nМаксимальное число a={}. Минимальное число b={}".format(a, b))
else:
    print("\nМаксимальное число b={}. Минимальное число a={}".format(b, a))