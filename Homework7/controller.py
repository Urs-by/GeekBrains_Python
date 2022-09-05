import view
import modelTxtFile
import modelNewEntry
import modelSearchName

value = None

def callMainMenu():
    view.printMainMenu()

def initValue():
    global value
    value = view.getValue()
    return value

def callPrintAll():
    data = modelTxtFile.readAll()
    view.printAll(data)

def callNewEntry():
    data = modelNewEntry.addNewRecord()
    modelTxtFile.addNewEntry(data)

def callPrintNAme():
    data = modelTxtFile.readAll()
    name = modelSearchName.inputName()
    result = modelSearchName.searchName(data, name)
    view.printName(result)



def callButton():
    global value
    if value == 1:
        callPrintAll()
    elif value == 2:
        callNewEntry()
    elif value == 3:
        callPrintNAme()

