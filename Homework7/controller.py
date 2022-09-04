import view
import modelTxtFile
import modelNewEntry

value = None

def callMainMenu():
    view.printMainMenu()

def initValue():
    global value
    value = view.getValue()

def callPrintAll():
    data = modelTxtFile.readAll()
    view.printAll(data)

def callNewEntry():
    data = modelNewEntry.addNewRecord()
    modelTxtFile.addNewEntry(data)



def callButton():
    global value
    if value == 1:
        callPrintAll()
    elif value == 2:
        callNewEntry()