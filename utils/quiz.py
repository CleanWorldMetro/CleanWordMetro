import random
from config import connection


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