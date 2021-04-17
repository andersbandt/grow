import envControl.control.relayBase
import time


intake_pin = 4
outtake_pin = 17


def intakeOn():
	relayBase.relayOn(intake_pin)

def intakeOff():
	relayBase.relayOff(intake_pin)

def outtakeOn():
	relayBase.relayOn(outtake_pin)

def outtakeOff():
	relayBase.relayOff(outtake_pin)




