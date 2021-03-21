import sensors
import relayControl
import pumpControl


ideal_pH = 5.7
mL_per_gallon = 15 # recommended addition of solution per gallon
pH_slope = .4 # pH increase for every mL drop/gallon of water
tank_size = 10 # tank size in gallons


if __name__ == "__main__":
	main()


def main():
	pH = sensors.read()
	if pH > 5.5:
		addAcid(pH)
	elif pH < 5.0:
		addBase(pH)



def addBase(pH):
	dif = pH -  ideal_pH
	amount = mL_per_gallon * tank_size
	pumpControl.pumpFluid('base', amount)


def addAcid(pH):
	dif = pH - ideal_pH
	amount = mL_per_gallon * tank_size
	pumpControl.pumpFluid('acid', amount)

