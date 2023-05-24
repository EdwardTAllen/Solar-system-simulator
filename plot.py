from Simulation import particles 
from matplotlib import pyplot as plt # import matplotlib so a plot can be created 
from Particle import Particle # import the particle class
import numpy as np # import numpy to create arrays 

complete_x = np.load("complete_x.npy", allow_pickle=True)
complete_y = np.load("complete_y.npy", allow_pickle=True)

for i in range(0, len(particles)):
    i_x = complete_x[(i)::len(particles)] # x coordiantes for one of the particles i
    i_y = complete_y[(i)::len(particles)] # y coordinates for one of the particles i
    plt.plot(i_x, i_y, label = particles[i].name) # plot x and y coordinates for one of the particles i
plt.title('Plot of n-particles for the Euler method') # create a title 
plt.xlabel('Position(m)') # lable x-axis
plt.ylabel('Position(m)') # label y-axis
plt.legend() # create legend
plt.show()