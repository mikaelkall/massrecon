#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Dirb
   Module for spidering target
"""
__author__ = 'kall.micke@gmail.com'

import subprocess
import requests
import shlex
import time
import os
import re
import signal
import sys
import ssl
#import M2Crypto
import OpenSSL

from halo import Halo

try:
    from librecon.configuration import *
    from librecon.cherrytree import *
    from librecon.utils import *
    from librecon.colors import *
except:
    from configuration import *
    from cherrytree import *
    from utils import *
    from colors import *

# Handler to exist cleanly on ctrl+C
def signal_handler(signal, frame):
    print("\nYou pressed Ctrl+C!")
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)


class Dirb:

    def __init__(self, hostname='', ssl_proto=False, silent=False):

        self.hostname = hostname
        self.module_disable = False
        self.directory_log = False
        self.silent = silent

        if self.module_disable is True:
            return

        self.ssl_proto = ssl_proto

        if self.ssl_proto is True:
            self.proto = 'https'
        else:
            self.proto = 'http'

        self.chr = CherryTree(address=hostname)

        # Load configuration
        self.cfg = Configuration()

        self.config_dir = self.cfg.config_dir

        if os.path.isfile('/usr/bin/gobuster') is False:
            utils.puts('info', 'Gobuster is not installed')
            self.module_disable = True
            return

        if self.cfg.config.get('massrecon', 'directory_log') == 'True':
            self.directory_log = True

        if self.cfg.config.get('massrecon', 'cherrytree_log') == 'True':
            self.cherrytree_log = True

        if len(self.hostname) == 0:
            utils.puts('warning', 'No host to spider')
            return

        self.scanfolder = '%s/results/dirb/%s' % (self.config_dir, self.hostname)

        if self.directory_log is True:
            self.dirb_dir = '%s/results/%s/dirb' % (self.config_dir, self.hostname)
            if os.path.isdir(self.dirb_dir) is False:
                os.makedirs(self.dirb_dir, exist_ok=True)

        self.wordlist = self.cfg.config.get('massrecon', 'dirb_wordlist')

    def run_command(self, command):

        with open("%s/output.txt" % self.dirb_dir, "a") as logfile:
            process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(" " + output.strip().decode())
                    logfile.write(" " + output.strip().decode() + '\n')

                    if self.cherrytree_log is True:
                        self.chr.append_data('GoBuster', output.strip().decode())

            rc = process.poll()
            return rc

    def dirb_stage_1(self):

        if self.module_disable is True:
            return

        color = Colors()
        output = ''

        utils().puts('success', "Spider %s://%s" % (self.proto, self.hostname))

        # gobuster spidering
        if self.silent is False:
            with Halo(text='%s%s ' % (color.blue, color.reset), spinner='dots'):

                try:
                    if self.directory_log is True:
                        output = self.run_command("gobuster -k -q -u %s://%s -w %s -x .php,.txt,.sh -t 40 -o %s/dirb_stage1" % (self.proto, self.hostname, self.wordlist, self.dirb_dir))
                    else:
                        output = self.run_command("gobuster -k -q -u %s://%s -w %s -x .php,.txt,.sh -t 40" % (self.proto, self.hostname, self.wordlist))
                except:
                    pass
        else:

            try:
                if self.directory_log is True:
                    output = self.run_command("gobuster -k -q -u %s://%s -w %s -x .php,.txt,.sh -t 40 -o %s/dirb_stage1" % (self.proto, self.hostname, self.wordlist, self.dirb_dir))
                else:
                    output = self.run_command("gobuster -k -q -u %s://%s -w %s -x .php,.txt,.sh -t 40" % (self.proto, self.hostname, self.wordlist))
            except:
                pass

    def special_match(self,strg, search=re.compile(r'[^a-zA-Z0-9_/]').search):
        return not bool(search(strg))


    def robots_scan(self):

        if self.module_disable is True:
            return

        color = Colors()
        output = ''

        try:
            r = requests.get("%s://%s/robots.txt" % (self.proto, self.hostname))
        except:
            utils().puts('error', "Connection failed: %s://%s" % (self.proto, self.hostname))
            return False

        if r.status_code == 200:

            utils().puts('success', "%s://%s/robots.txt" % (self.proto, self.hostname))

            if self.directory_log is True:
                with open("%s/robots.txt" % self.dirb_dir, 'w') as f:
                    f.writelines(r.text)

            if self.cherrytree_log is True:
                _leaf_name = 'robots.txt_%s' % time.strftime("%Y%m%d_%H:%M:%S")
                self.chr.insert(name='machines', leaf=self.hostname)
                self.chr.insert(name=self.hostname, leaf=_leaf_name, txt=r.text)

            entries = [r for r in r.text.split('\n') if ':' in r and 'user-agent:' not in r.lower()]

            for e in entries:
                _folder = str(e.split(':')[1]).strip()

                if self.special_match(_folder) is False:
                    continue

                # Gobuster spidering
                if self.silent is False:

                    with Halo(text='%s%s\n\n' % (color.blue, color.reset), spinner='dots'):

                        _url = "%s://%s%s" % (self.proto, self.hostname, _folder)
                        utils().puts('info', "Spider: %s" % _url)

                        try:
                            if self.directory_log is True:
                                output = self.run_command("gobuster -k -q -u %s -w %s -x .php,.txt,.sh -t 40 -o %s/dirb_%s" % (_url, self.wordlist, self.dirb_dir, _folder.replace('/', '_')))
                            else:
                                output = self.run_command("gobuster -k -q -u %s -w %s -x .php,.txt,.sh -t 40" % (_url, self.wordlist))
                        except:
                            pass
                else:

                    _url = "%s://%s%s" % (self.proto, self.hostname, _folder)
                    utils().puts('info', "Spider: %s" % _url)

                    try:
                        if self.directory_log is True:
                            output = self.run_command("gobuster -k -q -u %s -w %s -x .php,.txt,.sh -t 40 -o %s/dirb_%s" % (
                            _url, self.wordlist, self.dirb_dir, _folder.replace('/', '_')))
                        else:
                            output = self.run_command("gobuster -k -q -u %s -w %s -x .php,.txt,.sh -t 40" % (_url, self.wordlist))
                    except:
                        pass
