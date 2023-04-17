from InputPipeline import orbitPropagator as op
from InputPipeline import currentGenerator as cg
from InputPipeline import ppigrf
from InputPipeline import fieldGenerator as fg
from OutputPipeline import DutyCycle
from OutputPipeline import PWM
from OutputPipeline import Cage
import time

day = 2
month = 2
year = 2023
test_length = 4
segments = 4

test = op.Orbit('ISS', test_length, segments)
test.generate()
test.display()
print(len(test.positions))

mag = fg.MagneticField(test.positions, day, month, year, test_length, segments)
mag.calculate()
mag.fix_datatype()
mag.display()
mag.plot_fields()

'''
currentGenerator code that takes in magnetic field values and converts them to
the proper current values necessary to drive the Helmholtz cage to a proper field
strength. There needs to be a Coil() object created for each axis in the system.
Input the parameters of the number of the name, number of turns, alpha (half the
the side length in m), and gamma(distance between coils factor, typically [.5, .5445]).
'''

'''
let's see what happens when we uncomment #X.display() and #Y.display() and #Z.display()
(this makes the test stop and it gets stuck)
'''

X = cg.Coil('X-axis', mag.Bx, 30, 1, .5445)
X.get_current()
#X.display()

Y = cg.Coil('Y-axis', mag.By, 30, 1, .5445)
Y.get_current()
#Y.display()

Z = cg.Coil('Z-axis', mag.Bz, 30, 1, .5445)
Z.get_current()
#Z.display()

cage = Cage.Cage(X.Iout, Y.Iout, Z.Iout,mag.Bx,mag.By, mag.Bz, test_length)

print("Calibrate 1")
cage.calibrate()
#print("Calibrate 2")
#print("Starting Simulation for: {}".format('SPOC'))
cage.control()
#cage.control()
cage.off()
