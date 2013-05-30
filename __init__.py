import os
import subprocess

__all__ = []
VERSION = '0.1'

MyProf_file = __import__('MyProf', globals(), locals(), ['MyProf'])
MyProf = MyProf_file.MyProf
myprof = MyProf_file.myprof
__all__ += ['myprof', 'MyProf']

# versioning using GIT if available
path = os.path.abspath('')
os.chdir(os.path.dirname(__file__))
try:
    CMD = ("git", "describe", "--tags", "--dirty", "--always")
    FNULL = open('/dev/null', 'w')
    GIT_PROCESS = subprocess.Popen(CMD, stdout=subprocess.PIPE, stderr=FNULL)
    GIT_PROCESS.wait()
    __version__ = GIT_PROCESS.stdout.read().strip()
    if not __version__:
        __version__ = VERSION
    else:
        __version__ = __version__.replace('0.0', VERSION)
    del CMD, FNULL, GIT_PROCESS
except OSError:
    __version__ = VERSION
del VERSION
os.chdir(path)
