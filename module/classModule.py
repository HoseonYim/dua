class log():
    timestamp = [None]
    app = [None]
    category = [None]
    tag = [None]

class Type(enum.IntEnum):
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