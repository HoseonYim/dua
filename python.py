# dataVisualization.py by localhost

import matplotlib.pyplot as plt
import numpy as np


class log():
    timestamp = [None]
    app = [None]
    category = [None]
    tag = [None]


def csvToArr(csvRdr):
    csvLog = log()

    next(csvRdr)

    for line in csvRdr:
        csvLog.timestamp.append(int(line[0]))
        csvLog.app.append(line[1])
        csvLog.category.append(line[2])
        csvLog.tag.append(line[3])

    return csvLog


def setPlt(app, time):
    for i in range(len(time) - 1, 0, -1):
        plt.bar('today', time[i], label=app[i])

    return plt.bar('today', time[0], bottom=time[1], label=app[0])


def usageRatio(appUsageLog):
    app = []
    time = []

    for i in range(len(appUsageLog.tag)):
        if appUsageLog.tag[i] == 'False':
            app.append(appUsageLog.app[i])
            time.append(
                appUsageLog.timestamp[i] - appUsageLog.timestamp[i - 1])

    setPlt(app, time)

    plt.title("Usage Ratio")
    plt.legend()

    plt.show()


def stepPlot(appUsageLog):  # 추가 작업 필요
    time = []

    plt.step(range(appUsageLog.time[0], appUsageLog.time[-1] + 1), )

    plt.legend()
    plt.show()


def main():
    csvRdr = csvLoad('sample.csv')

    appUsageLog = log()

    appUsageLog = csvToArr(csvRdr)

    usageRatio(appUsageLog)  # visualization
    stepPlot(appUsageLog)


main()
