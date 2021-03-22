import relayBase
import time


intake_pin = 4
outtake_pin = 17


def intakeOn():
	relayControl.relayOn(intake_pin)

def intakeOff():
	relayControl.relayOff(intake_pin)

def outtakeOn():
	relayControl.relayOn(outtake_pin)

def outtakeOff():
	relayControl.relayOff(outtake_pin)




