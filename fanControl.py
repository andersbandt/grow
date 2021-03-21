import relayControl
import time



def fanOn(fan_pin):
	relayControl.relayOn(fan_pin)

def fanOff(fan_pin):
	relayControl.relayOff(fan_pin)


