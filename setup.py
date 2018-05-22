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
        'configparser==3.5.0',
        'Paver==1.3.4',
        'M2Crypto==0.30.1',
        'pyOpenSSL==18.0.0',
        'nose==1.3.7',
        'rednose==1.3.0',
        'unittest2==1.1.0',
        'requests==2.13.0'
    ],
    install_requires=[
        'halo==0.0.12',
        'configparser==3.5.0',
        'Paver==1.3.4',
        'M2Crypto==0.30.1',
        'pyOpenSSL==18.0.0',
        'nose==1.3.7',
        'rednose==1.3.0',
        'unittest2==1.1.0',
        'requests==2.13.0'
    ],
    scripts=['massrecon.py'],
    zip_safe=False
)
