import sys

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

def existNameGUI(name):
    print("Welcoome back,",name)
    print("1.New game")
    print("2.Continue")
    print("3.Exit program")
    option = int(input("Please enter your option(1-3): "))
    return option

def optionWithExistNameGUI(option,username):
    if option == 1:
        print("Welcome to new game!")

    elif option == 2:
        print("Here is your point and your stamina !")
    elif option == 3:
        print("End process")
        sys.exit()
    else:
        print("Invalid number, please type in range(1/2/3)")

def nonExistGUI():
    print("Congratulation !! It is a new name")
    print("1.New game")
    print("2.Exit program")
    option = int(input("Please enter your option(1/2): "))
    return option

def optionNonExistGUI(option,username):
    if option == 1:
        print("Welcome to Clean World!!!")

    elif option == 2:
        print("End process")
    else:
        print("Invalid number, please type in range(1/2)")
def menu():
    username =inputName()
    nameListInDatabase = getPlayers() # return list of username
    onlyNameList = formatedNameList(nameListInDatabase)
    # print(nameInDatabase)
    if isExist(username,onlyNameList) == True:
        # menu.existNameGUI()
        option = existNameGUI(username)
        player = optionWithExistNameGUI(option)

    else:
        option = nonExistGUI()
        player = optionNonExistGUI(option)

    return
def newGame(name):
    nameData = [name,]

menu()