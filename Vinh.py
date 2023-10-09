import mysql.connector
import random
connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'clean_world',
    user= 'dbuser',
    password= 'pass_word',
    autocommit=True)

def quiz_question(location_id):
    sql = "select quiz_question.text from city,quiz_question"
    sql = sql + " where quiz_question.location_id=city.id and"
    sql = sql + " location_id='" + str(location_id) + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    random_quizz = random.choice(result)
    # if cursor.rowcount > 0:
    #     for random_quizz in result:
    #         print(f"the question is {random_quizz}")
    return result
location_id=1
quiz_question(location_id)
currentQuestionList = quiz_question(location_id)
def generateRandomQuestion(questionList):
    randomQuestion = random.choice(questionList)
    return randomQuestion[0]
newRandomQuestion = generateRandomQuestion(currentQuestionList)
print(newRandomQuestion)

#  def quiz_question_option(quiz_question_id):
#      #1 get random id
#
#     get question based on that id
#
#     show answer with that id
#
#     let user choose option
#
#     # evaluate answer
#     # sql="select * from quiz_question_option where quiz_questionid;"
#     # moreSql = "where quiz_question_id =" +questionId
#     sql="select * from quiz_question_option;"
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)
#     if cursor.rowcount > 0:
#         for index,row in enumerate(result,start=1) :
#             print(index,")",f"{row[1]}")
#         player = int(input("what is the answer of this question (choose the number): "))
#     answer = result[player-1]
#     print(answer)
#     isCorrect = answer[3]
#     print(type(isCorrect))
#     if isCorrect == 1:
#         print(" your answer is correct")
#     else:
#         print("your answer is not correct")
#     # if player==row[0]:
#     #     print("correct")
#     # else:
#     #     print("incorrect")
#         return
# quiz_question_option()


