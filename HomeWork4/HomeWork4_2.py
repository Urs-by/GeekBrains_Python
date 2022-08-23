# Задача 2. В первой строке файла находится информация об ассортименте мороженного,
# во второй - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»
def readstroke (str):
    with open('icecream.txt', encoding="utf-8") as name:
        data = name.readlines()[str].strip().split(',')
        return data

str1 = set(readstroke(0))
str2 = set(readstroke(1))
stoped = list(str1.difference(str2))
print("Закончилось мороженное: ")
for i in stoped:
    print(i)