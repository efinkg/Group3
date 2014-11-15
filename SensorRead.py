import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

def RCtime(PiPin):
   measurement = 0
   GPIO.setup(PiPin,GPIO.OUT)
   GPIO.setup(PiPin,GPIO.LOW)
   time.sleep(0.1)
   GPIO.setup(PiPin, GPIO.IN)

   while (GPIO.input(PiPin)==GPIO.LOW):
      measurement += 1

   return measurement

while True:
   print RCtime(19)
