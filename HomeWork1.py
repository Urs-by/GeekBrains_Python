# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

'''week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
n = int(input ('Введите цифру, обозначающую день недели: '))
if n < 1 or n > 7:
    print("Нет такого дня")
else:
    print(week_days[n-1])'''

# Задача 2. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

'''ax = int(input("Введите координату Х точки А: "))
ay = int(input("Введите координату Y точки А: "))
bx = int(input("Введите координату Х точки B: "))
by = int(input("Введите координату Y точки B: "))
# применяем теорему Пифагора
print('Расстояние между точками А и В = ', round(((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5, 2))'''

# Задача 3. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

n = int(input('Введите число: '))
if n < 1 or n > 4:
    print('Вы ввели несуществующий номер четверти!')
else:
    print(f'диапазон возможных координат точек в {n} четверти')
    if n == 1:
        print('x > 0, y > 0')
    elif n == 2:
        print('x > 0, y < 0')
    elif n == 3:
        print('x < 0, y < 0')
    else:
        print('x < 0, y > 0')



# Задача 4. Напишите программу, которая на вход принимает число (N),
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

'''n = int(input('Введите число: '))
n += 1
if n > 1:
    for i in range(2, n, 2):
        print(i)
else:
    print('нет четных чисел в заданном диапазоне!')'''
