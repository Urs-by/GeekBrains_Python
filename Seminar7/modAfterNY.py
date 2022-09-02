import datetime

def afterNY():
    timeNow = datetime.datetime.now()
    timeNY = datetime.datetime(timeNow.year, 1, 1)
    return (timeNow - timeNY).days
