"""
Cython for days needing it
"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('y2024/days/day04c.pyx'),
)
