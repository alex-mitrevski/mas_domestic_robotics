#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['mdr_hri_behaviours'],
    package_dir={'mdr_hri_behaviours': 'ros/src/mdr_hri_behaviours'}
)

setup(**d)