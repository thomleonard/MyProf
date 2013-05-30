import numpy as np
from MyProf import myprof

def func():
   a = []
   for i in range(5):
       a.append(np.ones(100000))
       myprof.point()
 
