#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  CherryTree class
"""
__author__ = 'kall.micke@gmail.com'

import sqlite3
import os

class CherryTree:

    def __init__(self):

        self.conn = sqlite3.connect('massrecon.db')
