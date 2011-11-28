'''
Created on 2011-11-21

@author: Alec
'''
import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
#CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    "nose", #Testing
    "mock", #Testing
    "coverage" #Testing?
    ]
           

from distutils.core import setup
setup(name='MonSer',
      version='0.0.1',
      long_description=README,
      packages=find_packages(),
      py_modules=['clients'],
      install_requires = requires,
      tests_require = requires,
      )