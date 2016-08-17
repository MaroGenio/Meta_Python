#!/usr/bin/env python
import os
import sys
import shutil
from apscheduler.schedulers import blocking
"""
user_dir = os.path.expanduser('~')
star_dir = user_dir + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
script_name = sys.argv[0]
pwd = os.getcwd()
source = pwd + '\\' + script_name
shutil.copy(source,star_dir)
"""

def job():
    print "Hello World!"

s = blocking()
s.add_job(job, 'interval', second=10)
s.start()
