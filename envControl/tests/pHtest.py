from control import pHControl
from control import pumpControl
from control import sensorControl
import time

dosing_interval = 5 # amount of time between acid/base additions in minutes
pumpSeconds = 20 # amount of seconds to run the pump each dosing interval
pH_interval = 15 # interval between pH readings in seconds
test_time = 30*60 # total testing time in seconds
pH_readings = int(dosing_interval*60/pH_interval) # number of pH readings between acid/base addition

def main():
	start_time = time.time()
	cur_time = 0
	print("BTW... pH_readings is ", pH_readings)
	doc = open('pHtest_data.txt', 'w')
	while cur_time < (start_time + test_time):
			pumpControl.pumpFluid('acid', pumpSeconds)
			cur_time = time.time()
			doc.write(str(cur_time - start_time) + '\n')
			doc.write("Acid: " + str(pumpSeconds) + '\n')

			i = 0
			for i in range(pH_readings):
				pH = sensorControl.readpH()
				cur_time = time.time()
				doc.write(str(cur_time - start_time) + '\n')
				doc.write(str(pH) + '\n')
				time.sleep(pH_interval)
				i = i + 1

	doc.close()



if __name__ == "__main__":
	main()
