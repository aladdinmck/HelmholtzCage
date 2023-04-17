
## Univerity of Georgia Senior Capstone Design

### Abstract

  A Helmholtz cage is a tool that can be used in the testing process of CubeSat Development. The University of Georgia’s Small Satellite Research Laboratory (SSRL) has multiple satellite missions that need to use attitude determination and control systems to properly position themselves in orbit. The Helmholtz Cage is a tool that allows researchers to simulate the environment of space by generating a uniform 3-axis magnetic field. This emulates the magnetic force in orbit that is the main force applied to a satellite that causes the satellite to lose control of its orientation. The Helmholtz cage allows researchers to test their control systems by placing satellites and electronics within the device to experience these forces and perform diagnostics of performance. This can help ensure mission success for a CubeSat, because without this device there is not a physical way of testing the system properly. 
	In our design, there is a full system including the Helmholtz structure, control electronics, and software to properly use the device. The Helmholtz Cage is composed of six 2m by 2m coils in which there are two coils on each axis x, y, and z separated by the radius of the coil. This separation distance of coils creates a uniform magnetic field in a region that is approximately one third of the total volume. Each coil is wrapped 30 times with 14 AWG copper magnet wire in order to produce a magnetic field strength of up to 1.5 Gauss (G) or .00015 Tesla (T). This is enough strength to properly cancel the ambient magnetic field of Earth and create the necessary magnetic field strength experienced in orbit. The system is capable of taking in an orbit description file and then propagating the position of a satellite forward in time by minutes. This allows the researchers to get highly accurate magnetic field changes as if they were in orbit. The power to the system runs through three separate power supplies that are each rated for 30V and 10A leading to the control box. The software controls a high current h-bridge for each axis with pulse width modulation (PWM)  that changes current flow through the coils and therefore creates the necessary magnetic field.  The system then uses triple axis magnetometers to determine the state inside of the cage at any given moment, which is then used through a feedback loop to verify that the system is controlled properly. 

<p align=center>
![CagePicture](/docs/CadCage.png)
</p>
### Team

Members: Evan Lengle, Mujean Kajan, Gareth Thompson, Ethan Grizzle
Sponsor: University of Georgia Small Satellite Research Laboratory <br /r>
Faculty Mentor: Dr. Mark Haidekerr

