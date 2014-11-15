import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

red = 16
blue = 20
green = 21

GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

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
