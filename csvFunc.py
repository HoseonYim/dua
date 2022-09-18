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