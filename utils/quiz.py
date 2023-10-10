import random
from config import connection


def quiz_questions(location_id):
    sql = "select quiz_question.text from city,quiz_question"
    sql = sql + " where quiz_question.location_id=city.id and"
    sql = sql + " location_id='" + str(location_id) + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    # # random_quizz = random.choice(result)
    # print(random_quizz)
    # if cursor.rowcount > 0:
    #     for random_quizz in result:
    #         print(f"the question is {random_quizz}")
    return result
# questionList =  quiz_questions(location_id)
# currentQuestionList = quiz_questions(location_id)
def generateRandomQuestion(questionList):
    randomQuestion = random.choice(questionList)
    return randomQuestion[0]
# newRandomQuestion = generateRandomQuestion(currentQuestionList)
# print(newRandomQuestion)

userId = 1
questionId = 1
location_id = 1
# print(quiz_questions(1))
questionList = quiz_questions(location_id)
print(generateRandomQuestion(questionList))
# question(questionId)
# options = getOptionForQuestions(questionId)
# # print(options)
# userAnswer = userAnser(options)
# userAnswer_Id = userAnswer[0]
#
# isCorrect = checking(userAnswer) ## have it
# userOption = [userId,questionId,userAnswer_Id,isCorrect] # Record of User Answer
# print(userOption)
# insertUserOption(userOption)