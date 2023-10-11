# import utils.quiz as quiz
from config import connection

import utils.player as playerUtil
import utils.quiz as quizUtil
import utils.robot as robotUtil


def inCityGui():
    print("What do you want to do \n"
          "1. go meet the boss \n"
          "2. Go farm\n"
          "3. Go play quiz\n"
          "4. Do nothing\n")
    option = input("What do you want to do? (1-4) ")
    return int(option)
def chooseOptionInCity(number,player,boss):
    if number == 1:
        print("meet boss")
    if number == 2:
        print("go farm")
    if number == 3:
        print("let's find some treasure")
        quizUtil.quiz(player,boss)
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

def introducton(name):
    print(f"Background:\nOur world CLEAN WORLD has been deserted and polluted one since the great war between Humans and Robots."
          f"\nLuckily there are still some remaining clean cities.Our hero {name} is currently living at Helsinki ,"
          f"\nOn one sunny day, when our hero was going picnic with his mother, a robot was nearby and it attacked them.\n"
          f"Luckily, one of the city’s guard is nearby and he was able to save them."
          f"\nHowever, due to an overexposure with the polluted energy from the robot, our hero’s mother was not able to survive."
          f"\nIn order to revenge his mother, he decided to destroy all the robots in the world."
          f"\nThe elder told him that the sauce of all the robot is from the factory in a city beyond the hill."
          f"\nTherefore, he decided to go to the next city to destroy the robots there")
def showIntroduction(player):
    name = player[1]
    if playerUtil.isNewPlayer(player):
        introducton(name)
        playerUtil.updateIsNew(player)
def game(player):
    while True:
        playerId = player[0]
        boss = robotUtil.get_current_boss_data(player)
        updatedPlayer =playerUtil.getPlayerByID(playerId)
        print("This is updated Player Data", updatedPlayer)
        showIntroduction(updatedPlayer)

        playerOption = inCityGui()
        chooseOptionInCity(playerOption,updatedPlayer,boss)

    # return playerOption



# player = playerUtil.getPlayerByName("Trung")
# formatedData = playerUtil.formatPlayerData(player)
# game(player)
