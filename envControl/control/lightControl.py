import envControl.control.relayBase as relayBase
import databases.dataBase as dataBase
import datetime

light_pin = 4

def lightOn():
	relayBase.relayOn(light_pin)


def lightOff():
	relayBase.relayOff(light_pin)


def lightOnStateChange():
	relayBase.relayOn(light_pin)
	cur_time = datetime.datetime.now()
	cur_time = int(cur_time.strftime('%H%M%S'))
	dataBase.updateState("Light", cur_time, 1)

	return True


def lightOffStateChange():
	relayBase.relayOff(light_pin)
	cur_time = datetime.datetime.now()
	cur_time = int(cur_time.strftime('%H%M%S'))
	dataBase.updateState("Light", cur_time, 0)

	return True



