import modAfterNY
import modBeforeNY
import view

value = None

def collMainMenu():
    view.printMainMenu()

def collAfterNY():
    days = modAfterNY.afterNY()
    view.printResult( "После нового года прошло", days)

def collBeforeNY():
    days = modBeforeNY.beforeNY()
    view.printResult("До Нового года осталось", days)

def initValue():
    global value
    value = view.getValue()

def collButton():
    global value
    if value == 1:
        collAfterNY()
    elif value == 2:
        collAfterNY()
    else:
        view.err()

