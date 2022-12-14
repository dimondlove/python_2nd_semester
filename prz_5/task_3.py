# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:42:35 2022

@author: Юрец
"""

st = "Это строка, в ней нет ничего особенного. В ней правда нет ничего особенного."

plenty = set(st)

print("Исходная строка: \"{}\"".format(st))

print("\nМножество: {}, его мощность равна {}.".format(plenty, len(plenty)))
