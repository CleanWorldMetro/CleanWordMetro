import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='clean_world',
    user='mark',
    password='metropolia')


def question():
    sql = "SELECT id, text FROM quiz_question order by rand() limit 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #print(result)
    #for row in result:
        #print(f'Question is: {row[1]}')
    return result



item = question()
print(item)
