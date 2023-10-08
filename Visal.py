import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port= 3306,
    database="clean_world",
    user="root",
    password="1234",
    autocommit=True
)


def getrobot(robot):
    sql = "SELECT id, name, location FROM robot WHERE id=" + str(robot)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f"I am {row[1]}: My location is {row[2]}")
    return


robot = int(input("Enter robot id: "))
getrobot(robot)

