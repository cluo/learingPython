#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
make by robinechen
modify by linzhonghong
"""

import os
import sys
import time
import datetime
import hashlib
import signal
from ConfigParser import ConfigParser,ParsingError
import pymysql
import imp
import json
import urllib2

main_path = '/usr/local/agenttools/agent/'

#输出LOG
def log(message, *args):
    message = message % args
    sys.stderr.write(message + '\n')

#上报数字接口
def report( id, value):
    report_tool = main_path + 'agentRepNum'
    cmd_report_monitor = "%s %s %s" % (report_tool, str(id).strip(), str(value))
    os.system(cmd_report_monitor)

#上报字符接口
def reportStr( id, alarm_str):
    report_tool = main_path + 'agentRepStr'
    cmd_report_monitor = "%s %s '%s'" % (report_tool, str(id).strip(), alarm_str)
    os.system(cmd_report_monitor)

def prog_dir():
    """
    获取程序的根路径
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def app_abs_path(rel_path=None):
    """
    返回路径的绝对路径，相对程序目录
    :param rel_path:相对路径
    :return:绝对路径
    """
    abs_path = ''
    if rel_path:
        abs_path = os.path.join(prog_dir(),rel_path)
    return abs_path

def read_config(config_file='conf/server.conf', section=""):
    """
    @note:解析配置文件，返回字典类型的配置信息
    @config_file:配置文件
    @return:典类型的配置信息
    """
    if not section:
        section = 'main'
    confparser = ConfigParser()
    opts = {}
    config_file = app_abs_path(config_file)
    if os.path.exists(config_file):
        try:
            confparser.read(config_file)
            # opts = {k:v for k,v in confparser.items('main')}
            for k,v in confparser.items(section):
                opts[k] = v
        except ParsingError, e:
            print >> sys.stderr, "Error reading config file: %s" % e
            sys.exit(1)
    return opts


def mysql_opts():
    """
    @note: 获取mysql参数配置
    @return：配置参数字典
    """
    opts = read_config(section='db')
    return opts
    # return dict(
    #     host = opts['host'],
    #     user = opts['user'],
    #     passwd = opts['passwd'],
    #     db = opts['db'],
    #     unix_socket = opts['unix_socket'],
    #     charset = opts['charset']
    # )

def get_file_md5(filename):
    """
    @note: 计算大文件MD5值
    @param filename: 文件绝对路径
    @return: 文件MD5值
    """
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = file(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def clean_proc(proc, wait_for_kill=10):
    """
    @note:清理进程函数
    @proc:进程实例
    @return:None
    """
    if not proc:
        return
    try:
        waited = 0
        while proc.is_alive():
            proc.terminate()
            waited += 1
            time.sleep(0.1)
            if proc.is_alive() and (waited >= wait_for_kill):
                os.kill(proc.pid,signal.SIGKILL)
    except (AssertionError, AttributeError):
        pass

def get_cur_datetime():
    return "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())

def send_to_master(sreq, load):
    try:
        ret = sreq.send(load)
    except Exception,e:
        print e


class MysqlHandler(object):
    def __init__(self):
        self.opts = mysql_opts()
        self.result = None

    def conn_db(self):
        try:
            conn = pymysql.connect(**self.opts)
        except:
            return None
        return conn

    def close_conn(self, conn):
        conn.commit()
        conn.close()

    def exec_sql(self, sqlstr, conn):
        error = False
        count = 0
        sqltype =sqlstr[0:6].lower()
        cur = conn.cursor()
        try:
            count = cur.execute(sqlstr)
        except:
            error = True
        if sqltype == 'select':
            if count == 0 or error:
                cur.close()
                self.result = False
                return False
            else:
                ret_list = cur.fetchall()
                cur.close()
                self.result = ret_list
                return ret_list
        elif sqltype == 'update' or sqltype == 'insert' or sqltype == 'delete':
            cur.close()
            if error:
                self.result = False
                return False
            else:
                self.result = True
                return True

    def result(self):
        return self.result

def load_module(mod_dir):
    """
    @note: 加载模块
    @param mod_dir:模块的路径
    @return:返回模块列表
    """
    names = {}
    modules = []
    funcs = {}
    for fn_ in os.listdir(mod_dir):
        if fn_.startswith('_'):
            continue
        if (fn_.endswith(('.py', '.pyc', '.pyo', '.so')) or os.path.isdir(fn_)):
            extpos = fn_.rfind('.')
            if extpos > 0:
                _name = fn_[:extpos]
            else:
                _name = fn_
            names[_name] = os.path.join(mod_dir, fn_)
    for name in names:
        try:
            # find_module函数第二个参数一定是一个list类型数据，否则执行失败
            fn_, path, desc = imp.find_module(name, [mod_dir])
            mod = imp.load_module(name, fn_, path, desc)
        except:
            continue
        modules.append(mod)
    for mod in modules:
        for attr in dir(mod):
            if attr.startswith('_'):
                continue
            #
            if callable(getattr(mod, attr)):
                func = getattr(mod, attr)
                if isinstance(func, type):
                    if any(['Error' in func.__name__, 'Exception' in func.__name__]):
                        continue
                try:
                    funcs['{0}.{1}'.format(mod.__name__, attr)] = func
                except:
                    continue
    return funcs

def post(url, data):
    """
    post到接口获取信息，主要是资源管理模块获取cmdb信息
    @param url:
    @param data:
    @return:
    """
    data = json.dumps(data).encode("utf-8")
    req = urllib2.urlopen(url, data)
    return json.loads(req.read())