#!/usr/bin/env python
#-*- coding:utf8 -*-
"""Joining relative fragments into absolute URLs
"""
#end_pymotw_header

from urlparse import urljoin

print urljoin('http://www.example.com/path/file.html', #相对路径URL构造
              'anotherfile.html')
print urljoin('http://www.example.com/path/file.html',
              '../anotherfile.html')

# http://www.example.com/path/anotherfile.html
# http://www.example.com/anotherfile.html
