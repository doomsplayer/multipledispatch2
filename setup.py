#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import multipledispatch

setup(name='multipledispatch2',
      version=multipledispatch.__version__,
      description='Multiple dispatch',
      url='http://github.com/doomsplayer/multipledispatch/',
      author='Young Wu',
      author_email='doomsplayer@gmail.com',
      license='BSD',
      keywords='dispatch',
      packages=['multipledispatch'],
      long_description=(open('README.md').read() if exists('README.md')
                        else ''),
      zip_safe=False)
