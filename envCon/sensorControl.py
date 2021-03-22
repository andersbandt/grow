import serialManager
import time


def readPH():
	serialManager.sendChar('P')
	time.sleep(.5)
	pH = serialManager.readLine()
	print("pH: ")
	print(pH)
	return pH

def readWaterTemp():
	serialManager.sendChar('W')
	time.sleep(.5)
	waterTemp = serialManager.readLine()
	print("Water temperature: ")
	print(waterTemp)
	return waterTemp

def readTemp():
	serialManager.sendChar('T')
	time.sleep(.5)
	temp = serialManager.readLine()
	print("Air temp: ")
	print(temp)
	return temp

def readEC():
	serialManager.sendChar('E')
	time.sleep(.5)
	EC = serialManager.readLine()
	print("EC: ")
	print(EC)
	print("ms/cm")
	return EC

def readTDS():
	serialManager.sendChar('D')
	time.sleep(.5)
	TDS = serialManager.readLine()
	print("TDS: ")
	print(TDS)
	print("ppm")
	return TDS


readPH()
readWaterTemp()
readTemp()
readEC()
readTDS()
