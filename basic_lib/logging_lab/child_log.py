#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-18
import logging

# root logger是默认的logger
# 如果不创建logger实例， 直接调用logging.debug()、logging.info()logging.warning()、logging.error()、logging.critical()这些函数，
# 那么使用的logger就是 root logger， 它可以自动创建，也是单实例的。
#
# 如何得到root logger
# 通过logging.getLogger()或者logging.getLogger("")得到root logger实例。
#
# 默认的level
# root logger默认的level是logging.WARNING
#
# 如何表示父子关系
# logger的name的命名方式可以表示logger之间的父子关系. 比如：
# parent_logger = logging.getLogger('foo')
# child_logger = logging.getLogger('foo.bar')
#
# 什么是effective level
# logger有一个概念，叫effective level。 如果一个logger没有显示地设置level，那么它就
# 用父亲的level。如果父亲也没有显示地设置level， 就用父亲的父亲的level，以此推....
# 最后到达root logger，一定设置过level。默认为logging.WARNING
# child loggers得到消息后，既把消息分发给它的handler处理，也会传递给所有祖先logger处理，

# 设置root logger
r = logging.getLogger()
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
r.addHandler(ch)

# 创建一个logger作为父亲
p = logging.getLogger('foo')
p.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
ch.setFormatter(formatter)
p.addHandler(ch)

# 创建一个孩子logger
# 可见， 孩子logger没有任何handler，所以对消息不做处理。
# 但是它把消息转发给了它的父
# 亲以及root logger。最后输出两条日志。
c = logging.getLogger('foo.bar')
c.debug('foo')