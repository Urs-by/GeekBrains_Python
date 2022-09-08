# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода.
# Выведите его даты.

import random
# метод заполнения двумерного массива
def fillMatrix(calendar_list):
    matrix =[0]*len(calendar_list)
    for i in range(len(calendar_list)):
        matrix[i] = list(random.randint(15, 35) for i in range(calendar_list[i]))
    return matrix

calendar_list = [31, 30, 31, 31, 30]
ter_list = fillMatrix(calendar_list)
print("Данные температур с мая по сентябрь:")
for i in ter_list:
    print(i)
# перевод данных в одну строку
str_temper = ''
for i in ter_list:
    for j in i:
        str_temper = str_temper+str(j) + " "
str_temper = str_temper.split(' ')
str_temper = list(str_temper[:-1])

print("Семидневные промежутки:")
week_list = []
number_week = 1
for i in range(0, len(str_temper), 7):
    week = str_temper[i:i+7]
    print(f"{number_week}-я неделя {week}")
    week = map(int, week)
    mean = round(sum(week)/7, 2)
    week_list.append(mean)
    number_week += 1
print("Список с средней температурой за семидневный промежуток")
print(week_list)
print(f"Самый холодный {week_list.index(min(week_list))+1}-й семидневный промежуток ")
print(f"со средней температурой {min(week_list)} градусов")
print(f"Самый жаркий {week_list.index(max(week_list))+1}-й семидневный промежуток ")
print(f"о средней температурой {max(week_list)} градусов")





