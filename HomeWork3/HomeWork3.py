# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи

'''data = open ('fibonachy.txt', 'w', encoding='UTF-8')
data.writelines("Последовательность Фибоначи:"+ '\n')
data.close()


n = int(input("Введите число N: "))
start = 0
list =[1]

for i in range(n-1):
    count = start+list[i]
    list.append(count)
    start = list[i]

with open ('fibonachy.txt', 'a') as data:
    data.writelines(str(list))'''

# Задача 2. В файле находятся названия фруктов.
# Выведите все фрукты, названия которых начинаются на заданную букву.
letter = input("Введите  букву: ")
print(f"Список фруктов на {letter}: ")
with open ('fruit.txt','r', encoding='utf-8') as frut:
    data = frut.readlines()
    for i in range(len(data)):
        if data[i][0] == letter.upper() or data[i][0] == letter.lower():
            print(data[i], end="")

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.


# bot_answer =  { "Привет" : " ой, кто здесь? ",
#       "я": "кто Я? Как тебя зовут?",
#       "как тебя зовут": "меня зовут БотПайПень I, а тебя? ",
#       "как дела" : "норм, а у тебя?",
#       "так себе" : "все будет хорошо!",
#       "норм": "ну и отлично!",
#       "что ты умеешь" : "в основном, слушаю",
#       "что":"лишбы-что",
#       "пока" : " и тебе не кашлять, жми 'Q'"  }
#
# name = None
# answer = input("Чтобы запустить бота наберите 'Привет' или Q для выхода: " + '\n')
# while answer != "Q":
#     if answer in bot_answer.keys():
#         print("BotPyPenI:   ", bot_answer[answer])
#         if answer == "я" or answer == "как тебя зовут":
#             name = input()
#             print(f"BotPyPenI:   Привет, {name} !")
#     else:
#         print("BotPyPenI:   Извини, не понял, памяти маловато!")
#     if name != None:
#         answer = input(f"{name} : ")
#     else:
#         answer = input("Вы : ")
