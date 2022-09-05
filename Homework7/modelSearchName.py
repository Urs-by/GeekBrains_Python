import view
import modelTxtFile

def inputName():
    data = view.searchName()
    return data

def searchName(catalog, name):
    result = []
    for i in range(len(catalog)):
        if name in catalog[i]:
            result.append(catalog[i])
    return result


# catalog = modelTxtFile.readAll()
# name = inputName()




