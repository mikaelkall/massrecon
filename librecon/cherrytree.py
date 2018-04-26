#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  CherryTree class
"""
__author__ = 'kall.micke@gmail.com'

import sqlite3
import time
import os

from utils import *

class CherryTree:

    def __init__(self):

        self.LEVEL = {'root': 0, 'host': 1, 'recon': 2, 'nmap': 3}

        db_file = os.path.join(os.path.dirname(__file__), '../.db/massrecon.ctb')

        if os.path.exists(db_file) is False:
            utils.puts('error', 'database could not be found')
            return False

        self.conn = sqlite3.connect(db_file)

    def insert(self, on_level='', data=''):

        if len(data) == 0:
            return

        if on_level not in self.LEVEL.keys():
            utils.puts('info', 'The input level do not match the levels configured')
            return False

        cur = self.conn.cursor()
        cur.execute('SELECT max(node_id) FROM node')
        node_id = int(cur.fetchone()[0]) + 1
        cur.close()

        # Configures default values
        epoch = time.mktime(time.localtime())

        name = data
        txt = '<?xml version="1.0"?><node><rich_text></rich_text></node> '
        syntax = 'customer-colors'
        tags = 0
        is_ro = 0
        is_rightxt = 0
        has_codebox = 0
        has_table = 0
        has_image = 0
        level = 0
        ts_creation = epoch
        ts_lastsave = epoch

        _sql = "INSERT INTO node VALUES (%s, '%s','%s', '%s', %s, %s, %s, %s, %s, %s, %s, '%s', '%s')" % (node_id,
                                                                                                          name,
                                                                                                          txt,
                                                                                                          syntax,
                                                                                                          tags,
                                                                                                          is_ro,
                                                                                                          is_rightxt,
                                                                                                          has_codebox,
                                                                                                          has_table,
                                                                                                          has_image,
                                                                                                          level,
                                                                                                          ts_creation,
                                                                                                          ts_lastsave)
        # Add node
        print(_sql)
        cur = self.conn.cursor()
        cur.execute(_sql)
        self.conn.commit()

        # Add children
        _sql = "INSERT INTO children VALUES (%s,%s,%s)" % (node_id, self.LEVEL[on_level], 1)
        print(_sql)
        cur.execute(_sql)
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == '__main__':

    chr = CherryTree()
    chr.insert('host', '192.168.0.2')
    chr.close()
