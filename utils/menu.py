from config import connection


def getPlayers():
    sql = "SELECT * from player"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print("this is",result)
    # result =runSQL(sql)
    return result

def isExist(username,namesInDatabase ):
    if username in namesInDatabase:
        return True
    else:
        return False

def formatedNameList(nameListFromDatabase): # return onlyNameList
    onlyNameList = []
    for nameData in nameListFromDatabase:
        nameInData = nameData[1]
        # print(nameInData)
        onlyNameList.append(nameInData)
    # print(onlyNameList)
    return onlyNameList


def inputName():
    name = input("Type your username: ")
    return name

def existNameGUI():
    print("1.New game")
    print("2.Continue")
    print("3.Exit program")
    option = input("Please enter your option(1-3): ")
    return option

def newGame(name):
    nameData = [name,]