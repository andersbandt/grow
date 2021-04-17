import envControl.control.relayBase as relayBase


air_pin = 2


def airOn():
	relayBase.relayOn(air_pin)

def airOff():
	relayBase.relayOff(air_pin)

