from motorPWM import MotorDriverHandler
import time
from RPIO import PWM
import RPi.GPIO as GPIO

handler = MotorDriverHandler(17, 18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

svo = PWM.Servo()

svo.set_servo(17, 18000.0 /20000.0)

while True:
    GPIO.output(18, False)
    time.sleep(0.5)
    GPIO.output(18, True)


    