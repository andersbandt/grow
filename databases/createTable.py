import sqlite3 as lite

con = lite.connect('readings.db')

with con:

	cur = con.cursor()

	cur.execute("CREATE TABLE temp(id INT, value INT, time DATETIME)")
