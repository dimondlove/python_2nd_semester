# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:05:16 2022

@author: Юрец
"""

numbers = (10, 9, 3, -5, 7, 3, 0, -4, 29, 3, 15)
num = 3
new_numbers = ()

print("\nИсходный кортеж:")
print(numbers)

if numbers.count(num) == 1:
    index = numbers.index(num)
    new_numbers = numbers[index:]
    
elif numbers.count(num) >= 2:
    index_first = numbers.index(num)
    temp_numbers = list(numbers)
    temp_numbers.reverse()
    index_last = - temp_numbers.index(num)
    
    new_numbers = numbers[index_first:index_last]
    
print("\nНовый кортеж:")
print(new_numbers)