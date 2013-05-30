from antares import *
from MyProf import myprof
from example2_func import func

myprof.point()

func()

myprof.point()

print myprof

myprof.plot()
raw_input()

myprof.plot(y='memory')
raw_input()

myprof.plot(x='time', y='memory')
raw_input()
