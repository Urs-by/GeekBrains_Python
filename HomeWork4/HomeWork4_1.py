# Задача 1. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа
# N. 60 -> 2, 2, 3, 5

n = int(input("Введите натуральное число N: "))
a = n
list_n = []

for i in range(2, 10):
    while n % i == 0:
        n = int(n / i)
        list_n.append(i)
print(f"Cписок простых множителей числа {a}")
print(list_n)