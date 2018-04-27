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
    print ("""
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
""")

    sys.exit(0)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        __usage()

    opt = sys.argv[1].strip()
    if opt.lower() == "recon":
        Librecon().run()
    else:
        __usage()