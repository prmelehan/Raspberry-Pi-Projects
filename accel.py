import time
#comment the lines below to run the script when not on a Raspberry Pi
import microstacknode.accelerometer.mma8452q

accelerometer = microstacknode.accelerometer.mma8452q.MMA8452Q()
accelerometer.init()
#Stop commenting here
def command():
    prompt = input("Command: ")
    if(prompt == "velocity"):
        velocity();
    elif(prompt == "speed"):
        speed();
    elif(prompt == "accel"):
        accel();
    elif(prompt == "position"):
        position();
    elif(prompt == "--help"):
        listhelp();
    elif(prompt == "quit"):
        exit();
    else:
        print("Command not found. Type --help for a list of commands");
        command();

def velocity():
	#A function that prints the velocity
	
def position():
	x, y, z = accelerometer.get_xyz()
    print('x: {}, y: {}, z: {}'.format(x, y, z))
	command();
def listhelp():
    print ("--help:   lists all the commands")
    print ("quit:   exits the program")
    print ("locate:   gets current location")
    print ("position:   gets current x, y, z")
    command();
command();