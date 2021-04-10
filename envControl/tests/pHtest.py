from control import pHControl
from control import pumpControl
from control import sensorControl
import time
import csv

dosing_interval = 1 # amount of time between acid/base additions in minutes
pumpSeconds = 3 # amount of seconds to run the pump each dosing interval
pH_interval = 15 # interval between pH readings in seconds
test_time = 5*60 # total testing time in seconds
pH_readings = int(dosing_interval*60/pH_interval) # number of pH readings between acid/base addition

def main():
	start_time = time.time()
	cur_time = 0
	print("BTW... pH_readings is ", pH_readings)
	doc = open('pHtest_data.csv', 'w')
	writer = csv.writer(doc)
	fields = ['Type', 'Data', 'Timestamp']
	writer.writerow(fields)
	while cur_time < (test_time):
			pumpControl.pumpFluid('acid', pumpSeconds)
			cur_time = time.time() - start_time
			writer.writerow(["Acid", pumpSeconds, cur_time ])

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
				writer.writerow(["EC", TDS, cur_time])
				time.sleep(pH_interval)
				i = i + 1

	doc.close()



if __name__ == "__main__":
	main()
