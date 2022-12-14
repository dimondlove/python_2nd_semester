# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 23:05:40 2022

@author: Юрец
"""

info = dict()

info["фио"] = "Руднев Юрий Александрович"
info["дата_рождения"] = "30/04/2002"
info["место_рождения"] = "Воронеж"

print(info)

info["хобби"] = ["баскетбол"]

info["хобби"] += ["программирование"]

info["животные"] = ("Мурзик", "Марс")

info["ЕГЭ"] = dict()

info["ЕГЭ"]["основы_информационных_технологий"] = 67
info["ЕГЭ"]["инженерная_математика"] = 53
info["ЕГЭ"]["русский_язык"] = 66

info["ЕГЭ"]["химия"] = 0

del info["ЕГЭ"]["химия"]

info["вузы"] = dict()

info["вузы"]["ВГУИТ"] = 123

print("Данные:")
print(info)

exams = sorted(info["ЕГЭ"])
print("Предметы:", exams)

uni = sorted(info["вузы"])
print("Вузы:", uni)

print("\nОтветы на вопросы:")

name = info["фио"][7:11];
starts_with_vowel = True
print("* моё имя начинается на гласную букву:", starts_with_vowel)

month = info["дата_рождения"][3:5]
born_in_winter_or_summer = False
print("* родился летом или зимой:", born_in_winter_or_summer)

hobbies_count = len(info["хобби"])
print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info["хобби"][0]))

print("* после окончания школы сдавал {} экз.".format(len(info["ЕГЭ"])))

sum_mark = sum(info["ЕГЭ"].values());
print("* сумма баллов = {}".format(sum_mark))

max_mark = max(info["ЕГЭ"].values())
print("* макс. балл = {}".format(max_mark))

vuz_count = 0;
for i in info["вузы"].values():
        vuz_count += int(i < sum_mark)
        
print("* кол-во вузов в которые я прохожу: {}".format(vuz_count))