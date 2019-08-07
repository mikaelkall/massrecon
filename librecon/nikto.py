#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Nikto
   Massrecon module for spider target machines
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

    def run_command(self, command):
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        i = 0
        while True:
            i += 1
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(" " + output.strip().decode())

                if self.cherrytree_log is True:
                    self.chr.append_data('Nikto', output.strip().decode())

            if i > 900000:
                break

        rc = process.poll()
        return rc

    def scan(self):

        color = Colors()

        if self.module_disable is True:
            return

        utils().puts('success', "Nikto %s://%s" % (self.proto, self.hostname))

        with Halo(text='%s%s ' % (color.blue, color.reset), spinner='dots'):
            try:
                if self.directory_log is True:
                    output = self.run_command("nikto -host %s://%s -output %s/nikto.txt" % (self.proto, self.hostname, self.nikto_dir))
                else:
                    output = self.run_command("nikto -host %s://%s" % (self.proto, self.hostname))
            except:
                pass


if __name__ == '__main__':
    pass
