import envControl.control.relayBase as relayBase


water_pin = 2


def waterOn():
	relayBase.relayOn(water_pin)

def waterOff():
	relayBase.relayOff(water_pin)

