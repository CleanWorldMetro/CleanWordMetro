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
    print(playerTuple)
    return playerTuple

def getPlayerByName(name):
    sql = "Select * from player "
    finalSql = sql + "where name = '" +name + "'"
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    return result


def getPlayerByID(id):
    sql = "SELECT * from player "
    finalSql = sql + "where id =" + str(id)
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    # print("this is", result)
    # result =runSQL(sql)
    # for player in result:
    #     print(player)
    return result[0]

# player =  (3, 'testPlayer', 5, 1, 1, 3, 0)

# format a player data from a tuple to a list
def formatPlayerData(player):
    formattedData = []
    for value in player:
        formattedData.append(value)
    return formattedData
