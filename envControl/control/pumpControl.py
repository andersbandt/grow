import envControl.control.relayBase as relayBase
import time

pump1_pin = 5 # tied to
pump2_pin = 6 # tied to
pump3_pin = 13 # tied to
pump4_pin = 19 # tied to base
pump5_pin = 26 # tied to acid


# this function turns a certain pump on
def pumpOn(pump, seconds):
	if pump == 'acid':
		relayBase.relayOn(pump5_pin)
		print("Pumped some acid")
	elif pump == 'base':
		relayBase.relayOn(pump4_pin)
	elif pump == 'nut_1':
		relayBase.relayOn(pump3_pin)
	elif pump == 'nut_2':
		relayBase.relayOn(pump2_pin)
	elif pump == 'nut_3':
		relayBase.relayOn(pump1_pin)

# this function turns a certain pump on
def pumpOff(pump, seconds):
	if pump == 'acid':
		relayBase.relayOff(pump5_pin)
		print("Pumped some acid")
	elif pump == 'base':
		relayBase.relayOff(pump4_pin)
	elif pump == 'nut_1':
		relayBase.relayOff(pump3_pin)
	elif pump == 'nut_2':
		relayBase.relayOff(pump2_pin)
	elif pump == 'nut_3':
		relayBase.relayOff(pump1_pin)


# pumpFluidTimed: turns on a pump for a second amount of seconds
# inputs: pump - string representing what pump we want; seconds - how many seconds we 
# 	want to run the pump
def pumpFluidTimed(pump, seconds):
	if pump == 'acid':
		relayBase.relayOn(pump5_pin)
		time.sleep(seconds)
		relayBase.relayOff(pump5_pin)
		print("Pumped some acid")
	elif pump == 'base':
		relayBase.relayOn(pump4_pin)
		time.sleep(seconds)
		relayBase.relayOff(pump4_pin)
	elif pump == 'nut_1':
		relayBase.relayOn(pump3_pin)
		time.sleep(seconds)
		relayBase.relayOff(pump3_pin)
	elif pump == 'nut_2':
		relayBase.relayOn(pump2_pin)
		time.sleep(seconds)
		relayBase.relayOff(pump2_pin)
	elif pump == 'nut_3':
		relayBase.relayOn(pump1_pin)
		time.sleep(seconds)
		relayBase.relayOff(pump1_pin)
