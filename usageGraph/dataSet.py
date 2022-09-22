# 임시 데이터 저장 파일
import mainClass

# data setting
datas = [
    mainClass.User([
        mainClass.UserData(mainClass.Type.internet, mainClass.DuringTime(
            mainClass.Time("2022/9/18", 9, 0), mainClass.Time("-", 13, 0))),
        mainClass.UserData(mainClass.Type.game, mainClass.DuringTime(
            mainClass.Time("2022/9/18", 13, 30), mainClass.Time("-", 14, 0))),
        mainClass.UserData(mainClass.Type.internet, mainClass.DuringTime(
            mainClass.Time("2022/9/18", 15, 0), mainClass.Time("-", 22, 30))),
        mainClass.UserData(mainClass.Type.internet, mainClass.DuringTime(
            mainClass.Time("2022/9/19", 15, 0), mainClass.Time("-", 12, 43))),
        mainClass.UserData(mainClass.Type.game, mainClass.DuringTime(
            mainClass.Time("2022/9/19", 15, 0), mainClass.Time("-", 23, 20))),
        mainClass.UserData(mainClass.Type.chatting, mainClass.DuringTime(
            mainClass.Time("2022/9/19", 15, 0), mainClass.Time("-", 15, 57))),
    ],

        mainClass.DuringTime(
        mainClass.Time("-", 9, 0),
        mainClass.Time("-", 17, 0)
    ),
        0)
]
