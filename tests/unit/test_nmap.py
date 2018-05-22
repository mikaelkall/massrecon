import unittest2 as unittest
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../../'))

from librecon.nmap import *

class Unittests(unittest.TestCase):

    def setUp(self):
        self.np = Nmap(hostname='127.0.0.1')

    def test_methods(self):
        self.assertTrue(hasattr(self.np, "scan_stage_1"))
        self.assertTrue(hasattr(self.np, "scan_stage_2"))
