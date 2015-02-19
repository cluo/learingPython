#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Expand tilde in filenames.
"""

__version__ = "$Id$"
#end_pymotw_header

import os.path

for user in [ '', 'dhellmann', 'postgresql' ]:
    lookup = '~' + user
    print '%12s : %s' % (lookup, os.path.expanduser(lookup))
 #           ~ : /Users/admin
 #  ~dhellmann : ~dhellmann    目录在用户目录不存在原样返回
 # ~postgresql : ~postgresql   目录在用户目录不存在原样返回
