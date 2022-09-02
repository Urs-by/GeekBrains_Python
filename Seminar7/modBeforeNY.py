import datetime

def beforeNY():
    timeNow = datetime.datetime.now()
    timeNY = datetime.datetime(timeNow.year+1, 1, 1)
    return (timeNY-timeNow).days
