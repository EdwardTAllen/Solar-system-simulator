import numpy as np

# list of data

deltaT = 3500 # time step in seconds 
time = 0 # initial time of the system


class Particle:
    """
    class Particle - this is a class which creates 
    particle objects to be used in the simulation. 
    It takes in the atributes of a particle: 
    position(pos), velocity(vel), acceleration(acc),
    name of the particle and its mass

    Within the class a particles position and velocity
    over time will be calcualted using the euler and euler chromer
    methods. The acceleration of the particle due to the 
    gravitational interation it has with all the other particles
    in the simulation (in the list particles) will also be calulated.
    """
    def __init__(self, 
    pos=np.array([0, 0, 0], dtype=float), 
    vel=np.array([0, 0, 0], dtype=float), 
    acc=np.array([0, 0, 0], dtype=float),
    name = 'ball',
    mass = 1):
        self.pos= np.array(pos, dtype = float) # position array
        self.vel = np.array(vel, dtype = float) # velocity array
        self.acc = np.array(acc, dtype = float) # acceleration array
        self.name = name # name of the particle used to lable them 
        self.mass = mass # mass of the particle 
        self.G = 6.67408E-11 # gravitational constant G in m^3kg^-1s^-2 (SI)

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
        self.name, self.mass, self.pos, self.vel, self.acc)    

    def euler(self, deltaT):
        '''
        A function that takes the atributes self and deltaT (a small time interval)
        and carries out a singular step of the Euler method where an evolving position(pos)
        and velocity(vel) are generated.
        position by the addition of (deltaT*self.vel) every iteration and 
        velocity by the addition of (deltaT*self.acc) every iteration.
        ''' 
        self.pos += self.vel*deltaT 
        self.vel += self.acc*deltaT

    def euler_cromer(self, deltaT):
        '''
        A function that takes the atributes self and deltaT (a small time interval)
        and carries out a singular step of the Euler-Cromer method where an evolving position(pos)
        and velocity(vel) are generated. This is like the Euler method however the evolving velocity
        this time is calculated before the position.
        position is generated by the addition of (deltaT*self.vel) every iteration and 
        velocity by the addition of (deltaT*self.acc) every iteration.
        ''' 
        self.vel += self.acc*deltaT
        self.pos += self.vel*deltaT

    def updateGravitationalAcceleration(self, particles):
        '''
        A function that takes the atributes self and the list of bodies 'particles'
        and carries out the acceleration due to gravity for a body in 'particles' 
        due to the interaction of the rest of the bodies in 'particles'
        '''
        self.acc = 0 # set initial acceleration
        for i in particles:
            if i.name != self.name: # use the lable of the particle (name) to make sure the particle does get acceleration due to it's self
                r = i.pos - self.pos
                self.acc += ((self.G*(i.mass))/(((np.linalg.norm(r))**2)))*((r)/(np.linalg.norm(r)))
                 # add a new value of acceleration on top of the last each time - iterative 
        return self.acc # function returns the acceleration due to gravity on particle i of the list 'particles'

    def kineticEnergy(self):
        '''
        A function that takes the atributes self and calculates the kinetic energy at a step in time for a particle
        useing the equation for kinetic energy KE = 1/2mv^2'
        '''
        KE = (self.mass*(np.linalg.norm(self.vel))**2)/2
        return KE

    def grav_potential(self, particles):
        for i in particles:
            if i.name != self.name:
                r = i.pos - self.pos
                potential = (-self.G*self.mass*i.mass)//(np.linalg.norm(r))
        return potential 