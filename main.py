import mysql.connector
import random
import utils.game as game
connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'clean_world',
    user= 'dbuser',
    password= 'pass_word',
    autocommit=True)
def main():
    while True:
        # if isNew
        # show game introduction

        #show normal game
        # show

        option = game.inCityGui()
        game.chooseOptionInCity(option)


main()

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