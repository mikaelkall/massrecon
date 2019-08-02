#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Nmap
   Massrecon module for portscan/vulnscan target machines
"""
__author__ = 'kall.micke@gmail.com'

import subprocess
import time
import os
import re
import signal
import sys

from librecon.configuration import *
from librecon.cherrytree import *
from librecon.utils import *
from halo import Halo
from librecon.colors import *

# Handler to exist cleanly on ctrl+C
def signal_handler(signal, frame):
    print("\nYou pressed Ctrl+C!")
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)


class Nmap:

    def __init__(self, hostname=''):

        self.hostname = hostname
        self.module_disable = False
        self.directory_log = False

        self.chr = CherryTree(address=hostname)

        # Load configuration
        self.cfg = Configuration()

        self.config_dir = self.cfg.config_dir

        if self.cfg.config.get('massrecon', 'nmap') != 'True':
            utils.puts('info', 'Nmap module is disabled')
            self.module_disable = True
            return

        if os.path.isfile('/usr/bin/nmap') is False:
            utils.puts('info', 'Nmap is not installed')
            self.module_disable = True
            return

        if self.cfg.config.get('massrecon', 'directory_log') == 'True':
            self.directory_log = True

        if self.cfg.config.get('massrecon', 'cherrytree_log') == 'True':
            self.cherrytree_log = True

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
        with Halo(text='%sNMAP STAGE[1]%s' % (color.blue, color.reset), spinner='dots'):
            try:
                if self.directory_log is True:
                    output = subprocess.getoutput("nmap -sT -P0 -oA %s/stage1 %s" % (self.nmap_dir, self.hostname))
                else:
                    output = subprocess.getoutput("nmap -sT -P0 %s" % self.hostname)
            except:
                pass

        # Save ports
        regxp = re.compile('([0-9]+)/tcp[ ]+open')
        self.ports = regxp.findall(output)

        print("%s=%s" % (color.red, color.reset) * 90)
        print("%s NMAP_STAGE_1: %s %s" % (color.yellow, self.hostname, color.reset))
        print("%s=%s" % (color.red, color.reset) * 90)

        for port in self.ports:
            utils.puts('success', "%s/tcp open" % port)
        print("%s-%s" % (color.red, color.reset) * 90)

        if self.cherrytree_log is True:
            self.chr.append_data('TCP', output)


    def scan_stage_2(self):

        if len(self.ports) == 0:
            return

        color = Colors()

        if self.module_disable is True:
            return

        # Nmap stage1
        with Halo(text='%sNMAP STAGE[2]%s' % (color.blue, color.reset), spinner='dots'):
            try:
                if self.directory_log is True:
                    output = subprocess.getoutput("nmap -sV -P0 -vv -sC -script-args=unsafe=1 -A -oA %s/stage2 -p %s  %s" % (self.nmap_dir, ','.join(self.ports), self.hostname))
                else:
                    output = subprocess.getoutput("nmap -sV -P0 -vv -sC -script-args=unsafe=1 -A -p %s %s" % (''.join(self.ports), self.hostname))
            except:
                pass

            print("\n")
            print("%s=%s" % (color.red, color.reset) * 90)
            print("%s NMAP_STAGE_2: %s %s" % (color.yellow, self.hostname, color.reset))
            print("%s=%s" % (color.red, color.reset) * 90)
            print('%s%s%s' % (color.green, output, color.reset))
            print("%s-%s" % (color.red, color.reset) * 90)
            print("\n")

        if self.cherrytree_log is True:
            self.chr.append_data('TCP', output)


    def scan_stage_3(self):

        if len(self.ports) == 0:
            return

        color = Colors()

        if self.module_disable is True:
            return

        # Nmap stage1
        with Halo(text='%sNMAP STAGE[3]%s' % (color.blue, color.reset), spinner='dots'):
            try:
                if self.directory_log is True:
                    output = subprocess.getoutput("nmap --script=vuln -oA %s/stage3 -p %s  %s" % (self.nmap_dir, ','.join(self.ports), self.hostname))
                else:
                    output = subprocess.getoutput("nmap --script=vuln -p %s %s" % (''.join(self.ports), self.hostname))
            except:
                pass

            print("\n")
            print("%s=%s" % (color.red, color.reset) * 90)
            print("%s NMAP_STAGE_3: %s %s" % (color.yellow, self.hostname, color.reset))
            print("%s=%s" % (color.red, color.reset) * 90)
            print('%s%s%s' % (color.green, output, color.reset))
            print("%s-%s" % (color.red, color.reset) * 90)
            print("\n")

        if self.cherrytree_log is True:
            self.chr.append_data('TCP', output)

if __name__ == '__main__':
    pass
