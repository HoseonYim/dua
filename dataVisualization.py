# Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
# /python.py python.py
import matplotlib.pyplot as plt
import numpy as np
import csv

def csvLoad(csvPath):
    csvFile = open(csvPath, 'r', encoding='utf-8')
    csvRdr = csv.reader(csvFile)

    return csvRdr

def csvToArr(csvRdr):
    logTimestamp = []
    logApp = []
    logCategory = []
    logTag = []

    next(csvRdr)

    for line in csvRdr:
        logTimestamp.append(int(line[0]))
        logApp.append(line[1])
        logCategory.append(line[2])
        logTag.append(line[3])

    return logTimestamp, logApp, logCategory, logTag

def setPlt(app, time):
    for i in range(len(time) - 1, 0, -1):
        plt.bar('today', time[i], label=app[i])

    return plt.bar('today', time[0], bottom=time[1], label=app[0])


def main():
    csvRdr = csvLoad('sample.csv')

    [logTimestamp, logApp, logCategory, logTag] = csvToArr(csvRdr)

    app = []
    time = []

    for i in range(len(logTimestamp)):
        if logTag[i] == 'False':
            app.append(logApp[i])
            time.append(logTimestamp[i] - logTimestamp[i - 1])
    
    setPlt(app, time)

    plt.legend()
    plt.show()

main()