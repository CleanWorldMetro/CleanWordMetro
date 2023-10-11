from config import connection

def insertNewPlayer (nameData):
    nameDataToTuple = tuple(nameData)
    playerComlumn = "name, resStat, location, isInCity, energy, isNew"
    sql = f"INSERT INTO player({playerComlumn}) VALUE {nameDataToTuple}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result #result user answer as a

def playerToTuple(player):
    playerTuple = tuple(player)
    # print(playerTuple)
    return playerTuple

def getPlayerByName(name):
    sql = "Select * from player "
    finalSql = sql + "where name = '" +name + "'"
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    return result[0]


def getPlayerByID(id):
    sql = "SELECT * from player "
    finalSql = sql + "where id =" + str(id)
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    print(result)
    # print("this is", result)
    # result =runSQL(sql)
    # for player in result:
    #     print(player)
    return result

# player =  (3, 'testPlayer', 5, 1, 1, 3, 0)

# format a player data from a tuple to a list
def formatPlayerData(player):
    formattedData = []
    for value in player:
        formattedData.append(value)
    return formattedData

def getCurrentPlayerLocationId(player):
    currentLocationId = player[3]
    return currentLocationId

def updateStat(player, newStat):
    currentPlayerId = player[0]
    sql = "update player"
    moreSql = sql + " SET resStat = " + str(newStat)
    finaSql = moreSql + " where id= "  + str(currentPlayerId) + ""
    cursor = connection.cursor()
    cursor.execute(finaSql)
    result = cursor.fetchall()
    return result

def setDefaultData(player):
    currentPlayerId = player[0]
    defaultIsNew = 1
    defaultResStat = 1
    sql = "update player"
    moreSql = f"{sql} SET resStat = {str(defaultResStat)}, isNew = {defaultIsNew}"
    finaSql = moreSql + " where id= "  + str(currentPlayerId) + ""
    cursor = connection.cursor()
    cursor.execute(finaSql)
    result = cursor.fetchall()
    return result


# def updating(player):
#     location_id = player[3]
#     sql = "update player"
#     moresql = sql + " set location=" + str(location_id) + ""
#     finaSql = moresql + " where id=" + str(player[0]) + ""
#     cursor = connection.cursor()
#     cursor.execute(finaSql)
#     result = cursor.fetchall()
#     if cursor.rowcount > 0:
#         return result

# playerName = "Huy"
# # player = getPlayerByName(playerName)
# print(player)
# print(getCurrentPlayerLocationId(player))
name = "Huy"
# player = getPlayerByName(name)
# player = (2, 'Huy', 2, 1, 0, 3, 0)
# updateStat(player,3)
# print(getPlayerByName("Huy"))
# print(player)