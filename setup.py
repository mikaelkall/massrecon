__author__ = 'nighter@nighter.se'

import os
import subprocess
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

# Fetch version from git tags, and write to version.py.
# Also, when git is not available (PyPi package), use stored version.py.
version_py = os.path.join(os.path.dirname(__file__), 'version.py')

try:
    version_git = subprocess.getoutput("/usr/bin/git ls-remote -q --tags 2>/dev/null | awk '{print $2}' |egrep -o '[0-9]+.[0-9]+.[0-9]+' |sort -g |tail -1").rstrip()
    if len(version_git) == 0:
        raise Exception('git describe failed to execute reason: %s' % o[1])
except Exception:
    with open(version_py, 'r') as fh:
        version_git = fh.read().strip().split('=')[-1].replace('"', '')

version_msg = "# Do not edit this file"
with open(version_py, 'w') as fh:
    fh.write(version_msg + os.linesep + "__version__ = '" + version_git + "'")

setup(
    name='massrecon',
    version="{ver}".format(ver=version_git),
    description='This is reconissance tool specific written for OSCP engagements.',
    url='https://github.com/mikaelkall/massrecon.git',
    author='Mikael Kall',
    author_email='nighter@nighter.se',
    packages=['librecon', 'oscp'],

    setup_requires=[
        'halo==0.0.28',
        'configparser==3.5.0',
        'Paver==1.3.4',
        'pyOpenSSL==18.0.0',
        'nose==1.3.7',
        'rednose==1.3.0',
        'unittest2==1.1.0',
        'requests==2.31.0',
        'python-docx==0.8.10'
    ],
    install_requires=[
        'halo==0.0.28',
        'configparser==3.5.0',
        'Paver==1.3.4',
        'pyOpenSSL==18.0.0',
        'nose==1.3.7',
        'rednose==1.3.0',
        'unittest2==1.1.0',
        'requests==2.31.0',
        'python-docx==0.8.10'
    ],
    scripts=['massrecon.py', 'version.py'],
    zip_safe=False
)
