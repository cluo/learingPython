#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Capture the output of a command and test its exit code at the same time.
"""
#end_pymotw_header

import subprocess

try:
    output = subprocess.check_output(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        shell=True,
        )
except subprocess.CalledProcessError as err:
    print 'ERROR:', err
else:
    print 'Have %d bytes in output' % len(output)
    print output
# ERROR: Command 'echo to stdout; echo to stderr 1>&2; exit 1' returned non-zero exit status 1
# to stderr