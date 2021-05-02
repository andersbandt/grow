import sqlite3
import os

# insertReading: insert a value into the readings database
# inputs: sensor - sensor from which the reading is coming from, should take the form
# 	of a string with the same name as the desired table name
def insertReading(sensor, value, date_string):
	conn = lite.connect('databases/readings.db')
	cur = conn.cursor()

	with conn:
		cur = con.cursor()
		cur.execute('INSERT INTO ? (DATETIME, VALUE) \
			VALUES(?, ?)', (sensor, value, date_string))

	print(sensor, " value of ", value, " recorded at ", date_string, " inserted into readings")
	conn.close()
	return True

# getParameter: returns certain calibration parameter
# input: parameter - string representing parameter type
def getCalibrationParameter(parameter):
	conn = sqlite3.connect('databases/parameters.db')
	cur = conn.cursor()

	with conn:
		cur.execute('SELECT * FROM CALIBRATION WHERE type=?', (parameter,))
		parameter = cur.fetchall()
		print("I received this as a parameter")
		print(parameter)
	conn.close()
	return parameter[0][2]

# getSchedule: returns certain schedule parameter
# input: area - control area
# outputs: schedule parameter 1; schedule parameter 2
def getScheduleParameter(area):
	conn = sqlite3.connect('databases/parameters.db')
	cur = conn.cursor()

	with conn:
		cur.execute('SELECT * FROM SCHEDULE WHERE AREA=?', (area,))
		parameter = cur.fetchall()
		print("I received this as a parameter")
		print(parameter)
	conn.close()
	return parameter[0][2], parameter[0][3]


# updateScheduleParam: updates a control area's parameters in the database
# input: area - control area; num - parameter number; value - value in parameter
# 	num should be 1 if changing parameter 1, 2 for parameter 2, and so on...
# output: none
def updateScheduleParam(area, num, value):
	conn = sqlite3.connect('databases/parameters.db')
	cur = conn.cursor()

	if num == 1:
		param = 'PARAM1'
	elif num == 2:
		param == 'PARAM2'
	else:
		print("Invalid parameter number sent")
		return False

	with conn:
		cur.execute('UPDATE SCHEDULE SET ?=? WHERE area=?', (param, value, area,))

	conn.close()


# getState: returns the on/off state of a control area
# input: area - control area
# output: 0/1 representing off/on
def getState(area):
	conn = sqlite3.connect('databases/runtimes.db')
	cur = conn.cursor()

	with conn:
		cur.execute('SELECT * FROM STATES WHERE area=?', (area,))
		parameter = cur.fetchall()
		print("I received this as a parameter")
		print(parameter)

	conn.close()
	return parameter[0][2], parameter[0][3] # should return the timestamp and the state


# updateState: updates the state of a control area
# input: area - control area; timestamp - timestamp the state was set at;
# 	state - the new state of the control area
# output: none
def updateState(area, timestamp, state):
	conn = sqlite3.connect('databases/runtimes.db')
	cur = conn.cursor()

	with conn:
		cur.execute('UPDATE STATES SET DATETIME=?, STATE=? WHERE area=?', (timestamp, state, area,))
		parameter = cur.fetchall()
		print("Updated ", area, "state to ", state)

	conn.close()
	return True 


# should print all the tables in a database
def tables_in_sqlite_db(conn):
	cursor = conn.execute("SELECT name FROM sqlite_master WHERe type='table';")
	tables = [
		v[0] for v in cursor.fetchall()
		if v[0] != "sqlite_sequence"
		]
	cursor.close()
	return tables
