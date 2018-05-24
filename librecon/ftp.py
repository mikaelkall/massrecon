#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Ftp
   Module for loot files from anonymous ftp
"""
__author__ = 'kall.micke@gmail.com'

import ftplib
import signal
import sys

try:
    from librecon.configuration import *
    from librecon.cherrytree import *
    from librecon.utils import *
    from librecon.colors import *
except:
    from configuration import *
    from cherrytree import *
    from utils import *
    from colors import *

# Handler to exist cleanly on ctrl+C
def signal_handler(signal, frame):
    print("\nYou pressed Ctrl+C!")
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)


class Ftp:

    def __init__(self, hostname=''):

        self.hostname = hostname

        if len(self.hostname) == 0:
            return

        self.module_disable = False
        self.directory_log = False

        self.chr = CherryTree(address=hostname)

        # Load configuration
        self.cfg = Configuration()
        self.config_dir = self.cfg.config_dir

        if self.cfg.config.get('massrecon', 'directory_log') == 'True':
            self.directory_log = True

        if self.cfg.config.get('massrecon', 'cherrytree_log') == 'True':
            self.cherrytree_log = True

        self.scanfolder = '%s/results/ftp_loot/%s' % (self.config_dir, self.hostname)

        if self.directory_log is True:
            self.ftp_dir = '%s/results/%s/ftp_loot' % (self.config_dir, self.hostname)
            if os.path.isdir(self.ftp_dir) is False:
                os.makedirs(self.ftp_dir, exist_ok=True)

    def _is_ftp_dir(self, ftp_handle, name, guess_by_extension=True):
        """ simply determines if an item listed on the ftp server is a valid directory or not """

        # if the name has a "." in the fourth to last position, its probably a file extension
        # this is MUCH faster than trying to set every file to a working directory, and will work 99% of time.
        if guess_by_extension is True:
            if len(name) >= 4:
                if name[-4] == '.':
                    return False

        original_cwd = ftp_handle.pwd()  # remember the current working directory
        try:
            ftp_handle.cwd(name)  # try to set directory to new name
            ftp_handle.cwd(original_cwd)  # set it back to what it was
            return True

        except ftplib.error_perm as e:
            return False
        except:
            return False

    def _make_parent_dir(self, fpath):
        """ ensures the parent directory of a filepath exists """
        dirname = os.path.dirname(fpath)
        while not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
                #print("created {0}".format(dirname))
            except:
                self._make_parent_dir(dirname)

    def _download_ftp_file(self,ftp_handle, name, dest, overwrite):
        """ downloads a single file from an ftp server """
        Ftp()._make_parent_dir(dest.lstrip("/"))
        if not os.path.exists(dest) or overwrite is True:
            try:
                with open(dest, 'wb') as f:
                    ftp_handle.retrbinary("RETR {0}".format(name), f.write)

                if dest.startswith('./'):
                    _dest = dest.replace('./', '')
                else:
                    _dest = dest

                utils().puts('success', "Looting %s/%s" % (self.ftp_dir, _dest))
            except FileNotFoundError:
                pass
                #print("FAILED: {0}".format(dest))
        else:
            pass
            #print("already exists: {0}".format(dest))

    def _mirror_ftp_dir(self,ftp_handle, name, overwrite, guess_by_extension):
        """ replicates a directory on an ftp server recursively """
        for item in ftp_handle.nlst(name):
            if self._is_ftp_dir(ftp_handle, item, guess_by_extension):
                self._mirror_ftp_dir(ftp_handle, item, overwrite, guess_by_extension)
            else:
                self._download_ftp_file(ftp_handle, item, item, overwrite)

    def download_ftp_tree(self, ftp_handle, path, destination, overwrite=False, guess_by_extension=True):
        """
        Downloads an entire directory tree from an ftp server to the local destination
        :param ftp_handle: an authenticated ftplib.FTP instance
        :param path: the folder on the ftp server to download
        :param destination: the local directory to store the copied folder
        :param overwrite: set to True to force re-download of all files, even if they appear to exist already
        :param guess_by_extension: It takes a while to explicitly check if every item is a directory or a file.
        if this flag is set to True, it will assume any file ending with a three character extension ".???" is
        a file and not a directory. Set to False if some folders may have a "." in their names -4th position.
        """

        path = path.lstrip("/")
        original_directory = os.getcwd()  # remember working directory before function is executed
        os.chdir(destination)  # change working directory to ftp mirror directory
        self._mirror_ftp_dir(ftp_handle, path, overwrite, guess_by_extension)
        os.chdir(original_directory)  # reset working directory to what it was before function exec

    def run(self):
        utils().puts('info', 'Tries anonymous FTP')
        f = ftplib.FTP(self.hostname, 'anonymous', 'anonymous')
        self.download_ftp_tree(f, './', self.ftp_dir)