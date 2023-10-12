from config import connection
import utils.player as playerUtil
import random


def getCurrentBossData(player):
    locationId = player[3]
    # sql = "SELECT name, type, pollustat,location FROM robot where id=" + str(bot_id)
    selectFields = "robot.id,robot.name,robot.type,robot.pollustat,robot.location,robottype.description"
    sql = f"SELECT {selectFields} FROM robot,robottype"
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
    selectFields = "robot.id, robot.name, robot.type, robot.pollustat, robot.location, robottype.description"
    sql = f"SELECT {selectFields} FROM robot,robottype"
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
        robotStat = robot[3]
        if robotStat >= playerStat:
            filteredList.append(robot)
    # print(filteredList)

    return filteredList

def getRandomRobot(robotList):
    randomRobot = random.choice(robotList)
    # print(randomRobot)
    return randomRobot

def getRobotType(robot):
    robotType = robot[2]
    return robotType

def isNormalRobot(robotType):
    if robotType == 1:
        return True
def isBossRobot(robotType):
    if robotType == 2:
        return True

def isWinAgainstNormalRobot(player,robot):
    playerStat = player[2]
    robotStat = robot[4]
    if playerStat+1 >= robotStat:
        return True
    else:
        return False

def isWinAgainstBossRobot(player,boss):
    playerStat = player[2]
    bossStat = boss[4]
    if playerStat == bossStat:
        return True
    else:
        return False

# def MatchI
# def insertMatch(matchInfo):


def isWin(player,robot):

    robotType = getRobotType(robot)
    if isNormalRobot(robotType):
        print("You have meet a normal robot")
        isWinResult = isWinAgainstNormalRobot(player,robot)
    elif isBossRobot(robotType):
        print("Oh No! you meet the city guardian")
        isWinResult = isWinAgainstBossRobot(player,robot)
    return isWinResult ## if player win against normal robot or boss robot

def getIsWinId(isWin):
    if isWin:
        return 1
    else:
        return 0

def insertMatchData(matchData):
    matchDataTuple = tuple(matchData)
    matchColumns = "player_id, robot_id, isWin"
    sql = f"INSERT INTO match_game ({matchColumns}) Value {matchDataTuple}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Match data inserted successfully")
    return result #result user answer as a

def showRobotInfo(robot):
    robotName = robot[1]
    robotStat = robot[3]
    robotDescription = robot[4]
    robotInfo = (f"robot: {robotName } -- Stat: {robotStat}  "
                 f"-- Description: {robotDescription}")
    print(robotInfo)
    return




def match(player,robot,boss):
    playerUtil.showPlayerInfo(player)
    showRobotInfo(robot)
    playerStat = player[2]
    bossStat = boss[3]
    isBoss = isBossRobot(robot)
    playerDefaultStat = 1
    # robotStat = robot[3]
    # robotType = getRobotType(robot)
    win = isWin(player,robot)

    if win:
        if isBoss:
            print("Boss walks away")
        else:
            print("Congrat! You have win")
        playerStat += 1
        playerStat = min(playerStat,bossStat)

    else:
        print("Poor you! You have loses")
        playerStat -= 1
        playerStat = max(playerStat,playerDefaultStat)
    return  [playerStat,win]


def isDefeatBoss(player, boss):  # have we defeat boss
    winBoss = isWinAgainstBossRobot(player, boss)
    if winBoss:
        return True
    else:
        return False


## return newplayer Stat when defeat boss
def defeatBoss(player, boss):
    playerStat = player[3]
    if isDefeatBoss(player, boss):  ##defeat robot
        playerStat += 1
    return playerStat


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

def fightBoss(player,boss):
    boss = getCurrentBossData(player)
    # isCleanCity(player,boss)
def fight(player,boss):

    player_name = player[1]
    robotList = getRobotsByLocation(player)  # get robot List at a location
    # boss = get_current_boss_data(player)  # get boss at a location
    # print("This is boss data",boss)
    filteredList = filterRobotList(player, robotList)  # filter robot list based on player stat
    # print("This is a new robot list based on player",filterRobotList(player,robotList))

    randomRobot = getRandomRobot(filteredList)  # get random robot from filtered list
    # print("This is random robot", getRandomRobot(filteredList))
    print("Wait here")
    # newPlayerStat = match(player, randomRobot, boss)
    result = match(player, randomRobot, boss)
    newStat = result[0]
    isWin = result[1]
    isWinId = getIsWinId(isWin)
    playerId = player[0]
    robotId = randomRobot[0]
    # print(playerId)
    # print(robotId)
    # print(isWinId)
    matchData = [playerId,robotId,isWinId]
    # print(matchData)
    # matchDataTuple = playerUtil.playerToTuple(matchData)
    insertMatchData(matchData)

    # print("This is match with robot), ",newPlayerStat)
    playerUtil.updateStat(player, newStat)

    newPlayerData = playerUtil.getPlayerByName(player_name)
    # print("This is new player data",newPlayerData)
    # return newPlayerData
    return

#player meet robot
# print("THis is robot List", robotList)
# player_name = "Trung"
# player = playerUtil.getPlayerByName(player_name)
# boss = getCurrentBossData(player)
# # robots = getRobotsByLocation(player)
# # print(robots)
# # print(boss)
# # bossInfo = showRobotInfo(boss)
# # # updatePlayerData = fight(player,boss)
# fight(player,boss)
# fightBoss(player,boss)