import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

red = 16
blue = 20
green = 21

GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def chooseColors(red, green, blue):
   try:   
      if (red == 1):
         GPIO.output(red, True)
      if (green == 1):
         GPIO.output(green, True)
      if (blue == 1):
         GPIO.output(blue, True)
      elif (red == 0 and green == 0 and blue == 0):
         GPIO.output(red, False)
         GPIO.output(blue, False)
         GPIO.output(green, False)
   except KeyboardInterrupt:
      print "Fuck you"

def whatColors(anemometer):
   try:
      if (anemometer == 1):
         print "Light up green"
         GPIO.output(red, False)
         GPIO.output(blue, False)
         GPIO.output(green, True)
         time.sleep(1)
      elif (anemometer == 2):
         print "Light up blue"
         GPIO.output(red, False)
         GPIO.output(blue, True)
         GPIO.output(green, False)
         time.sleep(1)
      elif (anemometer == 3):
         print "Light up green and blue"
         GPIO.output(red, False)
         GPIO.output(blue, True)
         GPIO.output(green, True)
         time.sleep(1)
      elif (anemometer == 4):
         print "Light up red"
         GPIO.output(red, True)
         GPIO.output(blue, False)
         GPIO.output(green, False)
         time.sleep(1)
      elif (anemometer == 5):
         print "Light up green and red"
         GPIO.output(red, True)
         GPIO.output(blue, False)
         GPIO.output(green, True)
         time.sleep(1)
      elif (anemometer == 6):
         print "Light up red and blue"
         GPIO.output(red, True)
         GPIO.output(blue, True)
         GPIO.output(green, False)
         time.sleep(1)
      elif (anemometer >= 7):
         print "Light it up!"
         GPIO.output(red, True)
         GPIO.output(blue, True)
         GPIO.output(green, True)
         time.sleep(1)
      else:
         print "gg"
         GPIO.output(red, False)
         GPIO.output(blue, False)
         GPIO.output(green, False)
         time.sleep(1)
   except KeyboardInterrupt:
      pass
   GPIO.output(red, False)
   GPIO.output(blue, False)
   GPIO.output(green, False)

''' 
try:
   while True:
      GPIO.output(red, False)
      GPIO.output(blue, False)
      GPIO.output(green, False)
      time.sleep(0.5)
      GPIO.output(red, False)
      GPIO.output(blue, False)
      GPIO.output(green, True)
      time.sleep(0.5)
      GPIO.output(red, False)
      GPIO.output(blue, True)
      GPIO.output(green, False)
      time.sleep(0.5)
      GPIO.output(red, False)
      GPIO.output(blue, True)
      GPIO.output(green, True)
      time.sleep(0.5)
      GPIO.output(red, True)
      GPIO.output(blue, False)
      GPIO.output(green, False)
      time.sleep(0.5)
      GPIO.output(red, True)
      GPIO.output(blue, False)
      GPIO.output(green, True)
      time.sleep(0.5)
      GPIO.output(red, True)
      GPIO.output(blue, True)
      GPIO.output(green, False)
      time.sleep(0.5)
      GPIO.output(red, True)
      GPIO.output(blue, True)
      GPIO.output(green, True)
      time.sleep(0.5)

except KeyboardInterrupt:
    pass
GPIO.cleanup()

'''
