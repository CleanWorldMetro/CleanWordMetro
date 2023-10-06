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
            print("Welcome to our game: \nClean World")
            print("Start new game !")
            listuser.append(username)
            break
nameofuser()