import control.relayBase
import time

pump1_pin = 5 # tied to
pump2_pin = 6 # tied to
pump3_pin = 13 # tied to
pump4_pin = 19 # tied to base
pump5_pin = 26 # tied to acid

mL_sec = 1 # flow rate of pumps in mL/sec

# this function pumps a certain amount (in mL) of fluid at a certain pump
def pumpFluid(pump, amount):
	if pump == 'acid':
		relayBase.relayOn(pump5_pin)
		time.sleep(amount/mL_sec)
		relayBase.relayOff(pump5_pin)
	elif pump == 'base':
		relayBase.relayOn(pump4_pin)
		time.sleep(amount/mL_sec)
		relayBase.relayOff(pump4_pin)
	elif pump == '284':
		relayBase.relayOn(pump3_pin)
		time.sleep(amount/mL_sec)
		relayBase.relayOff(pump3_pin)
	elif pump == '644':
		relayBase.relayOn(pump4_pin)
		time.sleep(amount/mL_sec)
		relayBase.relayOff(pump4_pin)
	elif pump == '057':
		relayBase.relayOn(pump5_pin)
		time.sleep(amount/mL_sec)
		relayBase.relayOff(pump5_pin)
