#!/usr/bin/env python
import serial
import time

# set up serial connection  
ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

serial.flushInput() # flush the input
serial.flushOutput() # flush the output 


def sendChar(char n):
  ser.write(n)
  print("Hello from a function")

def readLine():
  x = ser.readline()
  print(x)
