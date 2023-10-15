from config import connection
# import utils.player as playerUtil
# import utils.robot as robotUtil
# import utils.country as countryUtil
# import utils.sql as sqlUtil

def getCurrentCityData(player):
    playeriD = player[0]
    sql = "Select city.id, city.name, city.country, isClean from city, player"
    finalSql = f"{sql} Where city.id = player.location and player.id = {playeriD}"
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    # finalSql = sql + "where name = '" +name + "'"
    return result[0]



def getCityListInOneCountry(country):
    currentCountryId = country[0]
    selectedColumns = "city.name"
    sql = "Select city.name from city,country"
    finalSql = f"{sql} WHERE city.country = country.id"
    print(finalSql)
    result = sqlUtil.executeSql(finalSql)
    return result



def changeIsClean(city):
    isClean = city[3]
    print(isClean)
    if isClean == 0:
        print("change from 0 to 1")
        isClean = 1
    else:  #future implement, can change isClean back to 0
        print("change from 1 to 0")
        isClean = 0
    return  isClean

def changeIsBossDefeatInCity(isBossDefeat,city):
    bossStatus = city [3] ## boss status
    print(bossStatus)
    if isBossDefeat:
        bossStatus = 1
    else:
        bossStatus = 0
    return bossStatus




def updateIsClean (city,newIsClean):
    currentCityId = city[0]
    # updateIsClean = changeIsClean(city)
    # print(updateIsClean)
    sql = "update city"
    moreSql = f"{sql} SET isClean = {newIsClean}"
    finalSql =f"{moreSql} Where id = {currentCityId}"
    # print(finalSql)
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    print("Your stat have been updated")

    return result

def updateBossStatus(city,newBossStatus):
    currentCityId = city[0]
    # updateIsClean = changeIsClean(city)
    # print(updateIsClean)
    sql = "update city"
    moreSql = f"{sql} SET isBossDefeat = {newBossStatus}"
    finalSql =f"{moreSql} Where id = {currentCityId}"
    # print(finalSql)
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    print("Your stat have been updated")

    return

def isLastCity(currentCity, cityList):
    currentCityName = currentCity[1]
    if currentCityName == cityList[len(cityList)-1]:
        return True
    else:
        return False

def formatCityList(cityListData):
    formattedList = []
    for city in cityListData:
        formattedList.append(city[0])
    return  tuple(formattedList) # return a tuple of citylist

def cleanCity(city):
    newIsClean = changeIsClean(city)
    updateIsClean(city,newIsClean) # update is Clean
    # newBossStatus = changeIsBossDefeatInCity(resultFightBoss,city)
    # updateBossStatus(city,newBossStatus) # update boss status
    result = newIsClean

    return result

def moveToNewCity(city,resultOfCleanCity):
    return

## move the import here to prevent circulate import
import utils.player as playerUtil
import utils.robot as robotUtil
import utils.country as countryUtil
import utils.sql as sqlUtil

# player = playerUtil.getPlayerByName("Trung")
# boss = robotUtil.getCurrentBossData(player)
# # print(boss)
# city = getCurrentCityData(player)
# # # city = "Vantaa"
# # currentCountry = countryUtil.getCurrentCountryData(player)
# # cityListData = getCityListInOneCountry(currentCountry)
# # formatedCityList = formatCityList(cityListData)
# # print(formatedCityList)
# # print(isLastCity(city,formatedCityList))
# # print(changeIsClean(city))
# newIsClean = changeIsClean(city)
# # print("old city",city)
# # # change = changeIsClean(city)
# # # print(change)
# update = updateIsClean(city,newIsClean)
# city = getCurrentCityData(player)
# print("new city",city)
# print(isCleanCity(player,boss))
# print(city)