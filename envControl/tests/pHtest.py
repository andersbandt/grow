from .. import pHControl
from .. import pumpControl
from .. import sensorControl
import time

dosing_interval = 10 # amount of time between acid/base additions in minutes
pumpSeconds = 15 # amount of seconds to run the test each dosing interval
pH_interval = 30 # interval between pH readings in seconds
test_time = 30 # total testing time in minutes
pH_readings = dosing_interval*60/pH_interval # number of pH readings between acid/base addition
cur_time = 0 # variable to track current time

def main():
	while cur_time < test_time :
		with open('pHtest_data.txt', 'w') as doc:
			pumpControl.pumpFluid('acid', pumpSeconds)
			f.write(cur_time)
			f.write(

		for i in range(pH_readings):
			sensorControl.readpH()
			time.sleep(pH_interval)




if __name__ == "__main__":
	main()
