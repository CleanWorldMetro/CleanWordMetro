from config import connection

# connection = mysql.connector.connect(
#     host= '127.0.0.1',
#     port= 3306,
#     database= 'clean_world',
#     user= 'mark',
#     password= 'metropolia',
#     autocommit=True)


def checking(question_id):
    sql = "select id, text from quiz_question_option where quiz_question_id = " + str(question_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #return a list of option with quiz_question_id = 1

    if cursor.rowcount > 0:
        for index, row in enumerate(result, start=1):
            print(f"{index}) {row[1]}")
        if question_id == 1:
            answer = 4
        elif question_id == 2:
            answer = 3
        elif question_id == 3:
            answer = 3
        elif question_id == 4:
            answer = 2
        elif question_id == 5:
            answer = 2
        elif question_id == 6:
            answer = 1
        elif question_id == 7:
            answer = 4
        elif question_id == 8:
            answer = 3
        elif question_id == 9:
            answer = 2
        elif question_id == 10:
            answer = 4
        player_answer = int(input('Enter your answer: '))
        # assign the id from user to fetch the
            print('your answer is correct')
            cursor.execute("SELECT MAX(id) FROM quiz_user_answer")
            max_id = cursor.fetchall()
            new_id = max_id[0][0] + 1
            userAnswer = [userid,quizid,userAnswerid,isCorrect]
            userAnswerTuple = tuple(userAnswer)
            print(f'')
            sql_update = f"INSERT INTO quiz_user_answer VALUES {userAnswerTuple}"

            data = (new_id, question_id, player_answer)
            cursor.execute(sql_update, data)

        else:
            print('your answer is incorrect')

id_no = int(input('no: '))
checking(id_no)


"""
while True:
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
        
"""