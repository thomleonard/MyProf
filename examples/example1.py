from antares import *
from MyProf import myprof
import numpy as np

a = []

myprof.point()

for i in range(5):
    a.append(np.ones(100000))
    myprof.point()

print myprof

myprof.plot()
raw_input()

myprof.plot(y='memory')
raw_input()

myprof.plot(y='memory_evolution')
raw_input()

myprof.plot(x='time', y='memory')
raw_input()
 
