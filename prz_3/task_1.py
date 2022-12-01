# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:43:42 2022

@author: Юрец
"""

title_team = input("Введите название футбольной команды: ")
symbols = "-"

print()
print(title_team, "- чемпион!")
print(symbols * len(title_team))
title_team = title_team.lower()
print(title_team)
print()
print("Длина наименования команды:", len(title_team))
print("\nЕсть ли буква \"п\" в наименование команды:", "п" in title_team)
print("\nБуква \"а\" повторяется", title_team.count("а") , "раз.")