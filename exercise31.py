
import sqlite3
path = "C:/Users/Phu Nguyen/OneDrive/Documents/phu/exercise1.py"
connection = sqlite3.connect(path)
print(connection)

cursor = connection.cursor()
sql = "SELECT `họ và tên`, `năm sinh` FROM sinhvien"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
