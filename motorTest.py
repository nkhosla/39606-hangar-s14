from motorPWM import MotorDriverHandler
import time
from RPIO import PWM
import RPi.GPIO as GPIO

handler = MotorDriverHandler(17, 18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

svo = PWM.Servo()

svo.set_servo(17, 18000.0)

#while True:


"""
    svo.set_servo(17, 18000.0)
    GPIO.output(18, False)
    print "switch"
    time.sleep(0.5)
    svo.set_servo(17, 10000.0)
    GPIO.output(18, True)
"""

while True:
    print "hfv"
    GPIO.output(18, False)
    time.sleep(0.1)
    GPIO.output(18.True)
    time.sleep(0.1)


    