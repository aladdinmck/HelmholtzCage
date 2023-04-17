import pathlib
from sgp4.api import Satrec
from sgp4.api import days2mdhms
from sgp4.api import jday
from astropy.coordinates import TEME, CartesianDifferential, CartesianRepresentation, ITRS
from astropy import coordinates as coord, units as u
from astropy.time import Time
import pandas as pd
import numpy as np
from datetime import datetime
import math
from pathlib import Path

class Orbit:

    def __init__(self, name, test_length, segments):
        self.test_length = test_length
        self.segments = segments
        self.positions = []
        self.name = name

    def generate(self):
        "Propogate the Orbit according to minutes in the future"
        TLEFile = Path(__file__).with_name('tleFile2.txt')
        #TLEFile = '/OrbitPropagation/tleFile.txt'
        TLEs = TLEFile.open('r')
        L_Name = []
        L_1 = []
        L_2 = []
        i = 1

        for line in TLEs:
            j = i
            if i == 1:
                L_Name.append(line)
                j = 2
            elif i == 2:
                L_1.append(line[:69])
                j = 3
            elif i == 3:
                L_2.append(line[:69])
                j = 1
            i = j

        dataframe = pd.DataFrame(columns=['Satellite_name', 'Line_1', 'Line_2', 'Position_vector', 'Speed_vector'])
        dataframe.Satellite_name = L_Name
        dataframe.Line_1 = L_1
        dataframe.Line_2 = L_2
        satellite = []
        print('\n')

        for i in range(len(dataframe)):
            print(dataframe.Satellite_name[i])
            s = dataframe.Line_1[i]
            t = dataframe.Line_2[i]
            satellite = Satrec.twoline2rv(s, t)
            year = satellite.epochyr

            if (year < 57):
                year = year + 2000
            else:
                year = year + 1900

        month, day, hour, minute, second = days2mdhms(satellite.epochyr, satellite.epochdays)
        jd, fr = jday(year, month, day, hour, minute, second)

        t_total = self.test_length
        splits = self.segments
        tsince = t_total // splits

        positions = []

        i = tsince
        while i <= t_total:

            error_code, teme_p, teme_v = satellite.sgp4(jd + i / 1440, fr)

            time = Time(jd + fr + i / 1440, format='jd')
            teme_p = CartesianRepresentation(teme_p * u.km)
            teme_v = CartesianDifferential(teme_v * u.km / u.s)
            teme = TEME(teme_p.with_differentials(teme_v), obstime=time)
            itrs = teme.transform_to(ITRS(obstime=time))

            gcrs = itrs.transform_to(coord.GCRS(obstime=time))
            geocentric = gcrs.transform_to(coord.GeocentricMeanEcliptic(obstime=time))
            p = geocentric.spherical._values
            p = p.tolist()
            positions.append(p)
            i += tsince

        self.positions = positions

        # error_code = non zero error code if satellite position could not be computed from given date,
        # teme_p = satellite position in km from center of the earth in idiosyncratic TEME coordinate frame
        # teme_v = velocity is the rate at which position is changing in km/s

    def display(self):
        print('Geocentric Positions of {}'.format(self.name))
        print(self.positions)
