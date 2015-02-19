#!/usr/bin/env python
#
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

"""Example of os.walk() implementing a simple recursive directory listing.

"""

__module_id__ = "$Id$"
#end_pymotw_header

import os, sys

# If we are not given a path to list, use /tmp
if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]

for dir_name, sub_dirs, files in os.walk(root):
    print dir_name #返回所有mulu

    # Make the subdirectory names stand out with /
    sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = sub_dirs + files
    contents.sort()
    # Show the contents
    for c in contents:
        print '\t%s' % c
    print





# /tmp
# 	.pd/
# 	KSOutOfProcessFetcher.501.OlaJUhhgKAnFsX7fZ0FyXTFxIgg=/
# 	KSOutOfProcessFetcher.tSEKseLfpG/
# 	aprTOrFZ0
# 	launch-h6gzLN/
# 	launch-oAj9PS/
# 	launchd-1774.BF45pO/
# 	launchd-2246.0XDlDd/
# 	launchd-976.ifK0r4/
# 	parallels_crash_dumps/
#
# /tmp/.pd
# 	501/
#
# /tmp/.pd/501
#
# /tmp/KSOutOfProcessFetcher.501.OlaJUhhgKAnFsX7fZ0FyXTFxIgg=
# 	ksfetch
#
# /tmp/KSOutOfProcessFetcher.tSEKseLfpG
# 	download
#
# /tmp/launch-h6gzLN
# 	Listeners
#
# /tmp/launch-oAj9PS
# 	Render
#
# /tmp/launchd-976.ifK0r4
# 	sock
#
# /tmp/parallels_crash_dumps
