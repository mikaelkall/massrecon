#!/usr/bin/env python

from paver.tasks import task
from paver.easy import sh

@task
def tasks():
   ''' List all paver tasks '''
   sh('paver --help |grep -A 8 "Tasks from pavement"')
