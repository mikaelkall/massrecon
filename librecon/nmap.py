#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Nmap
   Massrecon module for portscan/vulnscan target machines
"""
__author__ = 'kall.micke@gmail.com'

import subprocess
import re

from configuration import *
from utils import *
from halo import Halo
from colors import *


class Nmap:

    def __init__(self, hostname=''):

        self.hostname = hostname
        self.module_disable = False
        self.directory_log = False

        # Load configuration
        self.cfg = Configuration()

        self.config_dir = self.cfg.config_dir

        if self.cfg.config.get('massrecon', 'nmap') != 'True':
            utils.puts('info', 'Nmap module is disabled')
            self.module_disable = True
            return

        if self.cfg.config.get('massrecon', 'directory_log') == 'True':
            self.directory_log = True

        if len(self.hostname) == 0:
            utils.puts('warning', 'No host to scan')
            return

        self.scanfolder = '%s/results/nmap/%s' % (self.config_dir, self.hostname)

        if self.directory_log is True:
            self.nmap_dir = '%s/results/%s/nmap' % (self.config_dir, self.hostname)
            if os.path.isdir(self.nmap_dir) is False:
                os.makedirs(self.nmap_dir, exist_ok=True)

    def scan_stage_1(self):

        color = Colors()

        if self.module_disable is True:
            return

        # Nmap stage1
        with Halo(text='Nmap stage1', spinner='dots'):
            try:
                if self.directory_log is True:
                    output = subprocess.getoutput("nmap -sT -oA %s/%s %s" % (self.nmap_dir, self.hostname, self.hostname))
                else:
                    output = subprocess.getoutput("nmap -sT %s" % self.hostname)
            except:
                pass
        # Save ports
        regxp = re.compile('([0-9]+)/tcp[ ]+open')
        self.ports = regxp.findall(output)

        print("%s=%s" % (color.red, color.reset) * 40)
        print("%s NMAP_STAGE_1: %s %s" % (color.yellow, self.hostname, color.reset))
        print("%s=%s" % (color.red, color.reset) * 40)

        for port in self.ports:
            utils.puts('success', "%s open" % port)
        print("%s-%s" % (color.red, color.reset) * 40)

if __name__ == '__main__':

    Nmap(hostname='127.0.0.1').scan_stage_1()
