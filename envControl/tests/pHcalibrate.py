
from envControl.control import sensorControl
import sqlite3


def calibrate():
	conn = sqlite3.connect('../databases/parameters.db')
	cur = conn.cursor()

	# grab first pH measurement
	input("Please put your pH probe into a known solution, press any key to continue")
	pH1 = float(input("What is the pH of your first solution\n?"))
	print("Taking pH measurement")
	voltage1 = sensorControl.readpHVolts()

	# grab second pH measurement
	input("Now put your pH probe into distilled water for a couple of minutes, press any key when done")
	input("Please put your pH probe into a different known solution, press any key to continue")
	pH2 = float(input("What is the pH of your second solution\n?"))
	print("Taking pH measurement")
	voltage2 = sensorControl.readpHVolts()

	m = (pH1 - pH2) / (voltage1 - voltage2)
	print(m)
	cur.execute("SELECT * FROM CALIBRATION WHERE type='pHslope'")
	m_original = cur.fetchall()[0][2]


	type = 'pHslope'
	cur.execute("UPDATE CALIBRATION SET VALUE=? WHERE TYPE='pHslope'", m)
	conn.commit()
	conn.close()

	print("Value of pH slope m changed from ", m_original, " to ", m)

