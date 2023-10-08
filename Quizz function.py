import mysql.connector
connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'clean_world',
    user= 'dbuser',
    password= 'pass_word',
    autocommit=True)

def quiz_question():
    sql = "select * from quiz_question;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[1]}")
        return
quiz_question()
def quiz_question_option(questionId):
    #1 get random id

    # get question based on that id

    # show answer with that id

    #let user choose option

    # evaluate answer
    sql="select * from quiz_question_option where quiz_questionid;"
    moreSql = "where quiz_question_id =" +questionId
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount > 0:
        for index,row in enumerate(result,start=1) :
            print(index,")",f"{row[1]}")
        player = int(input("what is the answer of this question (choose the number): "))
    answer = result[player-1]
    print(answer)
    isCorrect = answer[3]
    print(type(isCorrect))
    if isCorrect == 1:
        print(" your answer is correct")
    else:
        print("your answer is not correct")
    # if player==row[0]:
    #     print("correct")
    # else:
    #     print("incorrect")
        return
quiz_question_option()


