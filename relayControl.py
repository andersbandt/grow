import RPi.GPIO as GPIO
import time


def relayOn(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 1)


def relayOff(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

relayOn(17)
time.sleep(1)
relayOff(17)

