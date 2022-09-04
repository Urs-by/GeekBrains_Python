catalog = {"id":"", "Имя":"", "Фамилия":"", "Компания":"", "Телефон":"", "Домашний":""}

def printMainMenu():
    print('Выберите пункт меню: ')
    print("1 - вывод всего справочника;\n"
          "2 - новая запись;\n"
          "3 - поиск по имени;\n"
          "4 - экспорт справочника в формат html; \n"
          "5 - экспорт справочника в форматы xml ")

def getValue():
    user = int(input("Ваш выбор: "))
    return user

def getNewEntry(data):
    user = input(f"Введите {data}: ")
    return user

def printAll(data):
    for i in range(len(data)):
        print(data[i], end = '')

