# Семинар 2, Задача 1
# Напишите программу, которая принимает на вход число N и
# выдает список факториалов для чисел от 1 до N
# например N =4 -> [1,2,6,24]

'''def sum_factorial(n):
    sum = 1
    for i in range(1, n+1):
       sum = sum*i
    return sum

list = []
n = int(input('Введите положительное число N: '))
if n  >0:
    for i in range(n):
        list.append(sum_factorial(i+1))
    print(f'cписок факториалов для чисел от 1 до {n}\n', list)
else:
    print("Введенное число не корректно для заданоого условия задачи")'''

# Семинар 2, Задача 2
# Выведите таблицу истинности для выражения
# ¬(X ∧ Y) ∨ Z

'''def table():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print (x, y, z, " ", int(not(x and y) or z))

print('таблица истинности для выражения: ¬(X ∧ Y) ∨ Z')
print ("x","y","z"," ¬(X ∧ Y) ∨ Z")
table()'''

# Семинар 2, Задача 3
# Даны 2 строки. Посчитайте сколько раз каждый символ первой строки встречается во второй:
#  'one' 'onetwonine'  o->2, n->3, e->3

'''first_str = input('Введите первую строку: ')
second_str = input('Введите вторую строку: ')

# Метод 1 - тичерство
#for i in first_str:
#    print(f' элемент {i} встречается во второй строке {second_str.count(i)} раз(а)')

# Метод 2

for i in first_str:
    count = 0
    for j in second_str:
        if i == j:
            count += 1
    print(f' элемент {i} встречается во второй строке {count} раз(а)')'''


# Семинар 2, Задача 4
# Задайте список из N элементов, заполненных числами из промежутка [-N,N]
# Сдвинте все элементы списка на 2 позиции вправо

# функция сдвига чисел на 1 шаг
def step(list):
    for i in range(len(list) - 1, 0, -1):
        temp = list[i - 1]
        list[i - 1] = list[i]
        list[i] = temp
    return list


n = int(input("Введите число N :"))
count = abs(int(input("Введите на сколько шагов нужно сдвинуть элементы списка вправо :")))

# создаем первоначальный список
list = []
for i in range(-n, n + 1):
    list.append(i)
print(f" Первоначальный список :\n {list}")
# Сдвигаем элементы списка на заданное количество шагов
for i in range(count):
    step(list)

print(f" Измененный список :\n {list}")

