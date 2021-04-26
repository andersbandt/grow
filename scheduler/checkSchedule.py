import time
import datetime

from envControl.control import *


def checkSensors(cur_time):
  return True

def checkFans(cur_time):
  return True

def checkLights(cur_time):
  return True



def main():
  cur_time = time.time()
  checkSensors(cur_time)
  checkFans(cur_time)
  checkLights(cur_time)
  

if __name__ == "__main__":
  main()
