import envControl.control.relayBase as relayBase
import time

water_pin = 3
flow_rate = 1 # flow rate of pump in gallons/minute

def waterOn():
	relayBase.relayOn(water_pin)

def waterOff():
	relayBase.relayOff(water_pin)


def emptyTankTimed(timeAmount):
	if timeAmount == -1:
		timeAmount = int(input("Enter how many seconds you would like to run the water pump: "))
	print("Initiating tank emptying process for ", timeAmount, " seconds")
	waterOn()
	time.sleep(timeAmount)
	waterOff()


def emptyTankAmount(amount):
	time = 0
	if amount == -1:
		amount = int(input("Enter how many gallons you would like to empty: "))
		time = amount*flow_rate
	print("Initiating tank emptying process for ", time, " seconds")
	print("Should be around ", amount, " gallons pumped")
	waterOn()
	time.sleep()
	waterOff()

