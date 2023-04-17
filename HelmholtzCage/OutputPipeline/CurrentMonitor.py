import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class CurrentMonitor():
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(i2c)
        self.X_axis = AnalogIn(self.ads, ADS.P0)
        self.Y_axis = AnalogIn(self.ads, ADS.P1)
        self.Z_axis = AnalogIn(self.ads, ADS.P2)
        
    def setGain(self, gain):
        self.ads.gain = gain
        
    def check(self):
        self.Vx = self.X_axis.voltage
        self.Vy = self.Y_axis.voltage
        self.Vz = self.Z_axis.voltage
    def display(self):
        print("X voltage = {} V".format(self.Vx))
        print("Y voltage = {} V".format(self.Vy))
        print("Z voltage = {} V".format(self.Vz))
