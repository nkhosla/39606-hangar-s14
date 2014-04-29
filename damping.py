#!/usr/bin/python

from accel import Accel
from PID import PID
from motorPWM import MotorDriverHandler
import time

# train the accelorometer
startTimeForCalibration = time.time()
numReadings = 0
sumReadings= 0

trainingAccel = Accel(0)
trainingAccel.wakeFromSleep()

while time.time() < (startTimeForCalibration+4.0):
    sumReadings += trainingAccel.getReadingX()
    numReadings += 1


meanReading = 0 - (sumReadings / numReadings)

# Set up the accelorometer
accelorometer = Accel(meanReading)
accelorometer.wakeFromSleep()

# Set up the PID control system

pid = PID(P=3, I=0, D=0, Derivator=0, Integrator=0, Integrator_max=50, Integrator_min=-50)


# Set up the motor driver handler
mdHandler = MotorDriverHandler(17,18)

while True:
    r= accelorometer.getReadingX()
    pidOutput = pid.update(r)
    mdHandler.respondToPIDSuggestedAccel(pidOutput)

    t = mdHandler.convertAccelerationToPercent(pidOutput)

   # print r, t