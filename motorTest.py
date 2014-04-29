from motorPWM import MotorDriverHandler

handler = MotorDriverHandler(17, 18)

while True:
    handler.respondToPIDSuggestedAccel(10)
    sleep(0.5)
