# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:48:54 2022

@author: Юрец
"""

st = "Это строка, в ней нет ничего особенного"
subst = "это строка"

if subst.lower() in st.lower():
    print("Подстрока есть")
else:
    print("Подстроки нет")