# Helmholtz Cage Software

## Project Summary 
---
A Helmholtz cage is a tool that can be used in the testing process of CubeSat 
Development. The University of Georgia’s Small Satellite Research Laboratory 
(SSRL) has multiple satellite missions that need to use attitude determination 
and control systems to properly position themselves in orbit. The Helmholtz Cage 
is a tool that allows researchers to simulate the environment of space by generating 
a uniform 3-axis magnetic field. This emulates the magnetic force in orbit that is 
the main force applied to a satellite that causes the satellite to lose control of 
its orientation. The Helmholtz cage allows researchers to test their control systems 
by placing satellites and electronics within the device to experience these forces 
and perform diagnostics of performance. This can help ensure mission success for 
a CubeSat, because without this device there is not a physical way of testing the 
system properly. In our design, there is a full system including the Helmholtz structure, 
control electronics, and software to properly use the device. The Helmholtz Cage is 
composed of six 2m by 2m coils in which there are two coils on each axis x, y, and z 
separated by the radius of the coil. This separation distance of coils creates a uniform 
magnetic field in a region that is approximately one third of the total volume. Each 
coil is wrapped 30 times with 14 AWG copper magnet wire in order to produce a magnetic 
field strength of up to 1.5 Gauss (G) or .00015 Tesla (T). This is enough strength to 
properly cancel the ambient magnetic field of Earth and create the necessary magnetic 
field strength experienced in orbit. The system is capable of taking in an orbit 
description file and then propagating the position of a satellite forward in time by 
minutes. This allows the researchers to get highly accurate magnetic field changes 
as if they were in orbit. The power to the system runs through three separate power 
supplies that are each rated for 30V and 10A leading to the control box. The software 
controls a high current h-bridge for each axis with pulse width modulation (PWM) that 
changes current flow through the coils and therefore creates the necessary magnetic field. 
The system then uses triple axis magnetometers to determine the state inside of the cage 
at any given moment, which is then used through a feedback loop to verify that the system 
is controlled properly.

## Installation 
---
This software was designed to operate on a Raspberry Pi 3 B+ or 4. It utilizes Adafruit's 
Circuit Python for which a set up guide can be found 
[here](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi).

Check Python Version is 3.9.7 or newer

```
python --version
```
If you need to update perform the following two commands in the terminal
```
sudo apt update
sudo apt get python3.9
```
The next step is to make sure all other dependencies are intsalled by using the requirements.txt 
file shown below.


```
sudo pip3 install -r path/requirements.txt
```
or
```
sudo pip install -r path/requirements.txt
```
This should set you up to be able to use the proper libraries necessary to operate your Helmholtz Cage.

## Instructions
---
The following will guide you through how to operate the Helmholtz Cage to suit your testing needs and 
customize the parameters necessary for your design.

### Input Pipeline
The input pipeline is designed with tools to generate a simuluated magnetic field across a propagated 
orbit. The Input Pipeline consists of these four parts:

- orbitPropagator
- fieldGenerator
- currentGenerator
- tleFile.txt

### orbitPropagator
The orbit propagation module is used to propagate an orbit into the future by minutes. First create 
an Orbit() class with the name of the satellite as a string along with the length of time to propagate 
(min) and the number of segments. You can change the tleFile with any satellite you want to propagate 
that is similair to your projected orbit. The default is the Spectral Ocean Color Satellite (SPOC) by 
University of georgia's Small Satellite Research laboratory. Go to this [website](https://www.n2yo.com/) 
to find TLE files for current stallites/objects in orbit like the ISS. NOTE: The number of segments must 
be less than or equal to the number of minutes propagated

```
import InputPipeline.orbitPropagator as op

orbit = op.Orbit('SPOC', 90, 45) #Set a 90 minute propagation with 45 time segments with the Orbit() class
orbit.generate() #Use the generate() function to calculate the orbital positions
orbit.display() #Print out the Geocentric Positions

```
### fieldGenerator

The fieldGenerator module takes in the propgated Geocentic positions and converts 
them into magnetic field strengths B calculated in Teslas [T]. This inputs for 
this are the date for when you want the propagation to be in along with the 
calculated positions from the Orbit() class. The input also takes in the 
propagation length and segments like the Orbit() class did. It is used as shown below.

```
import InputPipeline.fieldGenerator as fg

magnetic_fields = fg.MagneticField(Orbit.positions, 1, 1, 2022, 90, 45)
magnetic_fields.calculate()                  # Calculates X, Y, and Z magnetic field strengths
magnetic_fields.fix_datatype()               # Fixes list data types
magnetic_fields.display()                    # Prints field strengths to terminal
magnetic_fields.plot_fields()                # Plot Graphs for each axis

```
### currentGenerator
This module takes in magnetic field values and converts them to the proper current 
values necessary to drive the Helmholtz cage to a proper field strength. There needs 
to be a Coil() object created for each axis in the system. Input the paramters of 
the number of the name, number of turns, alpha (half the side length in m), and 
gamma (distance between coils factor, typically .5-.5445).

```
import InputPipeline.currentGenerator as cg

X = cg.Coil('X-axis', magnetic_field.Bx, 30, 1, .5445)
X.get_current()
X.display()

Y = cg.Coil('Y-axis', magnetic_fields.By, 30, 1, .5445)
Y.get_current()
Y.display()

Z = cg.Coil('Z-axis', magnetic_fields.Bz, 30, 1, .5445)
Z.get_current()
Z.display()
```
### Sensors
The sensors section is used to interface with sensors used for the Helmholtz cage 
system. The main sensor used for the software is the MLX90393 Triaxial Magnetometer. 
Create a a magnetometer object and use its read() as status() functions.

