# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:16:22 2022

@author: Юрец
"""

print("Решение кв. уравнения | ax ^ 2 + bx + c = 0")
print("Введите коэффициенты квадратного уравнения")

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

m = int(input("Введите минимальное значение отрезка: "))
n = int(input("Введите максимальное значение отрезка: "))

d = b ** 2 - 4*a*c

if d < 0:
    print("Решений нет")
    
elif d == 0:
    x = -b / (2*a)
    print("x = ", x)
    
    if m <= x <= n:
        print("Решение уравнения попадает в отрезок [", m, ";", n, "]")
    else:
        print("Решение уравнения не попадает в отрезок [", m, ";", n, "]")
        
else:
    x1 = (-b - d**0.5) / (2*a)
    x2 = (-b + d**0.5) / (2*a)
    print("x1 = ", x1, " x2 = ", x2)
    
    if (m <= x1 <= n) or (m <= x2 <= n):
        print("Решение уравнения попадает в отрезок [", m, ";", n, "]")
    else:
        print("Решение уравнения не попадает в отрезок [", m, ";", n, "]")