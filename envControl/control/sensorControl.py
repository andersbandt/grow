import control.serialBase as serialBase
import control.dataBase as dataBase
import time

# function to read analog input pH and convert to pH
def readpH():
	m = dataBase.getParameter('pHslope')
	serialBase.sendChar('P')
	time.sleep(.5)
	pH_voltage = float(serialBase.readLine()[:4]) # get rid of the new line carriage '\r\n' and convert to float
	pH = round(7 - (3.26 - pH_voltage)*m, 2)
	print("pH: ")
	print(pH)
	return pH

# function to read the raw pH voltage
def readpHVolts():
	serialBase.sendChar('P')
	time.sleep(.5)
	pH_voltage = float(serialBase.readLine()[:4])
	print(pH_voltage)
	return pH_voltage

# function to display the pH voltage over and over
def adjustpHOffset():
	while True:
		serialBase.sendChar('P')
		time.sleep(.5)
		pH_voltage = float(serialBase.readLine()[:4])
		print(pH_voltage)

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
	temp = serialBase.readLine()[:3] # extract temp voltage
	temp = temp.decode()
	temp = float(temp)
	temp = .1205*temp
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

