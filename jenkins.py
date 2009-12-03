import os

from ctypes import cdll
from ctypes import c_int
from ctypes import byref

from distutils.sysconfig import get_python_lib

lookup3 = cdll.LoadLibrary(os.path.join(get_python_lib(), "lookup3.so"))


def hashlittle(s, seed=0):
    return lookup3.hashlittle(s, len(s), seed)


def hashlittle2(s, seed1=0, seed2=0):
    init_val1 = c_int(seed1)
    init_val2 = c_int(seed2)
    lookup3.hashlittle2(s, len(s), byref(init_val1), byref(init_val2))
    return init_val1.value, init_val2.value
