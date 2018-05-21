#!/usr/bin/env python

from paver.tasks import task
from paver.easy import sh
import subprocess

@task
def tasks():
   ''' List all paver tasks '''
   sh('paver --help |grep -A 8 "Tasks from pavement"')

@task
def tag_and_push():
   ''' Tag commit and push to master '''
   output = subprocess.getoutput("git ls-remote -q --tags | awk '{print $2}' |egrep -o '[0-9]+.[0-9]+.[0-9]+' |sort -g |head -1")
   if len(output) == 0:
       return

   # Increase version number
   major = output.split('.')[0]
   minor = output.split('.')[1]
   patch  = int(output.split('.')[-1]) + 1
   version="%s.%s.%s" % (major, minor, patch)

   print("\nYou are about to tag and commit and push %s to master" % version)
   x = input('Press y to continue or q to quit: ')
   if x == 'y':
      sh('git checkout master')
      sh('git rebase develop')
      sh('git tag -a %s -m "%s"' % (version, version))
      sh('git push origin master')
      sh('git push --tags')
