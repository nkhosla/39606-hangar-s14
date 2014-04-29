from motorPWM import MotorDriverHandler
import time
from RPIO import PWM
import RPi.GPIO as GPIO

handler = MotorDriverHandler(17, 18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

svo = PWM.Servo()

svo.set_servo(17, 18000.0)

while True:
    GPIO.output(18, True)

    """
    svo.set_servo(17, 18000.0)
    GPIO.output(18, False)
    print "switch"
    time.sleep(0.5)
    svo.set_servo(17, 10000.0)
    GPIO.output(18, True)
    """


    