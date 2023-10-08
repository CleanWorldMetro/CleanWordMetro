from config import connection


# connection = mysql.connector.connect(
#     host = "127.0.0.1",
#     port = 3300,
#     database = "clean_world",
#     user = "root",
#     password = "",
#     autocommit = True

def getTables():
    sql = "SHOW tables"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("this is",result)
    # result =runSQL(sql)
    for table in result:
        print(table)

def getPlayers():
    sql = "SELECT * from player"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("this is",result)
    # result =runSQL(sql)
    for table in result:
        print(table)

def getPlayerByID(id):
        sql = "SELECT * from player "
        finalSql = sql + "where id =" +str(id)
        cursor = connection.cursor()
        cursor.execute(finalSql)
        result = cursor.fetchall()
        print("this is", result)
        # result =runSQL(sql)
        for player in result:
            print(player)

def getRobots():
    sql = "SELECT * from robot"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("this is",result)
    # result =runSQL(sql)
    for table in result:
        print(table)

player_info = []
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

# getTables()
# player_info = []
# getPlayers()
# getPlayerByID(1)
# getRobots()
# getMatches()
# getQuestions()
# getOptionForQuestions(1)
chooseOptionInCity(inCityGui())
