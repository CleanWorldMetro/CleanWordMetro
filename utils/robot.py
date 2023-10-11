from config import connection

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

# get_current_boss_data(1)

