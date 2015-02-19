#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Find attributes of a file other than its name.
"""

__version__ = "$Id$"
#end_pymotw_header

import os.path
import time

print 'File         :', __file__
print 'Access time  :', time.ctime(os.path.getatime(__file__))
print 'Modified time:', time.ctime(os.path.getmtime(__file__))
print 'Change time  :', time.ctime(os.path.getctime(__file__))
print 'Size         :', os.path.getsize(__file__)

#文件时间 文件大小
# File         : /Users/admin/gitSource/learingPython/basic_lib/os_path_lab/ospath_properties.py
# Access time  : Tue Feb 17 17:03:43 2015
# Modified time: Mon Feb 21 01:37:45 2011
# Change time  : Tue Feb 17 09:56:39 2015
# Size         : 495