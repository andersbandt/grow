import sqlite3

conn = sqlite3.connect('parameters.db')



conn.execute("INSERT INTO CALIBRATION (TYPE, VALUE) \
		VALUES ('pHslope', -6.17)")

conn.commit()

conn.close()
