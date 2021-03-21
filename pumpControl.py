import relayControl
import time

pump1_pin = 1
pump2_pin = 2
pump3_pin = 3
pump4_pin = 4
pump5_pin = 5

mL_sec = .03 # flow rate of pumps in mL/sec


# this function pumps a certain amount (in mL) of fluid at a certain pump
def pumpFluid(pump, amount):
	if pump == 'acid':
		relayControl.relayOn(pump1_pin)
	elif pump == 'base':
		relayControl.relayOn(pump2_pin)
	elif pump == '284':
		relayControl.relayOn(pump3_pin)
	elif pump == '644':
		relayControl.relayOn(pump4_pin)
	elif pump == '057':
		relayControl.relayOn(pump5_pin)