```
import Sensors.Magnetometer as magnetometer

magnetometer = magnetometer.Magnetometer()
magnetometer.setup()                            #Connect the magnetometer to I2C bus
magnetometer.read()                             #Read magneticfields
magnetometer.display()                          #Print the last read values
magnetometer.status()                           #Show the magnetometers status
```

### Output Pipeline

The output pipeline consists of tools necessary to control and output vlaues to the 
Helmholtz cage. The output pipeline consists of the following modules:

- Cage
- Current Monitor
- DutyCycle
- Pinout
- PWM
- User Interface

### Pinout
The pinout class can be used to set the various GPIO pins on a Raspberry Pi. The 
defult pinout uses the proper GPIO  outputs for the system. To change the pins go 
into Pinout.py and chnage the pin numbers and whether they are inputs or outputs. 
Below is a list of the GPIO pins used on a Rapsberry Pi 4 setup.

<div align="center">

| Raspberry Pi Pin  | GPIO Number | Description | Type |
| ----------- | ----------- | ----------- | ----------- |
| Pin 38 | GPIO 20 | FF1_X | INPUT |
| Pin 40 | GPIO 21 | FF2_X | INPUT |
| Pin 15 | GPIO 22 | FF1_Y | INPUT |
| Pin 13 | GPIO 27 | FF2_Y | INPUT |
| Pin 35 | GPIO 19 | FF1_Z | INPUT |
| Pin 37 | GPIO 26 | FF2_Z | INPUT |
| Pin 22 | GPIO 25 | DIR_X | OUTPUT |
| Pin 18| GPIO 24 | DIR_Y | OUTPUT |
| Pin 36 | GPIO 16 | DIR_Z | OUTPUT |
| Pin 29 | GPIO 5 | resetX | OUTPUT |
| Pin 16 | GPIO 23 | resetY | OUTPUT |
| Pin 11 | GPIO 17 | resetZ | OUTPUT |


<div align="left">

An example of setting the pinouts in a program is shown below:
```
import OutputPipeline.Pinout as Pinout

pins = Pinout.Pins()
```
### DutyCycle

Another useful tool to use is the DutyCycle module. This is necessary to produce both 
the direction and duty cycle corresponding to currents generated. For the direction, 
an array of equal size to the current is generated with 1's and 0's with the former 
being the negative direction and the latter positive direction for an axis. The duty 
cycles are calculated by dividing the current values by the LSB value for your system 
which is by default .000144 mA corresponding to a max current of 7.5 A. 
The code exerpt below demonstrates use of this module:

```
import OutputPipeline.DutyCycle as DutyCycle

dutycycles = DutyCycle.DutyCycle(Ix, Iy, Iz)
dutycycles.calculate()
```

### PWM 

To set the PWM values it is quite simple but needs the adafruit_pca9685 to work properly. 
Input the duty cycles generated for each axis and the class will output those accordingly.

```
import OutputPipeline.PWM as PWM

pwm = PWM.PWM()                        
pwm.connectI2C()                        #Connect device to I2C bus
pwm.set_frequency(2400)                 #Set PWM Frequency
pwm.set_DutyCycles(x_duty_cyle, y_duty_cycle, z_duty_cycle) #Set Duty Cycles for each axis

```
### Current Monitor

The current monitor tool allows the user to interface with three current monitors by 
connecting to an external analog to digital converter. The ADC this code uses is the 
4 channel I2C based =ADS1115=. This will read in the correct voltage produced by a 
current monitor that is then converted into currents. This is primarily used for error 
events in the control, but also can be used by implementing them into the control sequence. 

```
import OutputPipeline.CurrentMonitor as cm

monitor = cm.CurrentMonitor()
monitor.gain(16)    #Set the gain type
monitor.check()     #Check the ADC values
monitor.display()   #Print the last read values
```

### Cage

The Cage class is the most important class and is the object that is used to perform the 
complex control algorithms. By initializing a Cage() object, the user needs to input the 
X, Y, and Z values for the Currents and Magnetic Fields along with the test length as before. 
The Cage class contains two main functions first is the calibrate function. This reads a 
magnetometer value from the center of the cage and then actuates currets in the oppsoite 
directions in order to nullify the ambient magnetic field of earth, approximately .2-.6 G. 
The arrays of currents are then biased with this value to ensure the cage satellite is 
experiencing the conditions necessary from the input pipeline propagation. The second function 
is the control() function which starts a for loop that has a nested while looped  timed to 
equate to orbit propagation. If set to max speed it will change values every minute and in 
the meantime it will feedback the magnetometer readings and adjust to the set point. This 
creates a closed loop with P control that can be adjusted for optimal control through 
testing practices.

```
import OutputPipeline.Cage as Cage

system = Cage.Cage(Ix, Iy, Iz, Mx, My, Mz, test_length)  #Initialize Cage
system.calibrate()                                       #Calibrate the system
system.control()                                         # Begin closed loop control sequence

```
### User Interface

## Testing
---
Use the test.py script in the main folder once you are ready to test the setup. It will run 
through a standard oepration sequence using the necessary classes and functions to achieve 
optimal results. 

```
cd path/HelmholtzCage  #find your appropriate folder path

python3 test.py        #run testing script
