#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Nikto
   Massrecon module for spider target machines
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


class Nikto:

    def __init__(self, hostname='', ssl_proto=False):

        self.hostname = hostname
        self.module_disable = False
        self.directory_log = False

        self.chr = CherryTree(address=hostname)

        # Load configuration
        self.cfg = Configuration()

        self.config_dir = self.cfg.config_dir

        self.ssl_proto = ssl_proto

        if self.ssl_proto is True:
            self.proto = 'https'
        else:
            self.proto = 'http'

        if self.cfg.config.get('massrecon', 'nikto') != 'True':
            utils.puts('info', 'Nikto module is disabled')
            self.module_disable = True
            return

        if os.path.isfile('/usr/bin/nikto') is False:
            utils.puts('info', 'Nikto is not installed')
            self.module_disable = True
            return

        if self.cfg.config.get('massrecon', 'directory_log') == 'True':
            self.directory_log = True

        if self.cfg.config.get('massrecon', 'cherrytree_log') == 'True':
            self.cherrytree_log = True

        if len(self.hostname) == 0:
            utils.puts('warning', 'No host to scan')
            return

        self.scanfolder = '%s/results/nikto/%s' % (self.config_dir, self.hostname)

        if self.directory_log is True:
            self.nikto_dir = '%s/results/%s/nikto' % (self.config_dir, self.hostname)
            if os.path.isdir(self.nikto_dir) is False:
                os.makedirs(self.nikto_dir, exist_ok=True)

    def scan(self):

        if len(self.ports) == 0:
            return

        color = Colors()

        if self.module_disable is True:
            return

        with Halo(text='%sNikto Spider%s' % (color.blue, color.reset), spinner='dots'):
            try:
                if self.directory_log is True:
                    output = subprocess.getoutput("nikto -host %s://%s -output %s/nikto.txt" % (self.proto, self.hostname, self.nikto_dir))
                else:
                    output = subprocess.getoutput("nikto -host %s://%s" % (self.proto, self.hostname))
            except:
                pass

            print("\n")
            print("%s=%s" % (color.red, color.reset) * 90)
            print("%s Nikto: %s %s" % (color.yellow, self.hostname, color.reset))
            print("%s=%s" % (color.red, color.reset) * 90)
            print('%s%s%s' % (color.green, output, color.reset))
            print("%s-%s" % (color.red, color.reset) * 90)
            print("\n")

        if self.cherrytree_log is True:

            _leaf_name = 'nikto_%s' % time.strftime("%Y%m%d_%H:%M:%S")

            self.chr.insert(name='machines', leaf=self.hostname)
            self.chr.insert(name=self.hostname, leaf=_leaf_name, txt=output)

if __name__ == '__main__':
    pass
