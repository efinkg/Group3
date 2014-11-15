import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pwm = 13
enable = 18
input1 = 5

GPIO.setup(pwm, GPIO.OUT) #PWM
GPIO.setup(enable, GPIO.OUT) #Enable
GPIO.setup(input1, GPIO.OUT) #Input 1
#If Input1 and PWM are HIGH, forward
#If Input1 LOW and PWM HIGH, backward

GPIO.output(enable, True) #Enable
GPIO.output(input1, True) #Forward, b/c we're turning on pwm in a hot second

#time.sleep(10)
p = GPIO.PWM(pwm, 50)  # channel=13 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(100, -1, -5):
	    p.ChangeDutyCycle(dc)
            time.sleep(1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
