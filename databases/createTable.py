import sqlite3

conn = sqlite3.connect('parameters.db')
print("Opened database successfully")


conn.execute('''CREATE TABLE CALIBRATION
		(ID INTEGER PRIMARY KEY AUTOINCREMENT,
		AREA     TEXT   NOT NULL,
		STATE        FLOAT    NOT NULL);''')

print("Table created successfuly")

conn.close()
