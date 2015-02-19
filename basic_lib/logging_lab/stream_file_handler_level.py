#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-18
import logging #开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件

# 创建一个logger
# logging.getLogger([name])
# 返回一个logger实例，如果没有指定name，返回root logger。
# 只要name相同，返回的logger实例都是同一个而且只有一个，即name和logger实例是
# 一一对应的。这意味着，无需把logger实例在各个模块中传递。只要知道name，就能得到
# 同一个logger实例
logger = logging.getLogger('mylogger')

#setLevel
# NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
# 如果把looger的级别设置为INFO， 那么小于INFO级别的日志都不输出， 大于等于INFO级
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
# Logger.addHandler(hdlr)
# logger可以雇佣handler来帮它处理日志， handler主要有以下几种：
# StreamHandler: 输出到控制台
# FileHandler:   输出到文件
#handler还可以设置自己的level以及输出格式。
logger.addHandler(fh)
logger.addHandler(ch)

# 记录一条日志
#运行后， 在控制台和日志文件都有一条日志：
logger.info('foorbar')

# 2011-08-31 19:18:29,816 - mylogger - INFO - foorbar




# logging.basicConfig([**kwargs])
# * 这个函数用来配置root logger， 为root logger创建一个StreamHandler，
#    设置默认的格式。
# * 这些函数： logging.debug()、logging.info()、logging.warning()、
#    logging.error()、logging.critical() 如果调用的时候发现root logger没有任何
#    handler， 会自动调用basicConfig添加一个handler
# * 如果root logger已有handler， 这个函数不做任何事情
#
# 使用basicConfig来配置root logger的输出格式和level：
# Python代码
# import logging
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
