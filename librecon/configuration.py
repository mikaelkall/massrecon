#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Configuration class
"""
__author__ = 'kall.micke@gmail.com'

import configparser
import os

from utils import *
from pathlib import Path

class Configuration:

    def __init__(self):

        home = str(Path.home())
        if os.path.isdir('%s/.massrecon' % home) is False:
            ## Create folder and add default configuration here
            pass


if __name__ == '__main__':
    Configuration()
