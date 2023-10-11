from config import connection

# def updating():
#     locationId = 1
#     playerId = 1
#     # sql="update player"
#     # sql=sql + " set location="+str(location_id)+""
#     # sql=sql + " where id="+str(player[0])+""
#     sql = f"UPDATE player set location = {locationId} where id = {playerId}"
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     if cursor.rowcount>0:
#         return result
#
# updating()
location_id = 1
sql = "SELECT robot.name, robot.type, robot.pollustat,robot.location FROM robot,robottype"
final = (f"{sql} WHERE robot.type = robottype.id and"
         f" location= {location_id} and robottype.name ='boss'")
print(final)


# player_name="Huy"
# updating(player_name)

# player=getcurrentplayerdata(player_name)
# boss=getBossdata()
# isWinboss(player,boss)



# name = "Trung1"
# nameData = [name, 1, 1, 1, 3, 1]
#
#
#
# nameDataToTuple = tuple(nameData)
# playerComlumn = "name, resStat, location, isInCity, energy, isNew"
# sql = f"INSERT INTO player({playerComlumn}) VALUE {nameDataToTuple}"
#
# print(sql)

