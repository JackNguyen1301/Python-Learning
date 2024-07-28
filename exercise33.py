import sqlite3
path = "C:/Users/Phu Nguyen/OneDrive/Documents/phu/phunguyen"
connection = sqlite3.connect(path)
print(connection)

cursor = connection.cursor()
# for i in range(1, 11):
#     x = "INSERT INTO student(fullname, avgpoint, yearolds) VALUES (" + str(i)+ ", " +str(i*2) +", 10)"
#     cursor.execute(x)
#     connection.commit()
x = "SELECT * FROM student WHERE avgpoint=100"
cursor.execute(x)
result = cursor.fetchall()
print(result)
cursor.close()
