# Задача 1. Задайте список случайных чисел от 1 до 10,
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random
my_list = [random.randint(1, 11) for i in range(10)]
print(f'Исходный список: {my_list}')

new_list = list(filter(lambda i: i > 5, my_list))

# или без lambda
# new_list = list(my_list[i] for i in range(len(my_list)) if my_list[i]>5)
print(f'Отфильтрованный список: {new_list}')
