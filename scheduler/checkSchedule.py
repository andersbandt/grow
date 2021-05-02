import time
import datetime
from databases import *
from envControl.control import *


def stateCheck(area):
	return True


def checkSensors(cur_time):
  return True


def checkFans(cur_time):
  return True


def checkLights(cur_time):
  state_time, state = dataBase.getState("Light") # get state and timestamp of light
	state_time = int(state_time)
	on_time, duration = dataBase.getScheduleParameter("Light")
	print("The light is currently recorded in state: ", state)
	print("The state was last pushed at: ", state_time)
	
	off_time = on_time + duration # calculate the off time
	if (off_time) > 240000:
 		off_time = (on_time + duration) - 240000

	if state: # if the light is on
 		if cur_time > off_time and cur_time < on_time: # if we in the "off" time range
 			lightControl.lightOffStateChange()
	else: # if the light is off
		if cur_time > on_time:
			lightControl.lightOnStateChange()




def checkAll():
  cur_time = datetime.datetime.now()
  cur_time = int(cur_time.strftime('%H%M%S'))
  print("The current time is: ", cur_time)
  checkSensors(cur_time)
  checkFans(cur_time)
  checkLights(cur_time)

if __name__ == "__main__":
  main()
