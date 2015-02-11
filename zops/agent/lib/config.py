#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
实现多进程同时写一个文件功能

"""
import ConfigParser,string,os,sys
cf = ConfigParser.ConfigParser()
cf.read("conf/config.conf")


DB_HOST = cf.get("db", "DB_HOST")
DB_PORT = cf.getint("db", "DB_PORT")
DB_USER = cf.get("db", "DB_USER")
DB_PASSWD = cf.get("db", "DB_PASSWD")
DB_DB = cf.get("db", "DB_DB")


