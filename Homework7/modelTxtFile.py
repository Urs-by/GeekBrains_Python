def readAll():
    with open("catalog.txt" , encoding="utf-8") as catalog:
        data = catalog.readlines()
        return data

def addNewEntry(data):
    with open("catalog.txt", 'a', encoding="utf-8") as catalog:
        catalog.writelines(data)

