#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  massrecon
  Relax this finds all vectors
"""

import sys
import os
import signal

from librecon.librecon import *

sys.path.insert(1, os.path.join(sys.path[0], '../'))

__author__ = 'kall.micke@gmail.com'

# Handler to exist cleanly on ctrl+C
def signal_handler(signal, frame):
    print("\nYou pressed Ctrl+C!")
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)


def __usage():
    print("""
███╗   ███╗ █████╗ ███████╗███████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
████╗ ████║██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██╔████╔██║███████║███████╗███████╗██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║╚██╔╝██║██╔══██║╚════██║╚════██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║███████║███████║██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
[kall.micke@gmail.com] [Scans and updates CherryTree]                                                                                           

Usage: massrecon [OPTIONS]

General Options

   recon <ip>\t\tStart recon target
   nmap  <ip>\t\tRun nmap module only
   dirb  <ip>\t\tRun dirb module only
""")

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

    if opt.lower() == "nmap":
        Librecon().nmap(ip=ip)
        sys.exit(0)

    if opt.lower() == "dirb":
        Librecon().dirb(ip=ip)
        sys.exit(0)
    else:
        __usage()
