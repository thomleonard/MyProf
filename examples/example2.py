from antares import *
from MyProf import myprof
from example2_func import func

myprof.point()

func()

myprof.point()

print myprof

myprof.plot()
myprof.plot(y='memory')
myprof.plot(x='time', y='memory')

