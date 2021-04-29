from envControl.control import pHControl
from envControl.control import pumpControl
from envControl.control import sensorControl
import time
import csv

dosing_interval = 1 # amount of time between acid/base additions in minutes
pumpSeconds = 5 # amount of seconds to run the pump each dosing interval
pH_interval = 10 # interval between pH readings in seconds
test_time = 10*60 # total testing time in seconds
pH_readings = int(dosing_interval*60/pH_interval) # number of pH readings between acid/base addition

def testNutrient():
	start_time = time.time()
	cur_time = 0
	print("BTW... pH_readings is ", pH_readings)
	doc = open('envControl/tests/ECtest_data.csv', 'w')
	writer = csv.writer(doc)
	fields = ['Type', 'Data', 'Timestamp']
	writer.writerow(fields)
	while cur_time < (test_time):
			pumpControl.pumpFluidTimed('nut_1', pumpSeconds)
			cur_time = time.time() - start_time
			writer.writerow(["Nutrient", pumpSeconds, cur_time ])

			i = 0
			for i in range(pH_readings):
				pH = sensorControl.readpH()
				cur_time = time.time() - start_time
				writer.writerow(["pH", pH, cur_time])
				TDS = sensorControl.readTDS()
				cur_time = time.time() - start_time
				writer.writerow(["TDS", TDS, cur_time])
				EC = sensorControl.readEC()
				cur_time = time.time() - start_time
				writer.writerow(["EC", EC, cur_time])
				time.sleep(pH_interval)
				i = i + 1

	doc.close()



if __name__ == "__main__":
	main()
