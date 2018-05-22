import unittest2 as unittest
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../../'))

from librecon.dirb import *

class Unittests(unittest.TestCase):

    def setUp(self):
        self.db = Dirb(hostname='127.0.0.1', ssl_proto=False)

    def test_methods(self):
        self.assertTrue(hasattr(self.db, "dirb_stage_1"))
        self.assertTrue(hasattr(self.db, "robots_scan"))
