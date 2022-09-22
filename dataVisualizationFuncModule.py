from enum import IntEnum
import math
import csv
import classModule

def csvLoad(csvPath):
    csvFile = open(csvPath, 'r', encoding='utf-8')
    csvRdr = csv.reader(csvFile)

    return csvRdr

def csvToArr(csvRdr):
    csvLog = classModule.log()

    next(csvRdr)

    for line in csvRdr:
        csvLog.timestamp.append(int(line[0]))
        csvLog.app.append(line[1])
        csvLog.category.append(line[2])
        csvLog.tag.append(line[3])

    return csvLog

def isLast(time1: classModule.Time, time2: classModule.Time):
    if (time1.hour > time2.hour):
        return True

    if (time1.hour == time2.hour):
        if (time1.minute > time2.minute):
            return True

        return False

    return False


def calcTime(time: classModule.DuringTime):

    time1 = time.startTime
    time2 = time.endTime

    if (not isLast(time1, time2)):
        temp = time1
        time1 = time2
        time2 = temp

    time1Min = time1.hour*60 + time1.minute
    time2Min = time2.hour*60 + time2.minute

    realTime_min = time1Min-time2Min

    return classModule.Time("-", math.floor(realTime_min/60), realTime_min % 60)