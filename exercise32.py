import sqlite3
path = sqlite3.connect("C:/Users/Phu Nguyen/OneDrive/Documents/phu/phunguyen")
print(path)

c = path.cursor()
c.execute("DROP TABLE IF EXISTS hocsinh")
sql = """
    CREATE TABLE student (
        fullname text(50) NOT NULL PRIMARY KEY,
        avgpoint numberic(50) NOT NULL,
        yearolds numberic(50) NOT NULL

         
    )
"""
c.execute(sql)