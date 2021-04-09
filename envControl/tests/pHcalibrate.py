
from control import sensorControl
import sqlite3


def main():
	conn = sqlite3.connect('\..\..\databases\parameters.db')
	cur = conn.cursor()

	m = -6.95
	type = 'pHslope'
	cur.execute("INSERT INTO CALIBRATION (TYPE, VALUE) \
			VALUES (?, ?)",
			(type, m))

	conn.commit()
	conn.close()


if __name__ == "__main__":
	main()
