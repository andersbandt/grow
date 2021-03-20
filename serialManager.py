#!/usr/bin/env python
import serial
import time

# set up serial connection

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=10
)


#ser.flushInput() # flush the input
#ser.flushOutput() # flush the output


def sendChar(char):
  	ser.write(char)
  	print("Hello from a function")
	time.sleep(.5)

def readLine():
	x = ser.readline()
	print(x)
	return x
