from RPIO import PWM
import RPi.GPIO as GPIO
import math

class MotorDriverHandler:

    def __init__(self, PWMPin, dirPin):
        self.servo=PWM.Servo()
        self.gpioPin = PWMPin
        self.dirPin = dirPin


        GPIO.setmode(GPIO.BCM)

        GPIO.setup(dirPin, GPIO.OUT)




    def convertAccelerationToPercent(self, accel):
        
        scalingFactor = 10.0


        percent = min(math.fabs(accel / scalingFactor), 1)




        return percent


    def setPercentOfTimeToBeOnState(self,percent):

        # Use the default 20ms = 20000us cycle
        cycleLength = 20000.0
        timeOn_raw = percent * cycleLength

        # round down so no decimals
        timeOn = math.floor(timeOn_raw)

        # Set the servo
        self.servo.set_servo(self.gpioPin, timeOn)


    def respondToPIDSuggestedAccel(self, acc):
        p = self.convertAccelerationToPercent(acc)
        self.setPercentOfTimeToBeOnState(p)

        if acc<0:
            GPIO.output(self.dirPin, False)

        else:
            GPIO.output(self.dirPin, True)
        


    def stop(self):
        self.servo.stop_servo()

