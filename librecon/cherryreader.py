#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  CherryTree Reader class
"""
__author__ = 'kall.micke@gmail.com'

import time
import os
import re

from socket import inet_aton
import struct

try:
    from librecon.configuration import *
    from librecon.utils import *
except:
    from configuration import *
    from utils import *


class CherryTreeReader:

    def __init__(self):

        # Load configuration
        cfg = Configuration()

        if len(cfg.config.get('massrecon', 'cherrytree_dbfile')) != 0 and 'DEFAULTDB' not in os.environ:
            self.db_file = cfg.config.get('massrecon', 'cherrytree_dbfile')
        else:
            self.db_file = '%s/massrecon.ctd' % cfg.config_dir

        if os.path.exists(self.db_file) is False:
            utils.puts('info', 'CherryTree database not found')
            os._exit(0)

    def get_addresses(self):

        addresses = []
        with open(self.db_file, 'r') as file:
            for row in file.read().split('\n'):
                rgxp = re.compile('.*<node custom_icon_id="10" foreground="" is_bold="True" name="(.*)" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1496953072.48" unique_id="\d+">.*')
                if len(rgxp.findall(row)) == 1:
                    try:
                        addresses.append(rgxp.search(row).group(1))
                    except:
                        pass
        try:
            sorted(addresses, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])
        except:
            addresses.sort()

        return addresses

if __name__ == '__main__':
    pass
    #print(CherryTreeReader().get_addresses())

