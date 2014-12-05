import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pwm = 13
enable = 18
input1 = 5
GPIO.setup(pwm, GPIO.OUT) #PWM
GPIO.setup(enable, GPIO.OUT) #Enable
GPIO.setup(input1, GPIO.OUT) #Input 1
p = GPIO.PWM(pwm, 1000)  # channel=13 frequency=50Hz

def testMotor():
   while 1:
      motorSetup()
      for speed in range(1,100):
          print speed
          runMotor(speed)
          time.sleep(0.1)
          speed = speed + 1
      stopMotor()


def motorSetup():
   GPIO.cleanup()
   GPIO.setmode(GPIO.BCM)
   pwm = 13
   enable = 18
   input1 = 5
   GPIO.setup(pwm, GPIO.OUT) #PWM
   GPIO.setup(enable, GPIO.OUT) #Enable
   GPIO.setup(input1, GPIO.OUT) #Input 1
#If Input1 and PWM are HIGH, forward
#If Input1 LOW and PWM HIGH, backward

def runMotor(dc):
   p = GPIO.PWM(pwm, 100)  # channel=13 frequency=50Hz
   p.ChangeDutyCycle(dc)
   p.start

def stopMotor():
   p.stop()
   GPIO.cleanup()

while True:
    motorSetup()
    testMotor()
    stopMotor()
