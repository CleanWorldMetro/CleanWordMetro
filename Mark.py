import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='clean_world',
    user='mark',
    password='metropolia')


def question(question_id):
    sql = "SELECT id, text FROM quiz_question WHERE id =" + str(question_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f'Question is: {row[1]}')


def quiz_question_option(question_id):
    #1 get random id

    # get question based on that id

    # show answer with that id

    #let user choose option
    question_id = int(input('question id: '))
    # evaluate answer
    sql = "select id, text from quiz_question_option where quiz_question_id = " + str(question_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount > 0:
        for index, row in enumerate(result, start=1):
            print(f"{index}) {row[1]}")

        return


question_id = int(input('question id: '))
question(question_id)
quiz_question_option(question_id)


