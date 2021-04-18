import envControl.control.relayBase as relayBase
import time


intake_pin = 22
outtake_pin = 10


def intakeOn():
	relayBase.relayOn(intake_pin)

def intakeOff():
	relayBase.relayOff(intake_pin)

def outtakeOn():
	relayBase.relayOn(outtake_pin)

def outtakeOff():
	relayBase.relayOff(outtake_pin)




