#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import subprocess

# Command with shell expansion
subprocess.call('echo $HOME', shell=True) #shell模式运行前先会处理变量  call会返回退出码，非0为错误
# /Users/admin