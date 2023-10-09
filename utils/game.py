def inCityGui():
    print("What do you want to do \n"
          "1. go meet the boss \n"
          "2. Go farm\n"
          "3. Go play quiz\n"
          "4. Do nothing\n")
    option = input("What do you want to do? (1-4) ")
    return int(option)
def chooseOptionInCity(number):
    if number == 1:
        print("meet boss")
    if number == 2:
        print("go farm")
    if number == 3:
        print("let's find some treasure")
    if number == 4:
        print("do nothing")

