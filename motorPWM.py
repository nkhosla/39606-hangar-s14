from RPIO import PWM
import math

class MotorDriverHandler:
    def __init__(self, gpioPin):
        self.servo=PWM.Servo
        self.gpioPin = gpioPin

    def setPercentOfTimeToBeOnState(percent):

        # Use the default 20ms = 20000us cycle
        cycleLength = 20000.0
        timeOn_raw = percent * cycleLength

        # round down so no decimals
        timeOn = math.floor(timeOn_raw)

        # Set the servo
        self.servo.set_servo(self.gpioPin, timeOn)


    def stop(self):
        self.servo.stop_servo()