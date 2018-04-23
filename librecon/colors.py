#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  colors
"""
__author__ = 'kall.micke@gmail.com'

class Colors:

    blue = ''
    reset = ''
    grey = ''
    yellow = ''
    red = ''
    green = ''
    purple = ''

    def __init__(self, disabled=False):

        if disabled is False:
            self.blue = '\033[1;34m'
            self.reset = '\033[0m'
            self.grey = '\033[90m'
            self.yellow = '\033[93m'
            self.red = '\033[91m'
            self.green = '\033[92m'
            self.purple = '\033[35m'
