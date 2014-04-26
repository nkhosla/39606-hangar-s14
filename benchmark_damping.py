#!/usr/bin/python

from accel import Accel
import time


accelorometer = Accel()
accelorometer.wakeFromSleep()


start_time = time.time()
for i in range (0,1000):
    print accelorometer.getReadingX()


end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))
