import mysql.connector
import random
connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'clean_world',
    user= 'dbuser',
    password= 'pass_word',
    autocommit=True)
mylist=[]
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

def generateRandomQuestion(questionList):
    randomQuestion = random.choice(questionList)
    return randomQuestion[0]
# newRandomQuestion = generateRandomQuestion(currentQuestionList)
# print(newRandomQuestion)



def quiz_question_id(name):
    sql="select quiz_question.id from quiz_question"
    sql=sql + " where quiz_question.text='"+name+"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    if cursor.rowcount > 0:
        for id in result:
            # print(id[0])
            return id[0]
    # return

location_id = 1  ## get location
# print(quiz_question(location_id))
currentQuestionList = quiz_question(location_id) ## get question list at location id 1
# print(currentQuestionList)
question = generateRandomQuestion(currentQuestionList)
print(question)
mylist.append(question)
# print(quiz_question_id(question))
var1 = quiz_question_id(question)
print(var1)


# for x in mylist:
#     print(x)
# name=x
# var1 = quiz_question_id(question)
# # print(quiz_question_id(name))
# print(var1)
# print(someVar)


