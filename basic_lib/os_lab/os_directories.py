#!/usr/bin/env python
#-*- coding:utf8 -*-
# Copyright 2007 Doug Hellmann.
#
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of Doug
# Hellmann not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

"""Working with directories.

"""

__module_id__ = "$Id$"
#end_pymotw_header

import os

dir_name = 'os_directories_example'

print 'Creating', dir_name
os.makedirs(dir_name)
# Creating os_directories_example


file_name = os.path.join(dir_name, 'example.txt')
print 'Creating', file_name
# Creating os_directories_example/example.txt

with open(file_name, 'wt') as f:
    f.write('example file')

print 'Listing', dir_name
# Listing os_directories_example
print os.listdir(dir_name)
# ['example.txt']

print 'Cleaning up'
# Cleaning up
os.unlink(file_name) #删除文件
os.rmdir(dir_name)  #删除目录






