import sqlite3

database = 'runtimes.db'

conn = sqlite3.connect(database)
print("Opened ", database, " successfully")


conn.execute('''CREATE TABLE STATES
		(ID INTEGER PRIMARY KEY AUTOINCREMENT,
		AREA     TEXT   NOT NULL,
		DATETIME TEXT   NOT NULL,
		STATE    INT    NOT NULL);''')

print("Table created successfuly")

conn.close()
