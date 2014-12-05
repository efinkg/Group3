import time
import RPi.GPIO as GPIO
import  multiprocessing
from multiprocessing import Process
import motor, button, thermometer, anemometer, led
tmin = 0
tmax = 0
temp_room = 0
buzzed = 1
jobs = []

def readButton():
   while 1:
      if (button.buttonPressed() == 1):
         killAll()

def readAnemometer():
   while 1:
      print anemometer.read()
      led.whatColors(anemometer.read())

def setup():
   GPIO.setwarnings(False)
   temp = thermometer.read_temp()
   global temp_room
   temp_room = temp
   global tmin 
   tmin = temp_room + 0.25
   global tmax 
   tmax = tmin + 0.85
   #motor.motorSpeed(100)
   #motor.stopMotor()
   print "Tmin is "  + str(tmin)
   print "Tmax  is " + str(tmax) 

def tooHot():
   global tmin
   global tmax   
   while 1:
      temp = thermometer.read_temp()
      if (temp > tmin):
         print str(tmin)
         print "Temp is too high"
         if (temp < tmax):
            button.buzzerOff()
            global buzzed
            buzzed = 0
            print "Needs moar air"
            dc = int(85 - (50*(temp-tmin)));
            if(dc <= 0):
              dc = 0.1
         else:
            print "Needs all of the air"
            button.buzzerOn(buzzed)
            global buzzed
            buzzed = 1
            dc = 0.1
         motor.motorSpeed(dc)
      else:
          motor.motorSpeed(100)
          button.buzzerOff()

def killAll():
   motor.motorSpeed(100)
   motor.stopMotor()
   button.buzzerOff()
   GPIO.cleanup()
   for job in jobs:
      job.terminate()

def run():
   try:
      p = Process(target = readAnemometer)
      p2 = Process(target = readButton)
      p3 = Process(target = tooHot)
      jobs.append(p)
      jobs.append(p2)
      jobs.append(p3)
      p.start()
      p2.start()
      p3.start()
      p.join()
      p2.join()
      p3.join()
   except KeyboardInterrupt:
      pass
   killAll()

if __name__ == '__main__':
   GPIO.setwarnings(False)
   setup()
   run()
#   readAnemometer()
   
