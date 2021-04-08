from .. import pHControl
from .. import pumpControl
from .. import sensorControl



pH_interval = 30 # interval between pH readings in seconds
dosing_interval = 10 # interval between acid/base additions in minutes

pH_readings = dosing_interval*60/pH_interval # number of pH readings between acid/base addition


def main():
	while True:
		pumpControl.pumpFluid('acid', 10)

		for i in range(pH_readings):
			sensorControl.readpH()
			time.sleep(pH_interval)




if __name__ == "__main__":
	main()
