# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:29:37 2022

@author: Юрец
"""

st = "Это строка, в ней нет ничего особенного. В ней правда нет ничего особенного."
del_char = " " #Символ который будем удалять из строки

for i in range(0, 3):
    char = ""
    max_count = 0
    st = st.replace(del_char, "")
    
    for i in range(len(st)):
        if st.count(st[i]) > max_count:
            char = st[i]
            max_count = st.count(st[i])
    
    print("{} - {}".format(char, max_count))
    del_char = char
