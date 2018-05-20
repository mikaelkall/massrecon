__author__ = 'nighter@nighter.se'

import os
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name='massrecon',
    version="1.0.0",
    description='This is reconissance tool specific written for OSCP engagements.',
    url='https://github.com/mikaelkall/massrecon.git',
    author='Mikael Kall',
    author_email='nighter@nighter.se',
    packages=['librecon'],

    setup_requires=[
        'halo==0.0.12',
        'configparser==3.5.0'
    ],
    install_requires=[
        'halo==0.0.12',
        'configparser==3.5.0'
    ],
    scripts=['massrecon.py'],
    zip_safe=False
)