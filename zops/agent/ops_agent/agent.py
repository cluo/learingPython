#!/usr/bin/env python
#-*- coding:utf8 -*-
__author__ = 'linzhonghong'
import os
import sys
import traceback
import hashlib
import time
import zmq
import zmq.auth
from zmq.auth.thread import ThreadAuthenticator
prog_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
prog_lib_dir = os.path.join(prog_, 'lib')
if prog_lib_dir not in sys.path:
    sys.path.insert(0, prog_lib_dir)
from heartbeats import HeartBeats
import payload
from util import read_config, send_to_master, prog_dir, load_module, app_abs_path
from multiprocessing.pool import ThreadPool
# 设置线程沲的大小，用于异步处理
pool = ThreadPool(processes=16)
from logger import Logger
log = Logger(config_file='conf/client.conf',
             logfile=os.path.join('logs', os.path.basename(os.path.realpath(sys.argv[0])).replace(".py",'.log'))
            )

class Client(object):

    def __init__(self, opts):
        self.opts = opts
        self.functions = load_module(app_abs_path(self.opts['mod_dir']))
        self.context = zmq.Context()
        self.client = self.context.socket(zmq.REP)
        self.uri = "tcp://%(local_ip)s:%(local_port)s"%self.opts
        self.poller = zmq.Poller()
        self.serial = payload.Serial()

    def __bind(self):
        self.auth = ThreadAuthenticator(self.context)
        self.auth.start()
        self.auth.allow(self.opts['master'])
        self.client.zap_domain = b'global'
        self.client.bind(self.uri)
        time.sleep(1)

    def do_task(self, task_info):
        sreq = payload.SREQ("tcp://%(master)s:%(master_port)s"%self.opts)
        try:
            # 执行指令前先验证
            secret = self.opts.get('secret', ' ')
            auth_key = task_info.get('auth_key', '')
            timestamp = task_info.get('timestamp', 0)
            if hashlib.md5("%s%s" % (secret, timestamp)).hexdigest() != auth_key:
                load = dict(
                    come_from='agent',
                    task_id=task_info['task_id'],
                    status=2,
                    ret_msg='task fail: auth key error',
                    ret_code=1001
                )
                send_to_master(sreq, load)
                return
            if abs(int(time.time())-int(timestamp)) > 60:
                load = dict(
                    come_from='agent',
                    task_id=task_info['task_id'],
                    status=2,
                    ret_msg='task fail: auth key expired',
                    ret_code=1001
                )
                send_to_master(sreq, load)
                return

            log.logger.info("running: task %s, func %s"%(task_info['task_id'], task_info['func']))
            # 执行模块函数之前，切换当前目录为prog_dir()
            os.chdir(prog_dir())
            f = task_info.pop('func')
            if f in self.functions:
                func = self.functions[f]
                ret = func(**task_info)
                if ret:
                    status = 1
                    ret_msg = 'task succ'
                    ret_code = 0
                else:
                    status = 2
                    ret_msg = 'task fail'
                    ret_code = 1001
            else:
                status = 2
                ret_msg = 'function %s not exists' % f
                ret_code = 1004
        except Exception, e:
            log.logger.error(e)
            status = 2
            ret_msg = 'task fail, %s' % traceback.format_exc()
            ret_code = 1001
        finally:
            # 避免函数改变当前目录，执行模块函数之后，换当前目录为prog_dir()
            os.chdir(prog_dir())
        load = dict(
            come_from='agent',
            task_id=task_info['task_id'],
            status=status,
            ret_msg=ret_msg,
            ret_code=ret_code
        )
        send_to_master(sreq, load)

    def run(self):
        if zmq.zmq_version_info() < (4,0):
            raise RuntimeError("Security is not supported in libzmq version < 4.0. libzmq version {0}".format(zmq.zmq_version()))
        self.heartbeats = HeartBeats(self.opts)
        self.heartbeats.start()
        self.__bind()
        while True:
            recv = self.serial.loads(self.client.recv())
            try:
                self.client.send(self.serial.dumps({'task_id':recv['task_id'], 'ret':'ok'}))
            except Exception,e:
                print e
                continue
            pool.apply_async(self.do_task, (recv, ))

    def destroy(self):
        if self.client.closed is False:
            self.client.setsockopt(zmq.LINGER, 1)
            self.client.close()
        if self.context.closed is False:
            self.context.term()
        self.heartbeats.join()

    def __del__(self):
        self.destroy()

if __name__ == '__main__':
    opts = read_config(config_file='conf/client.conf')
    cli = Client(opts)
    cli.run()