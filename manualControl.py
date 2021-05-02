import envControl.control.lightControl as lightControl
import envControl.control.fanControl as fanControl
import envControl.control.pHControl as pHControl
import envControl.control.pumpControl as pumpControl
import envControl.control.airControl as airControl
import envControl.control.waterControl as waterControl
import envControl.control.sensorControl as sensorControl
import envControl.control.relayBase as relayBase


import envControl.tests.pHcalibrate as pHcalibrate
import envControl.tests.pHtest as pHtest
import envControl.tests.ECtest as ECtest

from databases import *

import scheduler.checkSchedule as checkScheduler
import scheduler.updateSchedule as updateScheduler


# main method to run to gather user input
def main():
	quit = False
	while not quit:
		print("Press 1 to control light")
		print("Press 2 to control fans")
		print("Press 3 to control pH")
		print("Press 4 to control pumps")
		print("Press 5 to read sensor input")
		print("Press 6 to control air and water")
		print("Press 7 to do a schedule/status check")
		print("Press 8 to update the schedule")
		print("Press 9 to run some system tests")
		print("Press anything else to quit")
		are = int(input("Enter control area number!"))

		if are == 1:
			controlLights()
		elif are == 2:
			controlFans()
		elif are == 3:
			controlpH()
		elif are == 4:
			controlPumps()
		elif are == 5:
			controlSensors()
		elif are == 6:
			controlAirWater()
		elif are == 7:
			checkSchedule()
		elif are == 8:
			updateSchedule()
		elif are == 9:
			runTests()
		else:
			quit = True

# function to control lights
def controlLights():
	print("Press 1 to turn light on")
	print("Press 2 to turn light off")
	act = int(input("Enter control action please!"))

	if act == 1:
		lightControl.lightOn()
		controlLights()
	elif act == 2:
		lightControl.lightOff()
		controlLights()


# function to control fans
def controlFans():
	print("Press 1 to turn intake fan on")
	print("Press 2 to turn intake fan off")
	print("Press 3 to turn outtake fan on")
	print("Press 4 to turn outtake fan off")
	act = int(input("Enter control action please!"))

	if act == 1:
		fanControl.intakeOn()
		controlFans()
	elif act == 2:
		fanControl.intakeOff()
		controlFans()
	elif act == 3:
		fanControl.outtakeOn()
		controlFans()
	elif act == 4:
		fanControl.outtakeOff()
		controlFans()
	elif act == 9:
		return


# function to control pH
def controlpH():
	print("Press 1 to add acid")
	print("Press 2 to add base")
	print("Press 3 to calibrate pH meter")
	print("Press 4 to adjust pH offset voltage")
	print("Press 5 to run a pH test")
	print("Press 9 to quit")
	act = int(input("Enter control action please!"))

	quit = False
	if act == 1:
		pHControl.addAcid()
		controlpH()
	elif act == 2:
		pHControl.addBase()
	elif act == 3:
		pHcalibrate.calibrate()
	elif act == 4:
		sensorControl.adjustpHOffset()
	elif act == 5:
		pHtest.main()
	elif act == 9:
		main()


# function to manually control all the pump relays
def controlPumps():
	print("Press 1 to turn on pump 1")
	print("Press 2 to turn off pump 1")
	print("Press 3 to turn on pump 2")
	print("Press 4 to turn off pump 2")
	print("Press 5 to turn on pump 3")
	print("Press 6 to turn off pump 3")
	print("Press 7 to turn on pump 4")
	print("Press 8 to turn off pump 4")
	print("Press 9 to turn on pump 5")
	print("Press 10 to turn off pump 5")
	print("Press 11 to quit")
	act = int(input("Enter control action please"))

	if act == 1: # pump 1
		relayBase.relayOn(5)
	elif act == 2:
		relayBase.relayOff(5)
		controlPumps()
	elif act == 3: # pump 2
		relayBase.relayOn(6)
		controlPumps()
	elif act == 4:
		relayBase.relayOff(6)
		controlPumps()
	elif act == 5: # pump 3
		relayBase.relayOn(13)
		controlPumps()
	elif act == 6:
		relayBase.relayOff(13)
		controlPumps()
	elif act == 7: # pump 4
		relayBase.relayOn(19)
		controlPumps()
	elif act == 8:
		relayBase.relayOff(19)
		controlPumps()
	elif act == 9: # pump 5
		relayBase.relayOn(26)
		controlPumps()
	elif act == 10:
		relayBase.relayOff(26)
		controlPumps()
	else:
		return


# function to control sensors
def controlSensors():
	print("Press 1 to read pH")
	print("Press 2 to read EC")
	print("Press 3 to read TDS")
	print("Press 4 to read air temperature")
	print("Press 9 to quit")

	act = int(input("Enter control action please!"))

	if act == 1:
		sensorControl.readpH()
		controlSensors()
	elif act == 2:
		sensorControl.readEC()
		controlSensors()
	elif act == 3:
		sensorControl.readTDS()
		controlSensors()
	elif act == 4:
		sensorControl.readTemp()
		controlSensors()
	elif act == 9:
		return



# function to control air and water pumps within tank
def controlAirWater():
	print("Press 1 to turn air on")
	print("Press 2 to turn air off")
	print("Press 3 to turn water pump on")
	print("Press 4 to turn water pump off")
	print("Press 5 to empty the tank (timed)")
	print("Press 6 to empty the tank (amount)")

	act = int(input("Enter control action please!"))

	if act == 1:
		airControl.airOn()
		controlAirWater()
	elif act == 2:
		airControl.airOff()
		controlAirWater()
	elif act == 3:
		waterControl.waterOn()
		controlAirWater()
	elif act == 4:
		waterControl.waterOff()
		controlAirWater()
	elif act == 5:
		waterControl.emptyTankTimed(-1)
		controlAirWater()
	elif act == 6:
		waterControl.emptyTankAmount()
		controlAirWater()
	elif act == 9:
		return


# function to control nutrients
def controlNutrients():
	print("Press 1 to add 284")
	print("Press 2 to add 644")
	print("Press 3 to add 057")

	act = int(input("Enter control action please!"))

	if act == 1:
		pumpControl.pumpFluid('284', 15) # should theoretically pump 15 mL of nutrient fluid
	elif act == 2:
		pumpControl.pumpFluid('644', 15) # should theoretically pump 15 mL of nutrient fluid
	elif act == 3:
		pumpControl.pumpFluid('057', 15) # should theoretically pump 15 mL of nutrient fluid


# function to run a schedule check
def checkSchedule():
	checkScheduler.checkAll()


# function to update the schedule
def updateSchedule():
	updateScheduler.updateSchedule(-1)


def runTests():
	print("Press 1 to run a nutrient test (parameters already declared")

	act = int(input("Enter control action please!"))

	if act == 1:
		ECtest.testNutrient()
	else:
		return





if __name__ == "__main__":
	main()

