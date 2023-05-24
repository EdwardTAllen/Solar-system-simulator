README

This project provides a simulation of a N-body system, where gravity between
N number of particles is modeled and the interaction of all bodies involved
can be observed. Here it is modeled as an example to simulate several planets
within the solar system and how they gravitationally interact with the sun.

FILES CONTAINED

The files contained are as follows: 'Simulation.py', this is where the main 
loop of the program is stored, generating the positions of the particles over
time, as well as where the desired planetory bodies are defined. The data is 
also saved to several .npy files.
'Particle.py' is where the Particle class is held which allows the generation
of a particle object defining many parameters and updating the acceleration
due to gravity on that object.
'plot.py' is a script which takes in the .npy data files of the N-body 
simulation and plots their motion accordingly on a 2D graph.
'plotEnergy.py' takes in the .npy data files and provides a plot of the total
energy in the system over time.


RUNNNING THE SIMULATION

First run 'Simulation.py'
To generate a plot of some of the planets in the solar system run 'plot.py'
To generate a plot of energy conservation run 'plotEnergy.py'

GIT HUB LINK

The main files can be found here:
https://github.com/EdwardTAllen/Solar-system-simulator
