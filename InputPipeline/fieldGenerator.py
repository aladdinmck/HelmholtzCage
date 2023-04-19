import datetime
from InputPipeline import ppigrf
import matplotlib.pyplot as plt
import itertools
import time

class MagneticField:

    def __init__(self, positions, day, month, year, test_length, segments):
        self.position = positions
        self.Bx = []
        self.By = []
        self.Bz = []
        self.day = day
        self.month = month
        self.year = year
        self.test_length = test_length
        self.segments = segments


    def calculate(self):
        "Calculate Magnetic Field Strengths from the Orbital Positions and date"
        value = 0
        for i in self.position:
            p = self.position[value]
            phi = p[0]
            theta = p[1]
            r = p[2]
            date = datetime.datetime(self.year,self.month, self.day)
            Br, Btheta, Bphi = ppigrf.igrf_gc(r, theta, phi, date)
            Bx = -Btheta *.000000001
            By = Bphi*.000000001
            Bz = -Br*.000000001

            self.Bx.append(Bx)
            self.By.append(By)
            self.Bz.append(Bz)
            value += 1

    def fix_datatype(self):
        "will adjust the output values to not be 3d arrays"
        update = list(itertools.chain.from_iterable(self.Bx))
        self.Bx = list(itertools.chain.from_iterable(update))

        update = list(itertools.chain.from_iterable(self.By))
        self.By = list(itertools.chain.from_iterable(update))

        update = list(itertools.chain.from_iterable(self.Bz))
        self.Bz = list(itertools.chain.from_iterable(update))


        


    def display(self):
        "Function that will output the magnetic field strengths in Each axis in [T]"
        print("\nTheoretical Magnetic Field Values")
        print('Bx = ' + str(self.Bx))
        print('By = ' + str(self.By))
        print('Bz = ' + str(self.Bz) + '\n')

    def plot_fields(self):
        total_time = []
        length = self.segments
        step_size = self.test_length//self.segments
        update  = step_size
        for i in range(0,length):
            total_time.append(update)
            update += step_size

        # This was the old way of plotting
        plt.plot(total_time, self.Bx)
        plt.xlabel("Orbit Propagation (min)")
        plt.ylabel("Magnetic Field Strength (T)")
        plt.title("X Magnetic Field")
        plt.show()
        plt.close()
        plt.plot(total_time, self.By)
        plt.xlabel("Orbit Propagation (min)")
        plt.ylabel("Magnetic Field Strength (T)")
        plt.title("Y Magnetic Field")
        plt.show()
        plt.close()
        plt.plot(total_time, self.Bz)
        plt.xlabel("Orbit Propagation (min)")
        plt.ylabel("Magnetic Field Strength (T)")
        plt.title("Z Magnetic Field")
        plt.show()
        plt.close()



'''
       # This was a new way being tested for the UI
        figure, axis = plt.subplots(2,3)

        axis[0,0].plot(total_time, self.Bx)
        #axis[0,0].plt.xlabel("Orbit Propagation (min)")
        #axis[0,0].ylabel("Magnetic Field Strength (T)")
        axis[0,0].set_title("X Magnetic Field")
        #plot.show()
        #plot.close()
        
        axis[0,1].plot(total_time, self.By)
        #axis[0,1].plt.xlabel("Orbit Propagation (min)")
        #axis[0,1].ylabel("Magnetic Field Strength (T)")
        axis[0,1].set_title("Y Magnetic Field")
        #plot.show()
        #plot.close()
        
        axis[0,2].plot(total_time, self.Bz)
        #axis[0,2].xlabel("Orbit Propagation (min)")
        #axis[0,2].ylabel("Magnetic Field Strength (T)")
        axis[0,2].set_title("Z Magnetic Field")
        plt.xlabel("Orbit Propagation (min)")
        plt.ylabel("Magnetic Field Strength (T)")
        plt.show()
        plt.close()
'''
'''
        # This was the old way of plotting
        plt.plot(total_time, self.Bx)
        plt.xlabel("Orbit Propagation (min)")
        plt.ylabel("Magnetic Field Strength (T)")
        plt.title("Z Magnetic Field")
        plt.show()
        plt.close()
        plt.plot(total_time, self.By)
        plt.xlabel("Orbit Propagation (min)")
        plt.ylabel("Magnetic Field Strength (T)")
        plt.title("Y Magnetic Field")
        plt.show()
        plt.close()
        plt.plot(total_time, self.Bz)
        plt.xlabel("Orbit Propagation (min)")
        plt.ylabel("Magnetic Field Strength (T)")
        plt.title("Z Magnetic Field")
        plt.show()
        plt.close()
'''
