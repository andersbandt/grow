import sqlite3

conn = sqlite3.connect('data.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE TEMPERATURE
		(ID INTEGER PRIMARY KEY AUTOINCREMENT,
		DATETIME     TEXT   NOT NULL,
		VALUE        INT    NOT NULL);''')

print("Table created successfuly")

conn.close()
