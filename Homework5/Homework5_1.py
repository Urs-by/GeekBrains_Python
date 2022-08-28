# Задача 1. Задайте список случайных чисел от 1 до 10,
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random
# my_list = [random.randint(1, 11) for i in range(10)]
# print(f'Исходный список: {my_list}')
#
# new_list = list(filter(lambda i: i > 5, my_list))
#
# # или без lambda
# # new_list = list(my_list[i] for i in range(len(my_list)) if my_list[i]>5)
# print(f'Отфильтрованный список: {new_list}')

# # Задача 2. Дан список случайных чисел. Создайте список,
# # в который попадают числа, описывающие возрастающую последовательность.
# # Порядок элементов менять нельзя.
# # [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
#
# my_list = [random.randint(0,50) for i in range(10)]
# print(my_list)
#
# def subs (list, j):
#     temp = list[j]
#     new_list = [temp]
#     for i in range(j, len(list)):
#         if list[i] > temp:
#             temp = list[i]
#             new_list.append(list[i])
#     if len(new_list) > 1:
#         return new_list
# # new_list=list(map( lambda :  ,my_list))
#
# print("Возможные возрастающие последовательности: ")
# for i in range(len(my_list)):
#     new_list = subs(my_list, i)
#     if  new_list != None:
#         print(new_list)


# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаютСписок уникальных элементов [1, 4, 2, 3, 6, 7]

my_list = [random.randint(1, 10) for i in range(10)]
print("Исходный список:")
print(my_list)
unic_list = set(my_list)

count = list(map(lambda i: my_list.count(i), unic_list ))
res = list(filter( lambda i: i!=1, count))

print("Список уникальных элементов")
print(list(unic_list))
print(f"Bсего совпадающих элементов  в списке: {len(res)}")
