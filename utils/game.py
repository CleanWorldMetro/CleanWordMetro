# import utils.quiz as quiz
from config import connection

def inCityGui():
    print("What do you want to do \n"
          "1. go meet the boss \n"
          "2. Go farm\n"
          "3. Go play quiz\n"
          "4. Do nothing\n")
    option = input("What do you want to do? (1-4) ")
    return int(option)
def chooseOptionInCity(number):
    if number == 1:
        print("meet boss")
    if number == 2:
        print("go farm")
    if number == 3:
        print("let's find some treasure")
        randomQuestion = quiz.newRandomQuestion
        print(randomQuestion)

    if number == 4:
        print("do nothing")

def getPlayers():
    sql = "SELECT * from player"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print("this is",result)
    # result =runSQL(sql)
    return result

def isExist(username,namesInDatabase ):
    if username in namesInDatabase:
        return True
    else:
        return False

def formatedNameList(nameListFromDatabase): # return onlyNameList
    onlyNameList = []
    for nameData in nameListFromDatabase:
        nameInData = nameData[1]
        # print(nameInData)
        onlyNameList.append(nameInData)
    # print(onlyNameList)
    return onlyNameList


def inputName():
    name = input("Type your username: ")
    return name