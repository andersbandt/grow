import sqlite3
import os



def tables_in_sqlite_db(conn):
	cursor = conn.execute("SELECT name FROM sqlite_master WHERe type='table';")
	tables = [
		v[0] for v in cursor.fetchall()
		if v[0] != "sqlite_sequence"
		]
	cursor.close()
	return tables



def getParameter(parameter):
	conn = sqlite3.connect('../databases/parameters.db')
	cur = conn.cursor()

	with conn:
		cur.execute('SELECT * FROM CALIBRATION WHERE type=?', (parameter,))
		parameter = cur.fetchall()
		return parameter[0][2]

	conn.close()
