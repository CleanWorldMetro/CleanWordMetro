from config import connection
import utils.player as playerUtil
import utils.robot as robotUtil
import utils.country as countryUtil
import utils.sql as sqlUtil

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
        isClean = 1
    else:  #future implement, can change isClean back to 0
        isClean = 0
    return  isClean

def changeIsBossDefeatInCity(isBossDefeat,city):
    bossStatus = city [4]
    if isBossDefeat:
        bossDefeat = 1
    else:
        bossDefeat = 0
    return bossDefeat

def cleanCity(city):
    return


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


player = playerUtil.getPlayerByName("Trung")
boss = robotUtil.getCurrentBossData(player)
# print(boss)
city = getCurrentCityData(player)
# city = "Vantaa"
currentCountry = countryUtil.getCurrentCountryData(player)
cityListData = getCityListInOneCountry(currentCountry)
formatedCityList = formatCityList(cityListData)
print(formatedCityList)
print(isLastCity(city,formatedCityList))
# print("old city",city)
# # change = changeIsClean(city)
# # print(change)
# update = updateIsClean(city)
# city = getCurrentCityData(player)
# print("new city",city)
# print(isCleanCity(player,boss))
# print(city)