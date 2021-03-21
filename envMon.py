import fanControl
import pHControl
import sensors
import time
import threading

fan1_pin = 17
fan2_pin = 3
airPump_pin = 4
waterPump_pin = 6
light_pin = 3
pump1_pin = 1
pump2_pin = 3
pump3_pin = 6
pump4_pin = 2
pump5_pin = 1


def checkPH():
	pHControl.checkPH()


def checkTemp():
	sensors.readTemp()


def checkWaterTemp():
	sensors.readWaterTemp()

def checkTDS():
	sensors.readTDS()


def checkEC():
	sensors.readEC()




def main():
	print("Running main environment monitor function")

	print("Checking pH and making adjustments if necessary")
	checkPH()

	print("
	
	



if __name__ == "__main__"":
	main()
