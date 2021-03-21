import serialManager
import time




def readPH():
	serialManager.sendChar('P')
	time.sleep(.5)
	pH = serialManager.readLine()
	print(pH)

def readWaterTemp():
	serialManager.sendChar('W')
	time.sleep(.5)
	waterTemp = serialManager.readLine()
	print(waterTemp)

def readTemp():
	serialManager.sendChar('T')
	time.sleep(.5)
	temp = serialManager.readLine()
	print(temp)

def readEC():
	serialManager.sendChar('E')
	time.sleep(.5)
	EC = serialManager.readLine()
	print(EC)

def readTDS():
	serialManager.sendChar('D')
	time.sleep(.5)
	TDS = serialManager.readLine()
	print(TDS)



readPH()
readWaterTemp()
readTemp()
readEC()
readTDS()
