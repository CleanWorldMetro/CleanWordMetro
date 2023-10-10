from config import connection
# print("Welcome to the Game or sth!")
# print("Press 1. for New Game")
# print("Press 2. to Continue")
# print("Press 3. to Exit")
# option = int(input("Enter option: "))
def start():


    if option == 1:
        print("Create username for a new game:")
        username = input("Enter username: ")
        print(f"Welcome, {username}! Let's start!")
        sql = f"INSERT INTO player(name) VALUES ('{username}')"

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()  # Commit the transaction

    elif option == 2:
        existing_user = input("Enter existing username: ")
        sql = f"SELECT * FROM player WHERE name = ('{existing_user}')"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            print(f"Welcome back {existing_user}!")


    elif option == 3:
        print("Exiting Game!")
# start()
def player():
    sql= "select player.name from player;"
    cursor= connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    if cursor.rowcount > 0:
        for x in result:
            print(f"{x[0]}")
    return

def enterUsername() :
    username = input("Enter your player name: ")
    return username
def userChooseGame(username,listUser):
    if username in listUser:
        print("1.Continue game with this name")
        print("2.Change a new name")
        print("3.Exit")
        number = int(input("Type your number(1,2,3): "))
        return number

def continueWithThisName():
    return

# player()
def nameofuser():
    listuser = []
    while True:
        username = input("Enter your player name: ")
        if username in listuser:
            print("1.Continue game with this name")
            print("2.Change a new name")
            print("3.Exit")
            number= int(input("Type your number(1,2,3): "))
            if number == 1:
                option= input("Do you want to continue: ")
                if option == "yes":
                    print("The game will be continue with previous stamina and point")
                elif option == "no":
                    listuser.remove(username)
                    newname = input("Enter your new name here: ")
                    listuser.append(newname)
                    print(f"{newname} is your currently player name")
                else:
                    print("Please answer (yes/no)")
            elif number == 2:
                listuser.remove(username)
                newname= input("Enter your new name here: ")
                listuser.append(newname)
                print(f"{newname} is your currently player name")
            elif number == 3:
                print("End process")
                break
            else:
                print("Invalid number, please choose in range(1,2,3)")
        else:
            print("Welcome to our game: \n SOS Team")
            print("Start new game !")
            listuser.append(username)
            break
# nameofuser()



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

def inputName():
     name= input("Type your username: ")
     return name
def formatedNameList(nameListFromDatabase):
    onlyNameList = []
    for nameData in nameListFromDatabase:
        nameInData = nameData[1]
        # print(nameInData)
        onlyNameList.append(nameInData)
    # print(onlyNameList)
    return onlyNameList
nameInDatabase = getPlayers()
checkName = isExist(inputName, nameInDatabase )
def game():
    while True:
        nameList = getPlayers() ## lay nameList
        onlyNameList = formatedNameList(nameList)
        # print(onlyNameList)
        name = inputName() ## user dien ten
        nameExist = isExist(name,onlyNameList)#return true or false
        print(nameExist)
        if nameExist == True:
            print("Name already used")
            print("Type another name")
            print(f"If you were {name}, please type again. And if you were not just entering another name")
            newName = input("Type your username: ")
            if newName == name:
                print("1.New game")
                print("2.Continue")
                print("3.Exit program")
                option = int(input("Please enter your option(1/2/3): "))
                if option == 1:
                    print("Welcome to new game!")
                    break
                elif option == 2:
                    print("Here is your point and your stamina !")
                    break
                elif option == 3:
                    print("End process")
                    break
                else:
                    print("Invalid number, please type in range(1/2/3)")
            elif newName != name and newName not in onlyNameList:
                print("1.New name")
                print("2.Exit program")
                option1 = int(input("Please enter your option(1/2): "))
                if option1 == 1:
                    print("Welcome to Clean World !!")
                    break
                elif option1 == 2:
                    print("End process")
                    break
        elif nameExist == False:
            print("Congratulation !! It is a new name")
            print("1.New game")
            print("2.Exit program")
            optionA = int(input("Please enter your option(1/2): "))
            if optionA == 1:
                print("Welcome to Clean World!!!")
                break
            elif optionA == 2:
                print("End process")
                break
            else:
                print("Invalid number, please type in range(1/2)")


        # while nameExist: # if name is existed
        #     print("Name already used")
        #     print("Type another name")
game()

    # nameExist = isExist(result1,name) # true / false
    # if nameExist == True:
    #     print("* Name already used")
    #     print("* Please type again")
    #     return
    # else:
    #     return
# print(getPlayers())

# inputName = inputName()
nameInDatabase = getPlayers()
checkName = isExist(inputName, nameInDatabase )
def optionPlayer():
    while True:

       if isExist(inputName, nameInDatabase) == True:
           print("1.New game")
           print("2.Continue")
           print("3.Exit program")
           option = int(input("Please enter your option(1/2/3): "))
           if option == 1:
               print("Welcome to new game!")
               break
           elif option == 2:
               print("Here is your point and your stamina !")
               break
           elif option == 3:
               print("End process")
               break
           else:
               print("Invalid number, please type in range(1/2/3)")
       else:
           print("Congratulation !! It is a new name")
           print("1.New game")
           print("2.Exit program")
           optionA = int(input("Please enter your option(1/2): "))
           if optionA == 1:
                print("Welcome to Clean World!!!")
                break
           elif optionA == 2:
                print("End process")
                break
           else:
                print("Invalid number, please type in range(1/2)")
# optionPlayer()















