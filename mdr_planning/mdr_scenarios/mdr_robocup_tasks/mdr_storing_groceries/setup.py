#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['mdr_storing_groceries'],
   package_dir={'mdr_storing_groceries': 'ros/src/mdr_storing_groceries'}
)

setup(**d)
