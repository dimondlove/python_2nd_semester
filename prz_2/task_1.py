# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:35:03 2022

@author: Юрец
"""

print("Введите два целых числа, a и b")

#Ввод целых чисел
a = int(input("a = "))
b = int(input("b = "))

print("\nАрифметические операции")
print(a, " + ", b, " = ", a + b)
print(a, " - ", b, " = ", a - b)
print(a, " * ", b, " = ", a * b)
print(a, " / ", b, " = ", round((a / b), 2))
print(a, " // ", b, " = ", a // b)
print(a, " % ", b, " = ", a % b)
print(a, " ** ", b, " = ", a ** b)

print("\n\nОперации сравнения")
print(a, " < ", b, " - ", a < b)
print(a, " <= ", b, " - ", a <= b)
print(a, " > ", b, " - ", a > b)
print(a, " >= ", b, " - ", a >= b)
print(a, " != ", b, " - ", a != b)
print(a, " == ", b, " - ", a == b)