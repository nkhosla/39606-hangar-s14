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




    def convertAccelerationToPercent(self, pidOutput):


        percent = min(math.fabs(pidOutput),0.999)

        return percent


    def setPercentOfTimeToBeOnState(self,percent):

        # Use the default 20ms = 20000us cycle
        cycleLength = 20000.0
        timeOn_raw = percent * cycleLength

        # round down so no decimals
        timeOn = math.floor(timeOn_raw)


        # Set the servo
        self.servo.set_servo(self.gpioPin, timeOn - (timeOn % 10))


    def respondToPIDSuggestedAccel(self, acc):
        p = self.convertAccelerationToPercent(acc)
        

        if acc<0:
            GPIO.output(self.dirPin, False)
            p = p/2 - ((p/2)%10)

        else:
            GPIO.output(self.dirPin, True)

        self.setPercentOfTimeToBeOnState(p)
        


    def stop(self):
        self.servo.stop_servo()

