import sqlite3


def insertCalibration():
	conn = sqlite3.connect('parameters.db')
	conn.execute("INSERT INTO CALIBRATION (TYPE, VALUE) \
			VALUES ('pHslope', -6.17)")
	conn.commit()
	conn.close()



def insertState(area):
	conn = sqlite3.connect('runtimes.db')
	cur = conn.cursor()

	with conn:
		cur.execute('INSERT INTO STATES (AREA, DATETIME, STATE) VALUES (?, 1.0, 0)', (area,))

	conn.close()


def insertSchedule(area):
	conn = sqlite3.connect('parameters.db')
	cur = conn.cursor()

	with conn:
		cur.execute('INSERT INTO SCHEDULE (AREA, PARAM1, PARAM2) VALUES (?, 100000, 16)', (area,))

	conn.close()	


#insertState("Light")
insertSchedule("Light")



