import random

field = [' ']*9

def list_win(field):
       win = [[field[0], field[1], field[2]],
              [field[3], field[4], field[5]],
              [field[6], field[7], field[8]],
              [field[0], field[3], field[6]],
              [field[1], field[4], field[7]],
              [field[2], field[5], field[8]],
              [field[0], field[4], field[8]],
              [field[2], field[4], field[6]]]
       return win

def scheme (field):
     print("┌─────┬─────┬─────┐")
     print('| ', field[0], ' | ', field[1], ' | ', field[2], ' |')
     print("├─────┼─────┼─────┤")
     print('| ', field[3], ' | ', field[4], ' | ', field[5], ' |')
     print("├─────┼─────┼─────┤")
     print('| ', field[6], ' | ', field[7], ' | ', field[8], ' |')
     print("└─────┴─────┴─────┘")

def verif (gamers, value):
    stop = True
    while stop:
        x = int(input(f"{gamers}, Введите номер клетки: "))
        if x > 0 and x < 10:
            if field[x-1] == " ":
                field[x-1] = value
                stop = False
            else:
                print("Клетка  занята, переходите")
        else:
            print("Клетка  не существует, переходите")


gamers1 = input(" Игрок 1, введите свое имя: ")
gamers2 = input(" Игрок 2, введите свое имя: ")
fortuna1 = random.randint(1, 6)
print(f'{gamers1}, у Вас выпало {fortuna1}')
fortuna2 = random.randint(1, 6)
print(f'{gamers2}, у Вас выпало {fortuna2}')
if fortuna2 > fortuna1:
    first = gamers2
    second = gamers1
    print(f'{gamers2} Вы ходите первым')
else:
    first = gamers1
    second = gamers2
    print(f'{gamers1} Вы ходите первым')


print(" Чтобы поставить крестик, введи номер клетки согласно схемы:")
print("┌─────┬─────┬─────┐")
print("|  1  |  2  |  3  |")
print("├─────┼─────┼─────┤")
print("|  4  |  5  |  6  |")
print("├─────┼─────┼─────┤")
print("|  7  |  8  |  9  |")
print("└─────┴─────┴─────┘")

stop = '0'
step = 0
while stop == '0':
    verif(first,"X")
    win = list_win(field)
    scheme(field)
    step +=1
    if step == 9:
        print("Ничья! Победила дружба!")
        break
    for i in win:
        if i.count("X") == 3:
            print( f"{first}, Вы победили!")
            stop = "1"
    if  stop =="1":
        break
    else:

        verif(second,"1")
        win = list_win(field)
        scheme(field)
        step += 1
        if step == 9:
            print("Ничья! Победила дружба!")
            break
        print(step)
        for i in win:
            if i.count("1") == 3:
                print( f"{second}, Вы победили!")
                stop = "1"

