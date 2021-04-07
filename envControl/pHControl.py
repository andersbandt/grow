import sensorControl
import relayBase
import pumpControl
from datetime import datetime
import sqlite3 as lite

ideal_pH = 5.7
lower_range = 5.0
upper_range = 6.0


mL_per_gallon = 15 # recommended addition of solution per gallon
pH_slope = .4 # pH increase for every mL drop/gallon of water
tank_size = 10 # tank size in gallons


if __name__ == "__main__":
	main()


def main():
	con = lite.connect('databases/readings.db')
	pH = sensors.readpH()
	now = datetime.now()
	dt_string = now.strftime("%d//%m/%Y %H:%M:%S")
	with con:
		cur = con.cursor()
		cur.execute("INSERT INTO pH VALUES(dt_string, pH)")
		print("pH value of ", pH, " recorded at ", dt_string, " inserted")
	if pH > upper_range:
		addAcid(pH)
	elif pH < lower_range:
		addBase(pH)


def addBase(pH):
	dif = pH -  ideal_pH
	amount = mL_per_gallon * tank_size
	pumpControl.pumpFluid('base', amount)
	print("Pumped ", amount, "of base to the tank")

def addAcid(pH):
	dif = pH - ideal_pH
	amount = mL_per_gallon * tank_size
	pumpControl.pumpFluid('acid', amount)
	print("Pumped ", amount, "of acid to the tank")
	
def calibratePH():
	

