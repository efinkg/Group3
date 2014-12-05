import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

ButtonPin = 27
BuzzerPin = 22
GPIO.setup(ButtonPin,GPIO.IN)
GPIO.setup(BuzzerPin,GPIO.OUT)

prev_input = 0 #Initialize prev_input to 0

''' 
while True:
   GPIO.output(BuzzerPin, False)
   input = GPIO.input(ButtonPin)
   if ((not prev_input) and input): #If we have pushed the button
      print("Bootin pressed")
      GPIO.output(BuzzerPin, True) #Run Buzzer
   prev_input = input   #update previous input
   time.sleep(0.05) #slight pause to debounce
'''
def buttonPressed():
   input = GPIO.input(ButtonPin)
   if (input): #If we have pushed the button
      print("Bootin pressed")
      return 1
   time.sleep(0.05)

def buzzerOn(buzzed):
   if(buzzed == 0):
      GPIO.output(BuzzerPin, True)
      time.sleep(1)   
      buzzerOff()
      print "Brrzap"

def buzzerOff():
   GPIO.output(BuzzerPin, False)
