from distutils.core import setup
from distutils.core import Extension

setup(name='jenkins',
      version='1.0',
      description="Python ctypes wrapper around Bob Jenkins' hash functions.",
      author="John Evans",
      author_email="john@milo.com",
      url="http://github.com/lgastako/jenkins/",
      py_modules=['jenkins'],
      ext_modules=[Extension('lookup3', ['lookup3.c'])],
      )
