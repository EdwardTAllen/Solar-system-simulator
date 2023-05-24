from matplotlib import pyplot as plt
import numpy as np

time_complete = np.load("time_complete.npy", allow_pickle=True)
energy_complete = np.load("energy_complete.npy", allow_pickle=True)

x = time_complete
y = energy_complete
plt.plot(x, y, label='Total energy(J)') 
plt.title('Plot of variance in total energy over time') # create a title 
plt.xlabel('Time (s)') # lable x-axis
plt.ylabel('Total energy (J)') # label y-axis
plt.legend()
plt.show()
