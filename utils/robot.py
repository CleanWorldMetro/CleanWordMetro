from config import connection
import utils.player as playerUtil
import random


def get_current_boss_data(player):
    locationId = player[3]
    # sql = "SELECT name, type, pollustat,location FROM robot where id=" + str(bot_id)

    sql = "SELECT robot.name, robot.type, robot.pollustat,robot.location FROM robot,robottype"
    final = (f"{sql} WHERE robot.type = robottype.id and"
             f" location= {locationId} and robottype.name ='boss'")
    cursor = connection.cursor()
    cursor.execute(final)
    result = cursor.fetchall()
    # print(result)
    # for row in result:
    #     print(f'Name: {row[0]}\nType: {row[1]}\nPollution Stats: {row[2]}\nLocation: {row[3]}')
    return result[0]

def getRobotsByLocation(player):
    locationId = player[3]
    sql = "SELECT robot.name, robot.type, robot.pollustat,robot.location FROM robot,robottype"
    final = (f"{sql} WHERE robot.type = robottype.id and"
             f" location= {locationId} ")
    cursor = connection.cursor()
    cursor.execute(final)
    result = cursor.fetchall()
    # print(result)
    return result

def filterRobotList(player,robotList):
    playerStat = player[2]
    filteredList = []
    for robot in robotList:
        robotStat = robot[2]
        if robotStat >= playerStat:
            filteredList.append(robot)
    # print(filteredList)

    return filteredList

def getRandomRobot(robotList):
    randomRobot = random.choice(robotList)
    print(randomRobot)
    return randomRobot

def getRobotType(robot):
    robotType = robot[1]
    return robotType

def isNormalRobot(robotType):
    if robotType == 1:
        return True
def isBossRobot(robotType):
    if robotType == 2:
        return True

def isWinAgainstNormalRobot(playerStat,robotStat):
    if playerStat+1 >= robotStat:
        return True

def isWinAgainstBossRobot(playerStat,robotStat):
    if playerStat == robotStat:
        return True

# def MatchI
# def insertMatch(matchInfo):


def isWin(player,robot):
    playerStat = player[2]
    robotStat = robot[2]
    robotType = getRobotType(robot)
    if isNormalRobot(robotType):
        print("You have meet a normal robot")
        isWin = isWinAgainstNormalRobot(playerStat,robotStat)
    elif isBossRobot(robotType):
        print("Oh No! you meet the city guardian")
        isWin = isWinAgainstBossRobot(playerStat,robotStat)
    return isWin ## if player win against normal robot or boss robot


def match(player,robot,boss):
    playerStat = player[2]
    bossStat = boss[2]
    playerDefaultStat = 1
    # robotStat = robot[2]
    # robotType = getRobotType(robot)
    win = isWin(player,robot)
    if win:
        print("Congrat! You have win")
        playerStat += 1
        playerStat = min(playerStat,bossStat)
    else:
        print("Poor you! You have loses")
        playerStat -= 1
        playerStat = max(playerStat,playerDefaultStat)
    return  playerStat

def isCleanCity(player,boss):
    win = isWin(player,boss)
    print("You have defeate the guardian",win)


# get_current_boss_data(1)

# player_name="Huy"
# player=playerUtil.getPlayerByName(player_name)
# print(player)
# robotList = getRobotsByLocation(player) # get robot List at a location
# boss = get_current_boss_data(player) # get boss at a location
# filteredList = filterRobotList(player,robotList) # filter robot list based on player stat
# randomRobot = getRandomRobot(filteredList) # get random robot from filtered list
# newPlayerStat = match(player,randomRobot,boss)
# playerUtil.updateStat(player,newPlayerStat)

def fightWithBoss(player):
    boss = get_current_boss_data(player)
    isCleanCity(player,boss)
def fight(player,boss):
    # player_name = p
    # player = playerUtil.getPlayerByName(player_name)
    print(player)
    player_name = player[1]
    robotList = getRobotsByLocation(player)  # get robot List at a location
    # boss = get_current_boss_data(player)  # get boss at a location
    # print("This is boss data",boss)
    filteredList = filterRobotList(player, robotList)  # filter robot list based on player stat
    # print("This is a new robot list based on player",filterRobotList(player,robotList))

    randomRobot = getRandomRobot(filteredList)  # get random robot from filtered list
    # print("This is random robot", getRandomRobot(filteredList))
    newPlayerStat = match(player, randomRobot, boss)
    # print("This is match with robot), ",newPlayerStat)
    playerUtil.updateStat(player, newPlayerStat)

    newPlayerData = playerUtil.getPlayerByName(player_name)
    # print("This is new player data",newPlayerData)
    # return newPlayerData
    return

#player meet robot
# print("THis is robot List", robotList)
# player_name = "Trung"
# player = playerUtil.getPlayerByName(player_name)
# boss = get_current_boss_data(player)
# updatePlayerData = fight(player,boss)