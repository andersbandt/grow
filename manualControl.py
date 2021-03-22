import lightControl
import fanControl
import pHControl
import pumpControl



if __name__ == __main__:
	main()


# main method to run to gather user input
def main():
	print("Press 1 to control lights")
	print("Press 2 to control fans")
	print("Press 3 to control pH")
	print("Press 4 to control pumps")
	are = int(input("Enter control area number!"))


	if are == 1:
		controlLights()
	elif are == 2:
		controlFans()
	elif are == 3:
		controlPH()
	elif are == 4:
		controlPumps()




def controlLights():
	print("Press 1 to turn light on")
	print("Press 2 to turn light off")
	act = int(input("Enter control action please!"))



def controlFans():
	print("Press 1 to turn intake fan on")
	print("Press 2 to turn intake fan off")
	print("Press 3 to turn outtake fan on")
	print("Press 4 to turn outtake fan off")
	act = int(input("Enter control action please!"))

def controlpH():
	print("Press 1 to add acid")
	print("Press 2 to add base")
	act = int(input("Enter control action please!"))

