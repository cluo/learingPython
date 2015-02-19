#!/usr/bin/env python
#-*- coding:utf8 -*-
"""Parsing URLs
"""
#end_pymotw_header

from urlparse import urlparse

url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlparse(url)
print 'scheme  :', parsed.scheme
print 'netloc  :', parsed.netloc
print 'path    :', parsed.path
print 'params  :', parsed.params
print 'query   :', parsed.query
print 'fragment:', parsed.fragment
print 'username:', parsed.username
print 'password:', parsed.password
print 'hostname:', parsed.hostname, '(netloc in lowercase)'
print 'port    :', parsed.port

# scheme  : http
# netloc  : user:pwd@NetLoc:80
# path    : /path
# params  : param
# query   : query=arg
# fragment: frag
# username: user
# password: pwd
# hostname: netloc (netloc in lowercase)
# port    : 80
