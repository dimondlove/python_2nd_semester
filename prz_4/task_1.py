# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:13:02 2022

@author: Юрец
"""

a = []
b = []

a.append(4.5)
a.append(3.4)

a.extend([8.7, 1.3])

b.append(14.5)
b.append(3.4)

b.extend([8.7, 11.3])

a.insert(1, 100)
a.insert(3, 100)

b.insert(0, 200)
b.insert(2, 200)

print("Исходные списки:")
print(a)
print(b)

del a[0]
del b[0]

a.remove(100)
b.remove(200)

print("\nПосле удалений:")
print(a)
print(b)

sa = set(a)
sb = set(b)
sa_and_sb = sa & sb

print("\nУникальные элементы:")
print("В первом множестве", sa)
print("Во первом множестве", sb)
print("Общие:", sa_and_sb)

c = a + b

c_asc = sorted(c)
c_desc = sorted(c, reverse=True)

sr_ar = round(((c[1] + c[3] + c[5] + c[7]) / 4), 2)
sr_geom = round(((c[0] * c[2] * c[4] * c[6])**(1./4.)), 2)

c_max = max(c)
c_min = min(c)

print("\nИтоговые:")
print(c)
print("Сортировка (возр.):", c_asc)
print("Сортировка (убыв.):", c_desc)
print("Ср. арифм. = {}, ср. геометр. = {}".format(sr_ar, sr_geom))
print("Макс. = {} и мин. = {}".format(c_max, c_min))