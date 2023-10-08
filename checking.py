import mysql.connector
import random

connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'clean_world',
    user= 'mark',
    password= 'metropolia',
    autocommit=True)


def chechking(question_id):
    sql = "select id, text from quiz_question_option where quiz_question_id = " + str(question_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount > 0:
        for index, row in enumerate(result, start=1):
            print(f"{index}) {row[1]}")
        player = int(input("what is the answer of this question (choose the number): "))
    answer = result[player - 1]
    print(answer)
    is_correct = answer[3]
    print(type(is_correct))
    if is_correct == 1:
        print(" your answer is correct")
    else:
        print("your answer is not correct")
        # if player==row[0]:
        #     print("correct")
        # else:
        #     print("incorrect")
        return


id_no = int(input('no: '))
chechking(id_no)