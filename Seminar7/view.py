def printMainMenu():
    print('Выберите пункт меню: ')
    print("1 - сколько дней прошло с начала года\n "
          "2 - сколько дней осталось до Нового Года")


def printResult(title, time):
    print(f'{title} {time} дня')

def getValue():
    user = int(input("Ваш выбор: "))
    return user

def err():
    print("Введено некорректное значение")