import config.connection as connection
import random



def quiz_question_option(question_id):
    #1 get random id

    # get question based on that id

    # show answer with that id

    #let user choose option

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

question_id = int(input('id: '))
quiz_question_option(question_id)
