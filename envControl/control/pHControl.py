import envControl
from datetime import datetime
import sqlite3 as lite

ideal_pH = 5.7
lower_range = 5.0
upper_range = 6.0


mL_per_gallon = 15 # recommended addition of solution per gallon
pH_slope = .4 # pH increase for every mL drop/gallon of water
tank_size = 5 # tank size in gallons


if __name__ == "__main__":
	main()


def main():
	return True

def addBase():
	amount = 1
	pumpControl.pumpFluid('base', amount)
	print("Pumped ", amount, "of base to the tank")


def addAcid():
	amount = 1
	pumpControl.pumpFluid('acid', amount)
	print("Pumped ", amount, "of acid to the tank")


def calibratePH():
	return True
