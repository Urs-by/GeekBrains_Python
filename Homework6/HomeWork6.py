# Задача 1. Дано натуральное число N. Найдите значение выражения:
# N + NN + NNN. N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396
#
# number = input("Введите положительно целое число N: ")
# my_list = [number]
# for i in range(2):
#     item = my_list[i] + number
#     my_list.append(item)
# res = list(map(int, my_list))
# print(f"{res[0]} + {res[1]} + {res[2]}  = {sum(res)}")

# Задача 2. Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет, есть в массиве последовательность
# из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет


# import random
#
# my_list = [random.randint(0, 9) for i in range(15)]
# print(my_list)
# number = list(input("Введите трёхзначное натуральное число: "))
# # переводим все значения number в int
# number_list = list(map(int, number))
#
# # проверяем есть ли в списке my_list все элементы из number
# ingoing = list(map(lambda i: i in my_list, number_list))
# if ingoing.count(True) == 3:
#     for i in range(len(my_list)):
#         if my_list[i] == number_list[0]:
#             # в res записываем разницу между каждым элементом из number и среза 3х элементов my_list
#             res = list(map(lambda x, y: x - y, number_list, my_list[i:i + 3]))
#             if res.count(0) == 3:
#                 print("Да")
#                 break
#     else:
#         print('Нет')
# else:
#     print('Нет')

# Задача 3. Найдите все простые несократимые дроби,
# лежащие между 0 и 1, знаменатель которых не превышает 11

# функция находит сократимые дроби
def multiplicity(i, j):
    for k in range(2, 10):
        if i % k == 0 and j % k == 0:
            return 1

print("Bсе простые несократимые дроби, лежащие между 0 и 1")
for i in range(1, 10):
    for j in range(1, 12):
        if i / j < 1:
            if multiplicity(i, j) != 1:
                print(i, '/', j)
