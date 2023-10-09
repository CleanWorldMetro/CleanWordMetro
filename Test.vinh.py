#fetch tat ca nhung cau hoi cua city 1
#chay thu tren mysql

#luu het tat ca nhung cau hoi vao list
# random cau hoi trong list
# sql = "select quiz_question.text from city,quiz_question"
# sql = sql + " where quiz_question.location_id=city.id and"
# sql = sql + " city.id='1';"
# print(sql)
city_id=1
sql = "select quiz_question.text from city,quiz_question"
sql=sql+" where quiz_question.location_id=city.id and"
sql=sql+" city_id='"+ str(city_id) +"'"
print(sql)
# sql = "select name,municipality from airport"
#     sql = sql + " where ident='"+ ident + "'"
#     print(sql)