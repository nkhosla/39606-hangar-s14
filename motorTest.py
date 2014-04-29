from motorPWM import MotorDriverHandler
import time

handler = MotorDriverHandler(17, 18)

while True:
    handler.respondToPIDSuggestedAccel(9)
    time.sleep(0.5)
