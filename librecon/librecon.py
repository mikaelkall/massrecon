#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  librecon.
  Find all vectors
"""
__author__ = 'kall.micke@gmail.com'

from librecon.nmap import *
from librecon.dirb import *

class Librecon:

    def __init__(self):
        pass

    '''
    Initate all recon modules
    '''
    def run(self, ip=''):

        # Starts nmap scan
        np = Nmap(hostname=ip)
        np.scan_stage_1()
        np.scan_stage_2()

        # Port 443 is open spider target.
        if '443' in np.ports:
            db = Dirb(hostname=ip, ssl_proto=True)
            db.download_certificate()
            db.robots_scan()
            db.dirb_stage_1()

        # Port 80 is open spider target.
        if '80' in np.ports:
            db = Dirb(hostname=ip, ssl_proto=False)
            db.robots_scan()
            db.dirb_stage_1()

    '''
    Initiate nmap module only
    '''
    def nmap(self, ip = ''):
        # Starts nmap scan
        np = Nmap(hostname=ip)
        np.scan_stage_1()
        np.scan_stage_2()

    '''
    Initiate Dirb module only
    '''
    def dirb(self, ip = ''):
        # Starts nmap scan
        db = Dirb(hostname=ip, ssl_proto=False)
        db.robots_scan()
        db.dirb_stage_1()

        db = Dirb(hostname=ip, ssl_proto=True)
        db.download_certificate()
        db.robots_scan()
        db.dirb_stage_1()