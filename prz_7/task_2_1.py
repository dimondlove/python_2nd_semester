# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:17:15 2022

@author: Юрец
"""

x = 1
s = 0
count = 0

while (x != 0):
    x = int(input("Введите x "))
    s += x
    count += 1
    
print("\nСумма введённых чисел равна {}. Количество введённых чисел равно {}.".format(s, count))