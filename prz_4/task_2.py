# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:47:47 2022

@author: Юрец
"""

list_1 = ["горец", "кидаться", "перетянуть", "мэр", "папаха", "поведение",
          "информатика", "музей", "трутник", "угол"]
list_2 = []

print("Исходный список:")
print(list_1)

max_length = 0

for i in range(len(list_1)):
    if len(list_1[i]) > max_length:
        max_length = len(list_1)
        max_i = i
        
for i in range(len(list_1)):
    list_2.append(list_1[i] + '_' * (max_length - len(list_1[i])))
        
print("\nСписок после обработки:")
print(list_2)