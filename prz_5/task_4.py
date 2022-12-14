# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:52:36 2022

@author: Юрец
"""

from collections.abc import Hashable

lst = [10, "строка,", 9, 3, -5, 7, 3, 0, ".", -4, 29, 3, 15, "Это"]
       
print("Исходный список: {}".format(lst))

st = set()

for i in lst:
    if isinstance(i, Hashable):
        st.add(i)
        
print("\nМножество: {}".format(st))