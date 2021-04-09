import sqlite3


def getParameter(parameter):
	conn = sqlite3.connect('parameters.db')
	cur = conn.cursor()

	with conn:
		cur.execute('''SELECT VALUE FROM CALIBRATION WHERE TYPE=parameter''')
		return cur.fetchall()

	conn.close()
