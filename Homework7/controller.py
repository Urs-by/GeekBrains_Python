import view
import modelTxtFile
import modelNewEntry
import modelSearchName
import modelXmlExport
import  modelHtmlExport

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

def callXmlExport():
    with open('catalog.xml', 'w', encoding="utf-8") as page:
        page.write('')
    data = modelTxtFile.readAll()
    for i in data:
        newstr = i.split(' ')
        modelXmlExport.createXml(newstr)
    view.printExportXml()

def callHtmlExport():
    with open('catalog.html', 'w', encoding="utf-8") as page:
        page.write(modelHtmlExport.head)
    data = modelTxtFile.readAll()
    for i in data:
        newstr = i.split(' ')
        modelHtmlExport.createHTML(newstr)
    with open('catalog.html', 'a', encoding="utf-8") as page:
        page.write('\n</html>')
    view.printExportHtml()



def callButton():
    global value
    if value == 1:
        callPrintAll()
    elif value == 2:
        callNewEntry()
    elif value == 3:
        callPrintNAme()
    elif value == 4:
        callHtmlExport()
    elif value == 5:
        callXmlExport()
    else:
        view.printError()

