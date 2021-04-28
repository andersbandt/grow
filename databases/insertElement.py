import sqlite3


def insertCalibration():
	conn = sqlite3.connect('parameters.db')
	conn.execute("INSERT INTO CALIBRATION (TYPE, VALUE) \
			VALUES ('pHslope', -6.17)")
	conn.commit()
	conn.close()



def insertState(area):
	conn = sqlite3.connect('databases/parameters.db')
	cur = conn.cursor()

	with conn:
		cur.execute('INSERT INTO STATES (AREA, TIMESTAMP, STATE) WHERE type=?', (area, 1.0, 0))

	conn.close()


insertState("Light")

