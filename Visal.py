
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="clean_world",
    user="root",
    password="1234",
    autocommit=True
)




def start():
    print("Welcome to the Game or sth!")
    print("Press 1. for New Game")
    print("Press 2. to Continue")
    print("Press 3. to Exit")
    option = int(input("Enter option: "))

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


start()



