#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Expand shell variables in filenames.
"""

__version__ = "$Id$"
#end_pymotw_header

import os.path
import os

os.environ['MYVAR'] = 'VALUE'

print os.path.expandvars('/path/to/$MYVAR')
#扩展路径中出现的所有shell环境变量 这里不会做任何验证来是否存在文件