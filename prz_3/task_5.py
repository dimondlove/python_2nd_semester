# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:55:41 2022

@author: Юрец
"""

st = "Это строка, в ней нет ничего особенного"
letter = "о"

if st.find(letter) == -1:
    print("В строке \"{}\" нету буквы \"{}\"".format(st, letter))
else:
    print("Индекс первого вхождения буквы \"{}\" - {}, индекс последнего "\
          "вхождения - {}.".format(letter, st.find(letter), st.rfind(letter)))