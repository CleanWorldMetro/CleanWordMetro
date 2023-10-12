from config import connection
import utils.player as playerUtil
import utils.robot as robotUtil

def getCurrentCityData(player):
    playeriD = player[0]
    sql = "Select city.id, city.name, city.country, isClean from city, player"
    finalSql = f"{sql} Where city.id = player.location and player.id = {playeriD}"
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    # finalSql = sql + "where name = '" +name + "'"
    return result[0]

def isCleanCity(player,boss):
    #edit logic so that player Stat go to boss Stat + 1
    # isClean = city[3] # return stat of isClean
    # playerStat= player[2]
    # bossStat = boss[3]
    win = robotUtil.isWinAgainstBossRobot(player,boss)
    if win:
        return True
    # print("You have defeate the guardian",win)
    ## insert match
    else:
        return False

def changeIsClean(city):
    isClean = city[3]
    print(isClean)
    if isClean == 0:
        isClean = 1
    else:  #future implement, can change isClean back to 0
        isClean = 0
    return  isClean

def updateIsClean (city):
    currentCityId = city[0]
    updateIsClean = changeIsClean(city)
    print(updateIsClean)
    sql = "update city"
    moreSql = f"{sql} SET isClean = {updateIsClean}"
    finalSql =f"{moreSql} Where id = {currentCityId}"
    # print(finalSql)
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    print("Your stat have been updated")

    return result

# player = playerUtil.getPlayerByName("Trung")
# boss = robotUtil.getCurrentBossData(player)
# print(boss)
# city = getCurrentCityData(player)
# print("old city",city)
# # change = changeIsClean(city)
# # print(change)
# update = updateIsClean(city)
# city = getCurrentCityData(player)
# print("new city",city)
# print(isCleanCity(player,boss))
# print(city)