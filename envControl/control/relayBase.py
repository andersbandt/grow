import RPi.GPIO as GPIO
import time

# sets a certain relay off by setting the output pin high
def relayOff(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 1)

# sets a certain relay on by setting the output low
def relayOn(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)


