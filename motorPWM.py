from RPIO import PWM
import math

class MotorDriverHandler:

    def __init__(self, gpioPin):
        self.servo=PWM.Servo
        self.gpioPin = gpioPin


    def convertAccelerationToPercent(self, accel):
        targetAccel = 0-accel 
        scalingFactor = 10.0

        percent = targetAccel / scalingFactor

        return percent


    def setPercentOfTimeToBeOnState(percent):

        # Use the default 20ms = 20000us cycle
        cycleLength = 20000.0
        timeOn_raw = percent * cycleLength

        # round down so no decimals
        timeOn = math.floor(timeOn_raw)

        # Set the servo
        self.servo.set_servo(self.gpioPin, timeOn)


    def respondToAccel(self, acc):
        p = self.convertAccelerationToPercent(accel)
        self.setPercentOfTimeToBeOnState(p)


    def stop(self):
        self.servo.stop_servo()