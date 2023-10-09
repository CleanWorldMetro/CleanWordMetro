import random

from config import connection


# connection = mysql.connector.connect(
#     host = "127.0.0.1",
#     port = 3300,
#     database = "clean_world",
#     user = "root",
#     password = "",
#     autocommit = True
player = []
boss = []
city = ""
def getTables():
    sql = "SHOW tables"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print("this is",result)
    # result =runSQL(sql)
    for table in result:
        print(table)

# getCurrentCity():
# sql= "Select city.name from player, city"
# finalSql = f"WHERE player."

def getPlayers():
    sql = "SELECT * from player"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print("this is",result)
    # result =runSQL(sql)
    return result

def getPlayerByID(id):
        sql = "SELECT * from player "
        finalSql = sql + "where id =" +str(id)
        cursor = connection.cursor()
        cursor.execute(finalSql)
        result = cursor.fetchall()
        # print("this is", result)
        # result =runSQL(sql)
        # for player in result:
        #     print(player)
        return result[0]

def loadingPlayerByID(playerId):
    playerTuple = getPlayerByID(playerId)
    # print(playerTuple)
    currentPlayer = []
    for value in playerTuple:
        currentPlayer.append(value)
    # print(currentPlayer)
    return currentPlayer

def getPlayerByName(name):
    sql = "Select * from player "
    finalSql = sql + "where name = '" +name + "'"
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()

    return result
def getRobotsInCity(city):
    sql = "SELECT robot.id, robot.name, robot.type, robot.pollustat from robot,city"
    moreSql =f"{sql} WHERE robot.location = city.id"
    finalSql =f"{moreSql} AND city.name = '{city}'"
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    print("this is",result)
    # result =runSQL(sql)
    return result

def getRobotById(robotId):
    sql = "SELECT * FROM robot "
    resultSql = f"{sql} WHERE id ={robotId}"
    cursor = connection.cursor()
    cursor.execute(resultSql)
    result = cursor.fetchall()
    print("this is one robot", result)
    return result

# def getBoss():
#     getRobotById()

# player_info = []
def getMatches():
    sql = "SELECT * from match_game"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("this is",result)
    # result =runSQL(sql)
    for match in result:
        print(match)

def getQuestions():
    sql = "SELECT * from quiz_question"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("this is",result)
    # result =runSQL(sql)
    for question in result:
        print(question)


def getOptionForQuestions(id):
    sql = "SELECT * from quiz_question_option "
    finalsql = sql + "where quiz_question_id = " + str(id)
    cursor = connection.cursor()
    cursor.execute(finalsql)
    result = cursor.fetchall()
    print("this is", result)
    # result =runSQL(sql)
    for question in result:
        print(question)

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
    if number == 4:
        print("do nothing")

# update player
# set resStat = 2
# where id = 3;
# select * from player;
def updatePlayerStat(playerTuple):
    id = playerTuple[0]
    print(id)
    newStat = playerTuple[2]
    print(newStat)
    sql = " UPDATE player"
    finalsql = f"{sql} SET resStat = {newStat} where id = {id}"
    cursor = connection.cursor()
    cursor.execute(finalsql)
    result = cursor.fetchall()
    print("this is", result)

def playerToTuple(player):
    playerTuple = tuple(player)
    print(playerTuple)
    return playerTuple

def generateRandomRobotID():
    return random.randint(player[3],)

def goFarm():
    # generate random robot
    print(f"go farming: {player}")



# getTables()
# player_info = []
# getPlayers()
# print(getPlayerByName("Trung"))
# loadingPlayerByID(3)
# player =loadingPlayerByID(3)
# goFarm()

# print(f"old player${player}")
# player[2] = 5
# print(f"new player ${player}")
# newPlayerTuble = playerToTuple(player)
# # print(newPlayerTuble)
# # print(newPlayerTuble[0])
# updatePlayerStat(newPlayerTuble)
# getPlayerByID(3)
# getRobots()
# getRobotById(1)
# getMatches()
# getQuestions()
# getOptionForQuestions(1)
# chooseOptionInCity(inCityGui())
getRobotsInCity("Helsinki")