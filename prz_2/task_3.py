# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:10:47 2022

@author: Юрец
"""

print("Введите значения сопротивления проводников")

#Ввод вещественных чисел
a = float(input("1-ый проводник: "))
b = float(input("2-ой проводник: "))

c = round((a + b), 1)

print("Общее сопротивление цепы равно", c ,"Ом")