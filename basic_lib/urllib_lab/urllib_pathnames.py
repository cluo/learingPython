#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import os

from urllib import pathname2url, url2pathname

print '== Default =='
path = '/a/b/c'
print 'Original:', path
print 'URL     :', pathname2url(path)
print 'Path    :', url2pathname('/d/e/f')
print

# == Default ==
# Original: /a/b/c
# URL     : /a/b/c
# Path    : /d/e/f
#

from nturl2path import pathname2url, url2pathname

print '== Windows, without drive letter =='
path = r'\a\b\c'
print 'Original:', path
print 'URL     :', pathname2url(path)
print 'Path    :', url2pathname('/d/e/f')
print

# Original: \a\b\c
# URL     : /a/b/c
# Path    : \d\e\f
#


print '== Windows, with drive letter =='
path = r'C:\a\b\c'
print 'Original:', path
print 'URL     :', pathname2url(path)
print 'Path    :', url2pathname('/d/e/f')


# == Windows, without drive letter ==

# == Windows, with drive letter ==
# Original: C:\a\b\c
# URL     : ///C:/a/b/c
# Path    : \d\e\f