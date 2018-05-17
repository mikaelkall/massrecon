#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  CherryTree class
"""
__author__ = 'kall.micke@gmail.com'

import sqlite3
import time
import os

from librecon.configuration import *
from librecon.utils import *


class CherryTree:

    def __init__(self, address=''):

        if len(address) == 0:
            return

        self.address = address

        # Load configuration
        cfg = Configuration()

        if cfg.config.get('massrecon', 'cherrytree_log') != 'True':
            utils.puts('info', 'CherryTree module is disabled')
            return

        db_file = '%s/massrecon.ctb' % cfg.config_dir

        if os.path.exists(db_file) is False:
            utils.puts('info', 'CherryTree database not found. Created it.')
            self.conn = sqlite3.connect(db_file)
            self.setup_database()
        else:
            self.conn = sqlite3.connect(db_file)

    def setup_database(self):

        self.conn.execute('CREATE TABLE IF NOT EXISTS bookmark (node_id INTEGER, sequence INTEGER)')
        self.conn.execute('CREATE TABLE IF NOT EXISTS children (node_id INTEGER, father_id INTEGER, sequence INTEGER)')
        self.conn.execute('CREATE TABLE IF NOT EXISTS codebox (node_id INTEGER, offset INTEGER, justification TEXT, txt TEXT, syntax TEXT, width INTEGER, height INTEGER, is_width_pix INTEGER, do_highl_bra INTEGER, do_show_linenum INTEGER)')
        self.conn.execute('CREATE TABLE IF NOT EXISTS grid (node_id INTEGER, offset INTEGER, justification TEXT, txt TEXT, col_min INTEGER, col_max INTEGER)')
        self.conn.execute('CREATE TABLE IF NOT EXISTS image (node_id INTEGER, offset INTEGER, justification TEXT, anchor TEXT, png BLOB, filename TEXT, link TEXT, time INTEGER)')
        self.conn.execute('CREATE TABLE IF NOT EXISTS node (node_id INTEGER, name TEXT, txt TEXT, syntax TEXT, tags TEXT, is_ro INTEGER, is_richtxt INTEGER, has_codebox INTEGER, has_table INTEGER, has_image INTEGER, level INTEGER, ts_creation INTEGER, ts_lastsave INTEGER)')

        self.insert('root', 'machines')

    def get_node_id(self, name):

        node_id = 0

        try:
            cur = self.conn.cursor()
            cur.execute("SELECT node_id FROM node WHERE name='%s'" % name)
            node_id = int(cur.fetchone()[0])
            cur.close()
        except:
            pass

        return node_id

    def get_next_node_id(self):

        next_id = 1

        try:
            cur = self.conn.cursor()
            cur.execute('SELECT max(node_id) FROM node')
            next_id = int(cur.fetchone()[0]) + 1
            cur.close()
        except:
            pass

        return next_id

    def check_if_exist(self, name=''):

        try:
            cur = self.conn.cursor()
            cur.execute("select name from node where name='%s'" % name)
            chk_name = str(cur.fetchone()[0])
            cur.close()
        except:
            pass

        try:
            if name == chk_name:
                return True
            else:
                return False
        except:
            return False

    def insert(self, name='', leaf='', txt=''):

        node_id = None
        next_id = None

        if len(name) == 0 or leaf == 0:
            return

        # Avoid dublicates
        if leaf == self.address:
            if self.check_if_exist(name=leaf) is True:
                return

        node_id = self.get_node_id(name=name)
        next_id = self.get_next_node_id()

        # Configures default values
        epoch = time.mktime(time.localtime())

        txt = '<?xml version="1.0"?><node><rich_text>%s</rich_text></node> ' % txt
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

        # Add node
        cur = self.conn.cursor()

        if len(leaf) > 0:
            name = leaf

        cur.execute('INSERT INTO node VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', (next_id,
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
                                                                            ts_lastsave))
        self.conn.commit()

        # Add children
        _sql = "INSERT INTO children VALUES (%s,%s,%s)" % (next_id, node_id, 1)
        cur.execute(_sql)
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    pass