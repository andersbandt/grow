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
  state, state_time = dataBase.getState("light") # get state and timestamp of light
  timediff = cur_time - state_time
  # find time since interval


def main():
  cur_time = datetime.now()
  cur_time = int(cur_time.strftime('%H%M%S'))
  print(cur_time)
  checkSensors(cur_time)
  checkFans(cur_time)
  checkLights(cur_time)
  

if __name__ == "__main__":
  main()
