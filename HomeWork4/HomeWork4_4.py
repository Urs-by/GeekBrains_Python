# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 5x^2 + 3x 3x^2 + x + 8 8x^2 + 4x + 8

def readstroke(file, spl):
    with open(file, encoding="utf-8") as name:
        data = name.readline().split(spl)
        return data

print(f"Первый многочлен: {readstroke('multi1.txt',' ')}")
print(f"Второй многочлен : {readstroke('multi2.txt',' ')}")
# сплитуем каждый многочлен чтобы отделить x^2
str1 = readstroke('multi1.txt','x^2')
str2 = readstroke('multi2.txt','x^2')

# если коэфициенты отсутствуют - добавляем 1
if str2[0]=='-':
    str2[0]=-1
if str1[0]=='-':
    str1[0]=-1

# запоминаем первый коэфициент
k1 = int(str1[0])+int(str2[0])
if k1 == 1:
    k1 = ''
if k1 == -1:
    k1 = '-'

# сплитуем второй элемент списка str1 и str2 чтобы отделить x
str11 = str1[1].split('x')
str22 = str2[1].split('x')

# если коэфициенты отсутствуют - добавляем 1
if str11[0]=='-' or str11[0] =='+':
    str11[0]=str11[0]+str(1)
if str22[0]=='-' or str22[0] =='+':
    str22[0]=str22[0]+str(1)

# запоминаем второй коэфициент
k2 = int(str11[0])+int(str22[0])
if k2 > 1:
    k2 = '+' + str(k2)
if k2 == 1:
    k2 = '+'
if k2 ==-1:
    k2 = '-'
# проверка на 3й элемент многочлена
if str11[1] == '':
    str11[1] = 0
if str22[1] == '':
    str22[1] = 0

# запоминаем третий  коэфициент
k3 = int(str11[1]) + int(str22[1])
if k3 > 0:
    k3 = '+' + str(k3)
if k3 == 1:
    k3 = ''

# собираем итоговый многочлен
if k1 == 0 and k2 == 0:
    res = str(k3)
elif k2 == 0:
    res = str(k1) + 'x^2' + str(k3)
elif k1 == 0:
    res = str(k2) + 'x' + str(k3)
else:
    res = str(k1) + 'x^2' +str(k2)+'x'+ str(k3)

print(f"Cумма многочленов равна: {res}")

with open("result.txt", "w", encoding="utf-8") as name:
    data = name.write(res)