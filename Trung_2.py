name = "Trung1"
nameData = [name, 1, 1, 1, 3, 1]

nameDataToTuple = tuple(nameData)
playerComlumn = "name, resStat, location, isInCity, energy, isNew"
sql = f"INSERT INTO player({playerComlumn}) VALUE {nameDataToTuple}"

print(sql)
