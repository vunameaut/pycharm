
import sqlite3
path = "D:/hoc tap/python/data/test.db"
conn = sqlite3.connect(path)
print(conn)

def printAll(result):
    for item in result:
        print(item)

cursor = conn.cursor()
cursor.execute("SELECT * FROM giangvien")
result = cursor.fetchall()



print(printAll(result))




conn.close()








