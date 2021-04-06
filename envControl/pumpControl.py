import relayBase
import time

pump1_pin = 5 # tied to acid
pump2_pin = 6 # tied to base
pump3_pin = 13 # tied to 284
pump4_pin = 19 # tied to 644
pump5_pin = 26 # tied to 057

mL_sec = .03 # flow rate of pumps in mL/sec

# this function pumps a certain amount (in mL) of fluid at a certain pump
def pumpFluid(pump, amount):
	if pump == 'acid':
		relayBase.relayOn(pump1_pin)
		time.sleep(amount/ml_sec)
		relayBase.relayOff(pump1_pin)
	elif pump == 'base':
		relayBase.relayOn(pump2_pin)
		time.sleep(amount/ml_sec)
		relayBase.relayOff(pump2_pin)
	elif pump == '284':
		relayBase.relayOn(pump3_pin)
		time.sleep(amount/ml_sec)
		relayBase.relayOff(pump3_pin)
	elif pump == '644':
		relayBase.relayOn(pump4_pin)
		time.sleep(amount/ml_sec)
		relayBase.relayOff(pump4_pin)
	elif pump == '057':
		relayBase.relayOn(pump5_pin)
		time.sleep(amount/ml_sec)
		relayBase.relayOff(pump5_pin)
