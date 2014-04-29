#!/usr/bin/python

from accel import Accel
from PID import PID
from motorPWM import MotorDriverHandler

# Set up the accelorometer
accelorometer = Accel()
accelorometer.wakeFromSleep()

# Set up the PID control system

pid = PID(P=250, I=0, D=0, Derivator=0, Integrator=0, Integrator_max=50, Integrator_min=-50)


# Set up the motor driver handler
mdHandler = MotorDriverHandler(17,18)

while True:
    r= accelorometer.getReadingX()
    pidOutput = pid.update(r)
    #mdHandler.respondToPIDSuggestedAccel(pidOutput)
    t = mdHandler.convertAccelerationToPercent(pidOutput)

    print r, t