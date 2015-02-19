#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Test properties of a file.
"""

__version__ = "$Id$"
#end_pymotw_header

import os.path

FILENAMES = [ __file__,
              os.path.dirname(__file__),
              '/',
              './broken_link',
              ]

for file in FILENAMES:
    print 'File        :', file
    print 'Absolute    :', os.path.isabs(file)
    print 'Is File?    :', os.path.isfile(file)
    print 'Is Dir?     :', os.path.isdir(file)
    print 'Is Link?    :', os.path.islink(file)
    print 'Mountpoint? :', os.path.ismount(file)
    print 'Exists?     :', os.path.exists(file)
    print 'Link Exists?:', os.path.lexists(file)
    print
# File        : /Users/admin/gitSource/learingPython/basic_lib/os_path_lab/ospath_tests.py
# Absolute    : True
# Is File?    : True
# Is Dir?     : False
# Is Link?    : False
# Mountpoint? : False
# Exists?     : True
# Link Exists?: True
#
# File        : /Users/admin/gitSource/learingPython/basic_lib/os_path_lab
# Absolute    : True
# Is File?    : False
# Is Dir?     : True
# Is Link?    : False
# Mountpoint? : False
# Exists?     : True
# Link Exists?: True
#
# File        : /
# Absolute    : True
# Is File?    : False
# Is Dir?     : True
# Is Link?    : False
# Mountpoint? : True
# Exists?     : True
# Link Exists?: True
#
# File        : ./broken_link
# Absolute    : False
# Is File?    : False
# Is Dir?     : False
# Is Link?    : False
# Mountpoint? : False
# Exists?     : False
# Link Exists?: False
