from OutputPipeline import PWM
from Sensors import Magnetometer2 as Magnetometer
from OutputPipeline import Pinout
from OutputPipeline import DutyCycle as dc
import time

pins = Pinout.Pins()

pins.set_directions(0,0,0)

mag = Magnetometer.Magnetometer()
mag.setup()
mag.read()
mag.display('G')

initx = 0 - mag.Mx
inity = 0 - mag.My
initz = 0 - mag.Mz
cycles = dc.DutyCycle(initx, inity, initz)
cycles.single_calc()

pins.set_directions(cycles.dir_x,cycles.dir_y,cycles.dir_z)

pwm = PWM.PWM()
pwm.connectI2C()
pwm.set_frequency(2000)
i = 0
start_freq = 3268

while i < 10:
    print("Duty Percent = {}%:".format(i+5))
    pwm.set_DutyCycles(cycles.xDutyCycle,cycles.yDutyCycle,cycles.zDutyCycle)
    time.sleep(5)
    try:
        mag.read()
        mag.display('G')
        diffx = (mag.Mx - initx)*10000
        diffy = (mag.My - inity)*10000
        diffz = (mag.Mz - initz)*10000
        print("Change in X:{}".format(diffx))
        print("Change in Y:{}".format(diffy))
        print("Change in Z:{}".format(diffz))
    except:
        print("ReadFailed")        
    time.sleep(5)
    i += 5
    start_freq += 3268

time.sleep(2)

pwm.set_DutyCycles(0,0,0)
