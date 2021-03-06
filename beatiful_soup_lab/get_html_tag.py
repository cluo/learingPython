#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-15
__author__ = 'cluo'
from BeautifulSoup import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

if __name__ == '__main__':
    soup = BeautifulSoup(html_doc)
    print soup.title
    # <title>The Dormouse's story</title>

    print soup.title.name   #tagname
    # u'title'

    print soup.title.string  #text
    # u'The Dormouse's story'

    print soup.title.parent.name #parent tag name
    # u'head'

    print soup.p
    # <p class="title"><b>The Dormouse's story</b></p>

    print soup.p['class']
    # u'title'

    print soup.a
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    #
    print  soup.findAll('a')
    # # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    # #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    # #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    #
    print  soup.find(id="link3")
    # # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>