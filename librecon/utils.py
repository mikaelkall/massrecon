#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  utils.
"""
__author__ = 'kall.micke@gmail.com'

import os

class utils:

    @staticmethod
    def puts(tp, msg, silent=False, nocolor=False):

        # Skip output if it should be silent is good to make test output more clean
        if silent is True:
            return

        """Output messages in fancy colors."""
        if tp == 'info':
            color_code = ('\033[93m' if nocolor is False else '')

            try:
                _msg = ("%s%5s%10s%s" % (color_code, "➜ ", msg, '\033[0m'))
                print(_msg)
                return _msg
            except:
                try:
                    _msg = ("%s%5s%10s%s" % (color_code, " ", msg, '\033[0m'))
                    print(_msg)
                    return _msg
                except:
                    pass

        elif tp == 'warning':
            color_code = ('\033[93m' if nocolor is False else '')
            try:
                _msg = ("%s%5s%10s%s" % (color_code, "➜ ", msg, '\033[0m'))
                print(_msg)
                return _msg
            except:
                try:
                    _msg = ("%s%5s%10s%s" % (color_code, " ", msg, '\033[0m'))
                    print(_msg)
                    return _msg
                except:
                    pass

        elif tp == 'error':
            color_code = ('\033[91m' if nocolor is False else '')
            try:
                _msg = ("%s%5s%10s%s" % (color_code, "✖ ", msg, '\033[0m'))
                print(_msg)
                return _msg
            except:

                try:
                    _msg = ("%s%5s%10s%s" % (color_code, " ", msg, '\033[0m'))
                    print(_msg)
                    return _msg
                except:
                    pass

        elif tp == 'success':
            color_code = ('\033[92m' if nocolor is False else '')
            try:
                _msg = ("%s%5s%10s%s" % (color_code, "✔ ", msg, '\033[0m'))
                print(_msg)
                return _msg
            except:

                try:
                    _msg = ("%s%5s%10s%s" % (color_code, " ", msg, '\033[0m'))
                    print(_msg)
                    return _msg
                except:
                    pass