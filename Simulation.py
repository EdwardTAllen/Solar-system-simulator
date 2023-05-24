#imports
import numpy as np # import numpy to create arrays 
from Particle import Particle # import the particle class
from matplotlib import pyplot as plt # import matplotlib so a plot can be created 
import copy
# variables - all units are SI

#planet distances from the sun (m)
distance_mars_sol = 228000000000
distance_earth_sol = 150000000000 
distance_venus_sol = 108000000000

deltaT = 3500 # time step in seconds 
iterations =  20000 # amoun tof times the code is ran
time = 0 # initial time of system 

# The sun initial data
solMass = 1.9885e30 
solRadius = 696500000 
# Earth initial data 
earthMass = 5.97237e24
earthPos = solRadius + distance_earth_sol # distance from the centre of the sun to the centre of earth 
earthVel = 29780
# Mars initial data 
marsMass = 6.4171e23 
marsPos = solRadius + distance_mars_sol
marsVel = 24139 
# Venus initial data
venusMass = 4.8685e24 
venusPos = solRadius + distance_venus_sol
venusVel = 35021

# The sun as a object 'Particle'
sol = Particle((np.array([0, 0, 0],dtype=float)), 
(np.array([0, 0, 0],dtype=float)), 
(np.array([0, 0, 0],dtype=float)), 
'sol', 
solMass)

# The Earth as a object 'Particle'
earth = Particle((np.array([earthPos, 0, 0],dtype=float)), 
(np.array([0, earthVel, 0],dtype=float)), 
(np.array([0, 0, 0],dtype=float)), 
'earth', 
earthMass)

# Mars as a object 'Particle'
mars = Particle((np.array([marsPos, 0, 0],dtype=float)), 
(np.array([0, marsVel, 0],dtype=float)), 
(np.array([0, 0, 0],dtype=float)), 
'mars', 
marsMass)

# Venus as a object 'Particle'
venus = Particle((np.array([venusPos, 0, 0],dtype=float)), 
(np.array([0, venusVel, 0],dtype=float)), 
(np.array([0, 0, 0],dtype=float)), 
'venus', 
venusMass)

particles = [sol, earth, mars, venus] # list of particles to be used in the simulation

# simulation code 

# create output container for each body
Data = []
energy_complete = []
time_complete = []  # time + deltaT each time (cumaltive)
flag_intevals = 100 # intervals that data is collected at 
energyK = 0 # initial energy 
energyP = 0

for i in range(0, int(iterations)):
    for p in particles:
        p.updateGravitationalAcceleration(particles)
        p.euler(deltaT)
        if i % flag_intevals == 0:
            Data.append([copy.deepcopy(p.pos[0]), copy.deepcopy(p.pos[1])]) 
    for p in particles:
        if i % flag_intevals == 0:
            time += deltaT # increase time by deltaT
            time_complete.append(time) # create list of time going up in increments of deltaT
            energyK = p.kineticEnergy() # kinetic energy
            energyP = p.grav_potential(particles) # potential energy
            energy_complete.append(energyK + energyP) # energyK + energyP is total energy 
 

complete_x = [] # list of just x coordiantes
complete_y = [] # list of just y coordinates 

Data_len = len(Data) # number of entries in data 
for i in range(0, Data_len):
    complete_x_entry = Data[i][0]
    complete_x.append(complete_x_entry)
    complete_y_entry = Data[i][1]
    complete_y.append(complete_y_entry)

# save data to files 
np.save("complete_x", complete_x, allow_pickle=True)
np.save("complete_y", complete_y, allow_pickle=True)
np.save("energy_complete", energy_complete, allow_pickle=True)
np.save("time_complete", time_complete, allow_pickle=True)

