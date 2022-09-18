from enum import IntEnum
from tempfile import tempdir
import math


class Type(IntEnum):
    internet = 0,
    game = 1,
    chatting = 2


class Time:
    def __init__(self, day: str, hour: int, minute: int):
        self.day = day
        self.hour = hour
        self.minute = minute


class DuringTime:
    def __init__(self, startTime: Time, endTime: Time):
        self.startTime = startTime
        self.endTime = endTime


class UserData:
    def __init__(self, type: Type, time: DuringTime):
        self.type = type
        self.time = time


class User:
    # dataList Array<UserData>
    def __init__(self, dataList: list, workingTime: DuringTime, id: int):
        self.dataList = dataList
        self.workingTime = workingTime
        self.id = id


def isLast(time1: Time, time2: Time):
    if (time1.hour > time2.hour):
        return True

    if (time1.hour == time2.hour):
        if (time1.minute > time2.minute):
            return True

        return False

    return False


def calcTime(time: DuringTime):

    time1 = time.startTime
    time2 = time.endTime

    if (not isLast(time1, time2)):
        temp = time1
        time1 = time2
        time2 = temp

    time1Min = time1.hour*60 + time1.minute
    time2Min = time2.hour*60 + time2.minute

    realTime_min = time1Min-time2Min

    return Time("-", math.floor(realTime_min/60), realTime_min % 60)
