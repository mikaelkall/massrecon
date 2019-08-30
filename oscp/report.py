
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Tries to automate the OSCP report writing from CherryTree data.
"""
__author__ = 'kall.micke@gmail.com'

import time
import os
import re
import sys

from shutil import copyfile

try:
    from librecon.configuration import *
    from librecon.utils import *
except:
    from configuration import *
    from utils import *

class Report:

    def __init__(self):

        self.cfg = Configuration()

    def create(self):

        home = str(Path.home())
        self.report_dir = '%s/.massrecon/' % home

        if os.path.isfile('template/OSCP-OS-XXXXX-Exam-Report_Template3.2.docx') is False:
            utils().puts('error', 'Template file not found')
            sys.exit(0)

        oscp_email = self.cfg.config.get('oscp', 'email')
        oscp_osid = self.cfg.config.get('oscp', 'osid')

        copyfile('template/OSCP-OS-XXXXX-Exam-Report_Template3.2.docx', self.report_dir + "/OSCP-%s-Exam-Report.docx" % oscp_osid)
        utils.puts('success', "Created: %s/OSCP-%s-Exam-Report.docx" % (self.report_dir, oscp_osid))
