import unittest
from ..control.sensorControl import sensorControl
import sqlite3


def main():
	conn = sqlite3.connect('home/pi/grow/databases/parameters.db')


	m = -6.95
	type = 'pHslope'
	conn.execute("INSERT INTO CALIBRATION (TYPE, VALUE) \
			VALUES (?, ?)",
			(type, m))

	conn.commit()
	conn.close()


if __name__ == "__main__":
	main()
