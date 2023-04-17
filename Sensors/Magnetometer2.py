import board
import time
import adafruit_mlx90393

class Magnetometer:
    def __init__(self):
        self.Mx = []
        self.My = []
        self.Mz = []
        self.SENSOR = None

    def setup(self):
        "Connect board to I2C an set the gain"
        i2c = board.I2C()  # uses board.SCL and board.SDA
        self.SENSOR = adafruit_mlx90393.MLX90393(i2c, gain=adafruit_mlx90393.GAIN_1X)

    def read(self):
        "Read one measurement for each axis in [T]"
        self.Mx, self.My, self.Mz = self.SENSOR.magnetic
        self.Mx = self.Mx*.000001
        self.My = self.My*.000001
        self.Mz = self.Mz*.000001
        if self.SENSOR.last_status > adafruit_mlx90393.STATUS_OK:
            self.SENSOR.display_status()
        time.sleep(1)

    def display(self, unit):
        "Show last Read values 'T' or 'G'"
        if unit == 'T':
            print("X: {} T".format(self.Mx))
            print("Y: {} T".format(self.My))
            print("Z: {} T".format(self.Mz))
        elif unit == 'G':
            self.Mx2 = self.Mx*10000
            self.My2 = self.My*10000
            self.Mz2 = self.Mz*10000
            print("X: {} G".format(self.Mx2))
            print("Y: {} G".format(self.My2))
            print("Z: {} G".format(self.Mz2))
        else:
            print("Please select G or T")
    def status(self):
        "Show the staus of the device"
        self.SENSOR.display_status()
