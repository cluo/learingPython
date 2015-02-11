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
import shlex
import commands
import subprocess
from ConfigParser import ConfigParser,ParsingError
import imp

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

def read_config(config_file='conf/client.conf', section=""):
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

def write_config(option, value, config_file='conf/client.conf', section='main'):
    """
    @note:更新配置文件
    @config_file:配置文件
    @return: 0 or 1
    """
    ret = 0
    confparser = ConfigParser()
    config_file = app_abs_path(config_file)
    if os.path.exists(config_file):
        try:
            confparser.read(config_file)
            fp = open(config_file, 'w')
            if confparser.has_section(section):
                confparser.set(section, option, value)
                ret = 1
            confparser.write(fp)
            fp.close()
        except Exception, e:
            print >> sys.stderr, "Error reading config file: %s" % e
            sys.exit(1)
    return ret

def mysql_opts():
    """
    @note: 获取mysql参数配置
    @return：配置参数字典
    """
    opts = read_config()
    return dict(
        host = opts['host'],
        user = opts['user'],
        passwd = opts['passwd'],
        db = opts['db'],
        unix_socket = opts['unix_socket'],
        charset = opts['charset']
    )

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

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

class Command(object):

    def __init__(self, command):
        self.command = command

    def run(self):
        status, output = commands.getstatusoutput(self.command)
        if status != 0:
            status = -1
        return status, output


class Command2(object):
    """
    Run subprocess commands.
    """
    command = None
    process = None
    status = None
    output, error = '', ''

    def __init__(self, command):
        if isinstance(command, basestring):
            command = shlex.split(command)
        self.command = command

    def run(self, timeout=None, **kwargs):
        """ Run a command then return: (status, output). """
        proc = subprocess.Popen(
            self.command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=True
        )
        try:
            if proc.wait(timeout) == 0:
                self.status = 0
                self.output = proc.stdout.read()
            else:
                self.output = proc.stdout.read()
                self.status = -1
        except subprocess.TimeoutExpired:
            try:
                os.kill(proc.pid, signal.SIGKILL)
            except:
                pass
            self.output = 'timeout'
            self.status = -1
        return self.status, self.output
