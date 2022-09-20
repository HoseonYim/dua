# dataVisualization.py by localhost

import matplotlib.pyplot as plt
import numpy as np
from module import dataVisualizationFuncModule
#from module import classModule

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
            time.append(appUsageLog.timestamp[i] - appUsageLog.timestamp[i - 1])
    
    setPlt(app, time)

    plt.title("Usage Ratio")
    plt.legend()
    
    plt.show()

def stepPlot(appUsageLog):          #추가 작업 필요
    time = []      

    plt.step(range(appUsageLog.time[0], appUsageLog.time[-1] + 1), )        #보수 필요

    plt.legend()
    plt.show()

def makeGraph(id):

    # finding user
    selectedUser = None
    for index in range(len(dataSet.datas)):
        if (dataSet.datas[index].id == id):
            selectedUser = dataSet.datas[index]
            break

    # finding date

    # date
    xValue = []

    # data, total time of types
    yValue = []

    # analyzing data
    index = -1
    lastDay = "-"
    for data in selectedUser.dataList:
        if (lastDay != data.time.startTime.day):
            yValue.append([])
            for data1 in mainClass.Type:
                yValue[index+1].append(0)
            lastDay = data.time.startTime.day
            index += 1
            xValue.append(data.time.startTime.day)

        calcTime = mainClass.calcTime(data.time)
        type = (int)(data.type)
        yValue[index][type] += calcTime.hour * 60 + calcTime.minute

    # generate graph
    for data in mainClass.Type:
        thisData = []
        for index in range(len(yValue)):
            thisData.append(yValue[index][data])

        print(xValue, thisData)
        plt.plot(xValue, thisData, marker='o', label=f"{data.name}")

    # show
    plt.legend()
    plt.title('usage time', fontsize=20)
    plt.show()

def main():
    csvRdr = csvFunc.csvLoad('sample.csv')

    appUsageLog = classModule.log()

    appUsageLog = csvFunc.csvToArr(csvRdr)

    usageRatio(appUsageLog)
    makeGraph(0)
#   stepPlot(appUsageLog)

main()