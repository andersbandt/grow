import sqlite3

database = 'parameters.db'

conn = sqlite3.connect(database)
print("Opened ", database, " successfully")


conn.execute('''CREATE TABLE SCHEDULE
		(ID INTEGER PRIMARY KEY AUTOINCREMENT,
		AREA     TEXT   NOT NULL,
		PARAM1 INT   NOT NULL,
		PARAM2    INT    NOT NULL);''')

print("Table created successfuly")

conn.close()
