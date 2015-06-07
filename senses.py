import picamera
import os
import microstacknode.gps.l80gps
import microstacknode.accelerometer.mma8452q
from time import sleep
camera = picamera.PiCamera()
accelerometer = microstacknode.accelerometer.mma8452q.MMA8452Q()
accelerometer.init()
def command():
    prompt = input("Command: ")

    if(prompt == "snap"):
        picture();
    elif(prompt == "video"):
        video();
    elif(prompt == "preview"):
        preview();
    elif(prompt == "--help"):
        listhelp();
    elif(prompt == "locate"):
        LatLng();
    elif(prompt == "position"):
        position();
    elif(prompt == "quit"):
        exit()
    else:
        print ("Command not found. Type --help for a list of commands");
        command();
def picture():
    name = input("Name the file: ")
    camera.capture(name + '.png')
    command()
def LatLng():
    amount = input("Running this command requires you to restart the script to exit. Press enter to continue: ");
    if(amount == ""):
      if __name__ == '__main__':
        gps = microstacknode.gps.l80gps.L80GPS()
        while True:
            gpgll = gps.gpgll
            print('latitude:  {}'.format(gpgll['latitude']))
            print('longitude: {}'.format(gpgll['longitude']))
            print()
            sleep(1)
    else:
        print("Press Enter only")
        LatLng();
def position():
    amount = input("Running this command requires you to restart the script to exit. Press enter to continue: ");
    if(amount == ""):
        while True:
            x, y, z = accelerometer.get_xyz()
            print('x: {}, y: {}, z: {}'.format(x, y, z))
            sleep(0.5)
    else:
        print("Press Enter only")
        position(); 
    
def video():
    name = input("Name the recording: ")
    durration = float(input("Length of Recording: "))
    if(int(durration)):
        camera.start_recording(name + '.h264')
        sleep(durration)
        camera.stop_recording()
        convert = input("Would you like to convert this recording? [y/n]")
        if(convert == "y"):
            os.chdir("/home/pi/Desktop");
            os.system('MP4Box -add ' + name +'.h264 '+name+'.mp4');
            command();
        else:
            command();
    else:
        print ("Length is not a number");
        command();
    
def preview():
    time = float(input("How long for the preview."));
    if(time):
        camera.start_preview();
        sleep(time);
        camera.stop_preview();
        command();
    else:
        print("Duration is not float");
        command()
def listhelp():
    print ("snap: takes a still image")
    print ("video: takes a video of a specified duration")
    print ("preview: displays a preview of the camera on the main monitor")
    print ("--help: lists all the commands")
    print ("quit: exits the program")
    print ("locate: gets current location")
    print ("position: gets current x, y, z")
    command();
    if(back == 'q'):
        command();
    else:
        listhelp();
command();

