#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   fullportscan module
"""
__author__ = 'kall.micke@gmail.com'

import subprocess
import shlex
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


class Fullportscan:

    def __init__(self, hostname='', silent=False):

        self.hostname = hostname
        self.module_disable = False
        self.directory_log = False
        self.silent = silent

        self.chr = CherryTree(address=hostname)

        # Load configuration
        self.cfg = Configuration()

        self.config_dir = self.cfg.config_dir

        if self.cfg.config.get('massrecon', 'fullportscan') != 'True':
            utils.puts('info', 'fullportscan module is disabled')
            self.module_disable = True
            return

        if os.path.isfile('/usr/bin/fullportscan') is False:
            utils.puts('info', 'fullportscan is not installed')
            self.module_disable = True
            return

        if self.cfg.config.get('massrecon', 'directory_log') == 'True':
            self.directory_log = True

        if self.cfg.config.get('massrecon', 'cherrytree_log') == 'True':
            self.cherrytree_log = True

        if len(self.hostname) == 0:
            utils.puts('warning', 'No host to scan')
            return

        self.scanfolder = '%s/results/fullportscan/%s' % (self.config_dir, self.hostname)

        if self.directory_log is True:
            self.fullportscan_dir = '%s/results/%s/fullportscan' % (self.config_dir, self.hostname)
            if os.path.isdir(self.fullportscan_dir) is False:
                os.makedirs(self.fullportscan_dir, exist_ok=True)

    def run_command(self, command):
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                pass
                print(" " + output.strip().decode())
        rc = process.poll()
        return rc

    def scan(self):

        color = Colors()

        if self.module_disable is True:
            return

        if self.silent is False:
            utils().puts('success', "fullportscan %s" % self.hostname)

            with Halo(text='%s%s ' % (color.blue, color.reset), spinner='dots'):
                try:
                    if self.directory_log is True:
                        output = self.run_command("fullportscan -t %s" % self.hostname)
                        with open(self.fullportscan_dir + '/fullportscan.txt', 'w') as logname:
                            logname.write(output)
                    else:
                        output = self.run_command("fullportscan -t %s" % self.hostname)
                except:
                    pass
        else:
            try:
                if self.directory_log is True:
                    output = self.run_command("fullportscan -t %s" % self.hostname)
                    with open(self.fullportscan_dir + '/fullportscan.txt', 'w') as logname:
                        logname.write(output)
                else:
                    output = self.run_command("fullportscan -t %s" % self.hostname)
            except:
                pass

        if self.cherrytree_log is True:

            _leaf_name = 'fullportscan_%s' % time.strftime("%Y%m%d_%H:%M:%S")

            self.chr.insert(name='machines', leaf=self.hostname)
            self.chr.insert(name=self.hostname, leaf=_leaf_name, txt=output)

if __name__ == '__main__':
    pass
