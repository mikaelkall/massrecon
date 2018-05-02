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
        self.config_dir = '%s/.massrecon' % home
        self.config = configparser.ConfigParser()

        if os.path.isdir(self.config_dir) is False:
            os.makedirs(self.config_dir, exist_ok=True)
            self.create_default_config()

        if os.path.isfile('%s/massrecon.ini' % self.config_dir) is False:
            self.create_default_config()

        self.config.read('%s/massrecon.ini' % self.config_dir)

        if os.path.isdir('%s/results' % self.config_dir) is False:
            os.makedirs('%s/results' % self.config_dir, exist_ok=True)

    def create_default_config(self):

        cfgfile = open('%s/massrecon.ini' % self.config_dir, 'w')
        self.config.add_section('massrecon')
        self.config.set('massrecon', 'cherrytree_log', 'True')
        self.config.set('massrecon', 'directory_log', 'True')
        self.config.set('massrecon', 'nmap', 'True')
        self.config.write(cfgfile)


if __name__ == '__main__':

    pass
    #cfg = Configuration()
    #print(cfg.config.get('massrecon', 'directory_log'))