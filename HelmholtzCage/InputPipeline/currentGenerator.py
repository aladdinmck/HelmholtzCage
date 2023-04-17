import math
import numpy as np
import itertools

class Coil:

    def __init__(self, name, B, N, a, gamma):

        self.Iout = []
        self.Bin = B
        self.N = N
        self.a = a
        self.gamma = gamma
        self.name = name

    def get_current(self):
        mu = 4*math.pi*(10**(-7))
        p = 0
        Io = []
        for i in self.Bin:
            B = self.Bin[p]
            num = B*math.pi*self.a*(1+(self.gamma**2))*((2+(self.gamma**2))**.5)
            den = mu*4*self.N
            I = num/den
            Io.append(I)
            p +=1
        self.Iout = Io
    def single_current(self):
        mu = 4*math.pi*(10**(-7))
        p = 0
        Io = []
        B = self.Bin
        num = B*math.pi*self.a*(1+(self.gamma**2))*((2+(self.gamma**2))**.5)
        den = mu*4*self.N
        I = num/den
        self.Isin = I

    def display(self):
        print('Currents for {} ='.format(self.name))
        print(self.Iout)
