
import utils.menu as menu
# import utils.quiz as quiz

def main():
    while True:
        # if isNew
        # show game introduction

        #show normal game
        # show
        # username =menu()
        # menu.menu()
        # getPlayerByName(username)
        username = menu.inputName()
        nameListInDatabase = menu.getPlayers()
        onlyNameList = menu.formatedNameList(nameListInDatabase)
        # print(nameInDatabase)

        if menu.isExist(username,onlyNameList) == True:
            # menu.existNameGUI()
            option = menu.existNameGUI()

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
        # option = game.inCityGui() # user choose option when incity
        # game.chooseOptionInCity(option) #


main()

