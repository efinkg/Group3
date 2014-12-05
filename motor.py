import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pwm = 13
enable = 18
input1 = 5

def motorEnable():
   p.start(100)
   p.stop()

def motorSpeed(speed):
   p.start(speed)
   p.ChangeDutyCycle(speed)

def stopMotor():
   p.stop()

def stopIt():
   p.stop()
   GPIO.cleanup()

GPIO.setup(pwm, GPIO.OUT) #PWM
GPIO.setup(enable, GPIO.OUT) #Enable
GPIO.setup(input1, GPIO.OUT) #Input 1
#If Input1 and PWM are HIGH, forward
#If Input1 LOW and PWM HIGH, backward

GPIO.output(enable, True) #Enable
GPIO.output(input1, True) #Forward, b/c we're turning on pwm in a hot second

#time.sleep(10)
p = GPIO.PWM(pwm, 100)  # channel=13 frequency=50Hz

#p.start(90)
