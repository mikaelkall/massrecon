#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  massrecon
  Automate recognisance and updates CherryTree
"""

import sys
import os
import signal

from librecon.librecon import *
from version import __version__

sys.path.insert(1, os.path.join(sys.path[0], '../'))

__author__ = 'kall.micke@gmail.com'

# Handler to exist cleanly on ctrl+C
def signal_handler(signal, frame):
    print("\nYou pressed Ctrl+C!")
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)


def __usage():
    print("""Massrecon %s ( http://blog.nighter.se/blog/2019/08/13/massrecon-released/ )
Usage: massrecon [OPTIONS]

General Options

       recon  <ip>\tStart recon target

   [Modules]

        nmap  <ip>\tRun nmap module only
        dirb  <ip>\tRun dirb module only
       nikto  <ip>\tRun nikto module only
         ftp  <ip>\tRun ftp module only
      sslyze  <ip>\tRun sslyze module only
   quickscan  <ip>\tRun quick portscan on all ports.
""" % __version__)

    sys.exit(0)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        __usage()

    try:
        opt = sys.argv[1].strip()
        ip = sys.argv[2].strip()
    except:
        __usage()

    if opt.lower() == "recon":
        Librecon().run(ip=ip)
        sys.exit(0)

    elif opt.lower() == "nmap":
        Librecon().nmap(ip=ip)
        sys.exit(0)

    elif opt.lower() == "dirb":
        Librecon().dirb(ip=ip)
        sys.exit(0)

    elif opt.lower() == "nikto":
        Librecon().nikto(ip=ip)
        sys.exit(0)

    elif opt.lower() == "ftp":
        Librecon().ftp(ip=ip)
        sys.exit(0)

    elif opt.lower() == "ftp":
        Librecon().sslyze(ip=ip)
        sys.exit(0)
    elif opt.lower() == "quickscan":
        Librecon().quickscan(ip=ip)
        sys.exit(0)

    elif opt.lower() == "sslyze":
        Librecon().sslyze(ip=ip)
        sys.exit(0)

    elif opt.lower() == "massrecon":
        Librecon().massrecon(ip=ip)
        sys.exit(0)
    else:
        __usage()
