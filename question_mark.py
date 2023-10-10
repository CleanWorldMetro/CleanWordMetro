import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='clean_world',
    user='mark',
    password='metropolia')


def question(robo_id):
    sql = "SELECT id, text FROM quiz_question WHERE id =" + str(robo_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f'Question is: {row[1]}')


robo = int(input('robo id: '))
question(robo)
