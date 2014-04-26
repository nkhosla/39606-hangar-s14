import smbus
import math

class Accel:
	"""
	A class to access the MPU 6050 acceloromoeter's X acceleration
	"""

	def __init__(self):
		# Power management registers
        self.power_mgmt_1 = 0x6b
        self.power_mgmt_2 = 0x6c

        # the 
        self.address = 0x68
        self.bus - smbus.SMbus(1)



    def wakeFromSleep(self):
        # Now wake the 6050 up as it starts in sleep mode
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)



    # General methods for extracting the data from the register addresses

    def read_word(self, adr):
        high = self.bus.read_byte_data(address, adr)
        low = self.bus.read_byte_data(address, adr+1)
        val = (high << 8) + low
        return val


    def read_word_2c(self, adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
    else:
        return val

    # Get an X accel reading
    def getReadingX(self):

    	xAccel_raw = self.read_word_2c(0x3b)
    	xAccel = xAccel_raw / 16384.0


    	return xAccel