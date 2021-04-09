import control.serialBase as serialBase
import control.dataBase as dataBase
import time

def readpH():
	m = dataBase.getParameter('pHslope')
	serialBase.sendChar('P')
	time.sleep(.5)
	pH_voltage = float(serialBase.readLine()[:4]) # get rid of the new line carriage '\r\n' and convert to float
	pH = round(7 - (2.5 - pH_voltage)*m, 2)
	print("pH: ")
	print(pH)
	return pH

def readWaterTemp():
	serialBase.sendChar('W')
	time.sleep(.5)
	waterTemp = serialBase.readLine()
	print("Water temperature: ")
	print(waterTemp)
	return waterTemp

def readTemp():
	serialBase.sendChar('T')
	time.sleep(.5)
	temp = float(serialBase.readLine()[:5].decode) # extract temp voltage
	print("Air temp: ")
	print(temp)
	return temp

def readEC():
	serialBase.sendChar('E')
	time.sleep(.5)
	EC = serialBase.readLine()
	print("EC: ")
	print(EC)
	print("ms/cm")
	return EC

def readTDS():
	serialBase.sendChar('D')
	time.sleep(.5)
	TDS = serialBase.readLine()
	print("TDS: ")
	print(TDS)
	print("ppm")
	return TDS

