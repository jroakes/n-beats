import os

from setuptools import setup

BASE_VERSION = '1.3.2'  # update regardless whether you update keras or pytorch or both.

# common packages.
INSTALL_REQUIRES = [
    'numpy>=1.18.1',
    'pandas>=0.25.3',
    'matplotlib>=3.0'
]

LIB_PACKAGE = ['nbeats_pytorch']
INSTALL_REQUIRES.extend([
    'torch'    
])

setup(
    name='nbeats-pytorch',
    version=BASE_VERSION,
    description='N-Beats',
    author='Philippe Remy (Pytorch), Jean Sebastien Dhr (Keras)',
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    packages=LIB_PACKAGE,
    install_requires=INSTALL_REQUIRES
)
