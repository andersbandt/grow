import serialBase
import time


def readpH():
        serialBase.sendChar('P')
        time.sleep(.5)
        pH = serialBase.readLine()
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
        temp = serialBase.readLine()
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

