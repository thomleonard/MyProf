#import resource
import os
import inspect
import numpy as np
import datetime
from antares.api.Base import Base
from antares.api.Zone import Zone
from antares.api.Instant import Instant
from antares.treatment.Treatment import Treatment

class MyProf():
    def __init__(self):
        self.time = [] 
        self.memory = []
        self.location = [] 
 
    def point(self, location=None):
        time = self.get_time()
        self.time.append(time)
        if location is not None: 
            self.location.append(str(location))
        else:
            fname, line = self.get_location()      
            self.location.append('%s : %s' % (fname, line))
        mem = self.get_memory()
        self.memory.append(mem)

    def get_location(self):
        callerframerecord = inspect.stack()[2]
        frame = callerframerecord[0]
        info = inspect.getframeinfo(frame)
        fname = info.filename
        line = info.lineno
        return fname, line

    def get_memory(self):
        return int(os.popen('ps -p %d -o rss | tail -1' % os.getpid()).read()) / 1000.
#        usage = resource.getrusage(resource.RUSAGE_SELF)
#        mem = usage[2] * resource.getpagesize() / 1000000.      
        return mem

    def get_time(self):
        return datetime.datetime.now()

    def __str__(self):
        memory = ['%.2f' % mem for mem in np.array(self.memory)]# - self.memory[0]]
        time = [str(dt - self.time[0]) for dt in self.time] 

        mem_max = max(map(len, memory))
        tim_max = max(map(len, time))
        pnt_max = max(5, len(str(len(time))))
     
        output = '%s   %s  %s  %s\n' % ('Point'.ljust(pnt_max), 'Time'.ljust(tim_max - 2), 'Mem (Mb)'.rjust(mem_max + 2), 'Location')
        output += '=' * len(output) + '\n'  
        for idx, loc in enumerate(self.location):
            output += '%s %s  %sMb  %s\n' % (str(idx).ljust(pnt_max), time[idx].ljust(tim_max), memory[idx].rjust(mem_max), loc)
        return output
 
    def __repr__(self):
        return self.__str__()

    def plot(self, x='points', y='time'):
        b = Base()
        b['0'] = Zone()
        b[0]['0'] = Instant()
        b[0][0]['time'] = [(dt - self.time[0]).total_seconds() for dt in self.time]
        b[0][0]['memory'] = np.array(self.memory)# - self.memory[0]
        b[0][0]['points'] = np.arange(len(self.time))

        t = Treatment('plot')
        t['base'] = b[:, :, (x, y)]
        t['legend'] = False
        t.execute()

        # raw_input()

myprof = MyProf() 
