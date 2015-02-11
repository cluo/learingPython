#!/usr/bin/env python
#-*- coding:utf8 -*-
__author__ = 'linzhonghong'
import os
import sys
import re
import commands
import platform
import traceback
import multiprocessing
import threading
from util import read_config
from mylog import init_aps_logger
import payload
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_MISSED
from apscheduler.triggers.interval import IntervalTrigger
from logger import Logger
log = Logger(config_file='conf/client.conf',
             logfile=os.path.join('logs', os.path.basename(os.path.realpath(sys.argv[0])).replace(".py",'.log'))
            )

aps_log = init_aps_logger('apscheduler', './logs/')

#apscheduler.events
def err_listener(ev):
    if ev.exception:
        aps_log.info('%s error.', str(ev.job))
    else:
        aps_log.info('%s miss', str(ev.job))

class HeartBeats(threading.Thread):
    """
    @note: 通过子进程方式，下发agent版本信息给客户端
    """
    def __init__(self, opts):
        """

        @param opts: 配置项
        """
        super(HeartBeats, self).__init__()
        self.opts = opts
        self.serial = payload.Serial()

    @property
    def get_ip(self):
        # get LAN IP address
        #cmd_get_ip = "/sbin/ifconfig br0|grep 'inet addr'|awk -F\: '{print $2}'|awk '{print $1}'"
        cmd_get_ip = "/sbin/ifconfig|grep 'inet addr'|awk -F\: '{print $2}'|awk '{if($1~/192\.168\.|172\.16\.|10\./){print $1}}'|head -1"
        try:
            ip = os.popen(cmd_get_ip).readline().strip()
        except:
            ip = '127.0.0.1'
        return ip

    @property
    def get_version(self):
        opts = read_config(config_file='conf/client.conf')
        return opts.get('version')

    def report_heartbeats(self):
        sreq = payload.SREQ("tcp://%(master)s:%(master_port)s"%self.opts)
        load = dict(
            come_from='HB',
            async=1,
            host_ip=self.get_ip,
            agent_version=self.get_version
        )
        try:
            ret = sreq.send(load)
            log.logger.info(ret)
        except Exception,e:
            log.logger.error(e)

    def run(self):
        self.report_heartbeats()
        sched = BlockingScheduler()
        sched.add_listener(err_listener, EVENT_JOB_ERROR | EVENT_JOB_MISSED)
        sched.add_job(self.report_heartbeats, trigger=IntervalTrigger(seconds=300))
        sched.start()

if __name__ == '__main__':
    opts = read_config(config_file='conf/client.conf')
    rr = HeartBeats(opts)
    rr.start()