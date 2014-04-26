#!/usr/bin/python

from accel import Accel
import time
from PID import PID


accelorometer = Accel()
accelorometer.wakeFromSleep()


startTimeForCalibration = time.time()
numReadings = 0
sumReadings= 0

while time.time() < (startTimeForCalibration+10.0):
    numReadings += 1
    sumReadings += accelorometer.getReadingX()


meanReading = 0 - (sumReadings / numReadings)




start_time = time.time()

# Set up the PID control system

pid = PID(P=1, I=1, D=1, Derivator=0, Integrator=0, Integrator_max=50, Integrator_min=-50)


for i in range (0,1000):
    r= accelorometer.getReadingX() + meanReading
    print r, pid.update(r)





end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))
