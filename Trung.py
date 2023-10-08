from config import connection


# connection = mysql.connector.connect(
#     host = "127.0.0.1",
#     port = 3300,
#     database = "clean_world",
#     user = "root",
#     password = "",
#     autocommit = True
)
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
        finalSql = sql + "where id =" +id + "'"
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

# getTables()
# player_info = []
# getPlayers()
# getPlayerByID(1)
# getRobots()
# getMatches()
# getQuestions()
getOptionForQuestions(1)