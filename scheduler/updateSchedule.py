import time
import datetime
import databases.dataBase as dataBase
from envControl.control import *


# updateParameter: updates a control area's parameters in the database
# inputs: flag - boolean for if inputs are being passed or not;
#   area - control area; num - parameter number; value - value in parameter
# outputs: none
def updateSchedule(flag, *args):
	if flag == 1: # if inputs are being passed
		True

	elif flag == -1: # if no inputs are being passed, prompt user
		area_num = int(input("Would you like to update: 1-Lights, 2-Outtake, 3-Intake, 4-Air pump, 5-Water pump"))

	if area_num == 1: # set light schedule
		area = "Light"
		num = int(input("Two options: 1-Time that light turns on, 2-Duration light is on"))
		value = int(input("Please enter the desired parameter value"))
	elif area_num == 2: # update outtake schedule
		area = "Outtake"
		num = int(input("Two options: 1-Duration fan is on, 2-Duration fan is off"))
		value = int(input("Please enter the desired parameter value"))
	elif area_num == 3: # update intake schedule
		area = "Intake"
		num = int(input("Two options: 1-Duration fan is on, 2-Duration fan is off"))
		value = int(input("Please enter the desired parameter value"))

	else:
		print("Invalid flag sent")
		return False

	dataBase.updateScheduleParam(area, num, value)
	return True



def main():
  return True

if __name__ == "__main__":
  main()
