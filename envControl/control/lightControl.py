import control.relayBase as relayBase


light_pin = 2

def lightOn():
	relayControl.relayOn(light_pin)


def lightOff():
	relayControl.relayOff(light_pin)
