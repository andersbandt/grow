import unittest
from control import sensorControl
import sqlite3


def main():
	conn = sqlite3.connect('../databases/parameters.db')


	m = -6.95
	type = 'pHslope'
	conn.execute("INSERT INTO CALIBRATION (TYPE, VALUE) \
			VALUES (?, ?)",
			(type, m))

	conn.commit()
	conn.close()


if __name__ == "__main__":
	main()
