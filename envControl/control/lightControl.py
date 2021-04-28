import envControl.control.relayBase as relayBase


light_pin = 4

def lightOn():
	relayBase.relayOn(light_pin)


def lightOff():
	relayBase.relayOff(light_pin)
