# -*- coding: utf-8 -*-
"""
@author: Joshua E. Lambert
"""

from setuptools import setup, find_packages
import os

module_dir = os.path.dirname(os.path.abspath(__file__))

setup(
    name='ccode_replace_python',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    package_data={'ccode_replace_python': ['clthyn.txt']},
    license='MIT',
    description='A package to replace country names with ccodes',
    long_description=open(os.path.join(module_dir, 'README.md')).read(),
    install_requires=[],
    url='https://github.com/JELambert/ccode_replace_python',
    author=['Joshua E. Lambert'],
    author_email=['joshua.lambert@knights.ucf.edu']
)
