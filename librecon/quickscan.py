#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   quickscan module

   Dependency: you need the quickscan tool to run this module.
   Install like this.

   sudo curl -L https://github.com/mikaelkall/HackingAllTheThings/raw/master/tools/static/linux/x86_64/quickscan -o /usr/local/bin/quickscan && sudo chmod +x /usr/local/bin/quickscan

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


class Quickscan:

    def __init__(self, hostname='', silent=False):

        self.hostname = hostname
        self.module_disable = False
        self.directory_log = False
        self.silent = silent

        self.chr = CherryTree(address=hostname)

        # Load configuration
        self.cfg = Configuration()

        self.config_dir = self.cfg.config_dir

        if self.cfg.config.get('massrecon', 'quickscan') != 'True':
            utils.puts('info', 'quickscan module is disabled')
            self.module_disable = True
            return

        if os.path.isfile('/usr/local/bin/quickscan') is False:
            utils.puts('info', 'quickscan is not installed')
            self.module_disable = True
            return

        if self.cfg.config.get('massrecon', 'directory_log') == 'True':
            self.directory_log = True

        if self.cfg.config.get('massrecon', 'cherrytree_log') == 'True':
            self.cherrytree_log = True

        if len(self.hostname) == 0:
            utils.puts('warning', 'No host to scan')
            return

        self.scanfolder = '%s/results/quickscan/%s' % (self.config_dir, self.hostname)

        if self.directory_log is True:
            self.fullportscan_dir = '%s/results/%s/quickscan' % (self.config_dir, self.hostname)
            if os.path.isdir(self.fullportscan_dir) is False:
                os.makedirs(self.fullportscan_dir, exist_ok=True)

    def run_command(self, command):

        with open("%s/output.txt" % self.fullportscan_dir, "a") as logfile:
            process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(" " + output.strip().decode())
                    logfile.write(" " + output.strip().decode() + '\n')

                    if self.cherrytree_log is True:
                        self.chr.append_data('TCP', output.strip().decode())

            rc = process.poll()
            return rc

    def scan(self):

        color = Colors()

        if self.module_disable is True:
            return

        if self.silent is False:
            utils().puts('success', "Quickscan %s" % self.hostname)

            with Halo(text='%s%s ' % (color.blue, color.reset), spinner='dots'):
                try:
                    if self.directory_log is True:
                        output = self.run_command("quickscan -t %s" % self.hostname)
                        with open(self.fullportscan_dir + '/quickscan.txt', 'w') as logname:
                            logname.write(output)
                    else:
                        output = self.run_command("quickscan -t %s" % self.hostname)
                except:
                    pass
        else:
            try:
                if self.directory_log is True:
                    output = self.run_command("quickscan -t %s" % self.hostname)
                    with open(self.fullportscan_dir + '/quickscan.txt', 'w') as logname:
                        logname.write(output)
                else:
                    output = self.run_command("quickscan -t %s" % self.hostname)
            except:
                pass


if __name__ == '__main__':
    pass
