from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import os
import sys
from codecs import open

from bittrex import __version__

here = os.path.abspath(os.path.dirname(__file__))


with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()


setup(name='bittrex',
      version=__version__,
      url='https://github.com/thiezn/bittrex-python',
      author='Mathijs Mortimer',
      install_requires=[],
      description='Python3 wrapper around bittrex v1.1 API',
      keywords='bittrex',
      long_description=readme + '\n\n' + history,
      include_package_data=True,
      zip_safe=False,
      platforms='any',
      classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      author_email='mathijs@mortimer.nl',
      license='MIT',
      packages=['bittrex'])
