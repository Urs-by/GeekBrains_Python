import view

def addNewRecord():
    namingList = ["Имя", "Фамилию", "Компанию", "Телефон", "Домашний телефон"]
    newEntry = []
    for i in namingList:
        data = view.getNewEntry(i)
        newEntry.append(data+" ")
    newEntry.append('\n')
    return newEntry






