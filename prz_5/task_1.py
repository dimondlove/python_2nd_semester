# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:58:56 2022

@author: Юрец
"""

numbers = (10, 9, 3, -5, 7, 0, 15)
print(numbers)

isFloat = False

for i in numbers:
    if not type(i) is int:
        isFloat = True
        
if not isFloat:
    numbers = tuple(sorted(numbers))
    print("\nКортеж отсортирован!")
else:
    print("\nИсходный кортеж:")
    
print(numbers)