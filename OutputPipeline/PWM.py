import board
import busio
import adafruit_pca9685


# need to import packages

class PWM:
    def __init__(self):
        self.Z = None
        self.X = None
        self.Y = None
        self.hat = None
        #self.currentX = self.currentX
        #self.currentY = self.currentY
        #self.currentZ = self.currentZ

    def connectI2C(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.hat = adafruit_pca9685.PCA9685(i2c)
        self.X = self.hat.channels[0]
        self.Y = self.hat.channels[1]
        self.Z = self.hat.channels[2]

    def set_frequency(self, freq):

        self.hat.frequency = freq

    def set_DutyCycles(self, x, y, z):
        self.X.duty_cycle = x
        #print('This value is out of range: ' + str(y)) # this was for debugging.
        self.Y.duty_cycle = y
        self.Z.duty_cycle = z

