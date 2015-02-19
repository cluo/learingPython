#!/usr/bin/env python
#
# Copyright 2010 Doug Hellmann.
#
"""Checking exit codes from external processes
"""
#end_pymotw_header

import subprocess

try:
    subprocess.check_call(['false'])      #check_call如果出错会产生异常
except subprocess.CalledProcessError as err:
    print 'ERROR:', err
# ERROR: Command '['false']' returned non-zero exit status 1