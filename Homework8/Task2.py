# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
import random

size = int(input("Введите размер матрицы: "))
matrix = [[random.randint(1, 10) for i in range(size)] for y in range(size)]

sum_main_diagonal = 0
for i in range(size):
    sum_main_diagonal += matrix[i][i]

for i in matrix:
    print(i)
print()
print(f"Cуммa элементов главной диагонали = {sum_main_diagonal}")

count = 0
for i in range(len(matrix)):
    if sum(matrix[i]) > sum_main_diagonal:
        count += 1
        print(f"Суммa элементов {i + 1}-й строки = {sum(matrix[i])} превышает сумму элементов главной диагонали")

if count == 0:
    print("В матрице нет строк, сумма элементов которых превышает сумму элементов главной диагонали")
