import matplotlib.pyplot as plt
import dataSet
import mainClass


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


makeGraph(0)
