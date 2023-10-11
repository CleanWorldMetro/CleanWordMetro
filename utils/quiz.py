import random
from config import connection
import player as playerUti


def quiz_questions(location_id):
    selectedField = "quiz_question.id, quiz_question.text"
    sql = f"select {selectedField} from city,quiz_question"
    sql = sql + " where quiz_question.location_id=city.id and"
    sql = sql + " location_id='" + str(location_id) + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    return result
# questionList =  quiz_questions(location_id)
# currentQuestionList = quiz_questions(location_id)
def generateRandomQuestion(questionList):
    randomQuestion = random.choice(questionList)
    print(randomQuestion[1])
    return randomQuestion
# ('Which of the following is a (1, 'Helsinki', 1, 0, 4,
# "Finland's Everyman's Right (Jokamiehenoikeus) allows people to:",
# 1) eco-friendly cleaning practice in Finland?',)

def getOptionForQuestions(id):
    sqlField = "id, text, is_correct"
    sql = f"SELECT {sqlField} from quiz_question_option "
    finalsql = sql + "where quiz_question_id = " + str(id)
    cursor = connection.cursor()
    cursor.execute(finalsql)
    result = cursor.fetchall()
    # print("this is", result)
    # result =runSQL(sql)
    # resultList = enumerate(result, start=1)
    for index, question in  enumerate(result,start=1):
        print(f"{index} {question[1]}")

        # print(question)
    return result

def userAnswer(options):
    option_id = int(input("Type your answer(1-4): "))
    # options = getOptionForQuestions(question_id)
    # print(options)
    user_option = options[option_id - 1]
    print("This is your answer: ", user_option[1])
    return user_option

def checking(userAnswer): ## return true or false for the user answer
    answerIsCorrect = userAnswer[2]## check if option is correct
    if answerIsCorrect == 1 :
        print(" You are correct!")
        return True
    else:
        print(" You are not correct")
        return False

def answer(userAnswer,playerStat):
    # when player answer right, stat +1, wrong stat -1
    if checking(userAnswer): #
        playerStat += 1
    else:
        playerStat -= 1
    return playerStat

def insertUserOption(userOption):
    userOptionToTuple = tuple(userOption)
    userOptionColumn = "player_ID,quiz_question_ID,quiz_answer_option_ID,is_correct"
    sql = f"INSERT INTO quiz_user_answer({userOptionColumn}) Value {userOptionToTuple}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result #result user answer as a

def answer(userOption,playerStat):
    # when player answer right, stat +1, wrong stat -1
    if checking(userOption): #
        playerStat += 1
    else:
        playerStat -= 1
    insertUserOption(userOption)
    return playerStat


# create a quiz def and return a new stat of player
def quiz(playerData):
    playerData = playerUti.formatPlayerData(playerData)
    print(playerData)
    userId = playerData[0]
    # print(userId)
    location_id = playerData[4]
    # print(quiz_questions(1))
    questionList = quiz_questions(location_id)  # get question list from location id
    # print(questionList)
    questionId = generateRandomQuestion(questionList)[0]  # get questionID
    # print(generateRandomQuestion())
    # question(questionId)
    options = getOptionForQuestions(questionId)  # get options from question ID
    # # print(options)
    userOptionAnswer = userAnswer(options)  # user choose answer
    # print(userOptionAnswer)
    userOptionAnswerId = userOptionAnswer[0]
    # print(userAnswer)
    # userAnswer_Id = userOptionAnswer[0]
    # print(userAnswer_Id)
    # #
    # isCorrect = checking(userOptionAnswer)  ## have it
    # userOptionAnswerData = [userId,questionId,userOptionAnswerId,isCorrect]
    newPlayerStat = answer()
    # print(userOption)# Record of User Answer
    # print(userOption)
    insertUserOption(userOptionAnswerData)
    # dataTuple = playerDataToTuple
    return

player = playerUti.getPlayerByID(3)
# print(player)
quiz(player)