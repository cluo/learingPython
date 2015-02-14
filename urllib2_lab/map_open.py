#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-14
__author__ = 'cluo'
import urllib2

# map 这一小巧精致的函数是简捷实现 Python 程序并行化的关键。
# map 源于 Lisp 这类函数式编程语言。它可以通过一个序列实现两个函数之间的映射。
urls = ['http://www.yahoo.com', 'http://www.reddit.com']
results = map(urllib2.urlopen, urls)
print results


# 上面的这两行代码将 urls 这一序列中的每个元素作为参数传递到 urlopen 方法中，
# 并将所有结果保存到 results 这一列表中。其结果大致相当于：
results = []
for url in urls:
    results.append(urllib2.urlopen(url))
print results
