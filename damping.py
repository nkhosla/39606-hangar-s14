#!/usr/bin/python

from accel import Accel

accelorometer = Accel()
accelorometer.wakeFromSleep()



while True:
    print accelorometer.getReadingX()