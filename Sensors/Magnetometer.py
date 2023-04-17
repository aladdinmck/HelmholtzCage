# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MLX90393
# This code is designed to work with the MLX90393_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products
from smbus2 import SMBus
import time


class Magnetometer:

    # read in sensor data and cross-check it with Magnetic field calculation values
    def __init__(self):
        self.Mx = []
        self.My = []
        self.Mz = []

    def read(self):
        # address = 0x0C [00001100]
        address = 0x0C
        bus = SMBus(1)

        # Select write register command, 0x60
        # AH = 0x00, AL = 0x5C, GAIN_SEL = 5, Address register (0x00 << 2), set Gain to 5
        config = [0x00, 0x5C, 0x00]
        bus.write_i2c_block_data(address, 0x60, config)
        data = bus.read_byte(address)  # status byte

        # AH = 0x02, AL = 0xB4, RES for magnetic measurement = 0, Address register (0x02 << 2), set resolution to 0
        config = [0x02, 0xB4, 0x08]
        bus.write_i2c_block_data(address, 0x60, config)
        data = bus.read_byte(address)

        # include error handling here

        # Start single measurement mode, X, Y, Z-Axis enabled
        bus.write_byte(address, 0x3E)
        data = bus.read_byte(address)
        time.sleep(0.5)

        # Read data back from 0x4E(78), 7 bytes
        # status, xMag msb, xMag lsb, yMag msb, yMag lsb, zMag msb, zMag lsb
        data = bus.read_i2c_block_data(address, 0x4E, 7)

        # Convert the data [unit:uT]
        # With Gain = 5 and Resolution = 0, uT/LSb = .268 XY and .489 Z
        xMag = data[1] * 256 + data[2]
        if xMag > 32767:
            xMag -= 65536
        yMag = data[3] * 256 + data[4]
        if yMag > 32767:
            yMag -= 65536
        zMag = data[5] * 256 + data[6]
        if zMag > 32767:
            zMag -= 65536

        self.Mx = .268 * xMag * .000001
        self.My = .268 * yMag * .000001
        self.Mz = .489 * zMag * .000001

    def print(self, unit):
        if unit == 'T':
            # Output data to screen
            print("Magnetic Field in X-Axis : %f [T]" % self.Mx)
            print("Magnetic Field in Y-Axis : %f [T]" % self.My)
            print("Magnetic Field in Z-Axis : %f [T]" % self.Mz)
        elif unit == 'G':
            mx = self.Mx * 10000
            my = self.My * 10000
            mz = self.Mz * 10000
            print("Magnetic Field in X-Axis : %f [G]" % mx)
            print("Magnetic Field in Y-Axis : %f [G]" % my)
            print("Magnetic Field in Z-Axis : %f [G]" % mz)
