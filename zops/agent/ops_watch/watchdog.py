#!/usr/bin/env python
#-*- coding:utf8 -*-
__author__ = 'linzhonghong'
import os
import sys
import zmq
import glob
import time
import shutil
import traceback
from msgpack import unpackb
from subprocess import call
import commands
prog_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
prog_lib_dir = os.path.join(prog_, 'lib')
if prog_lib_dir not in sys.path:
    sys.path.insert(0, prog_lib_dir)
from util import app_abs_path, read_config, write_config, get_file_md5, prog_dir
from mylog import init_aps_logger
from logger import Logger
log = Logger(config_file='conf/client.conf',
             logfile=os.path.join('logs', os.path.basename(os.path.realpath(sys.argv[0])).replace(".py",'.log'))
            )
aps_log = init_aps_logger('apscheduler', './logs/')


class WatchDog(object):

    def __init__(self, opts):
        self.opts = opts
        context = zmq.Context()
        self.sock = context.socket(zmq.SUB)
        self.sock.setsockopt(zmq.SUBSCRIBE, "")
        self.sock.connect("tcp://%(master)s:%(update_port)s" % opts)

    def watch_process(self):
        proc_list = ('ops_agent/agent.pyc',)
        for proc in proc_list:
            try:
                if not os.path.exists(app_abs_path(proc)):
                    log.logger.error("proc file %s is not exists" % app_abs_path(proc))
                    continue
                if not os.popen("pgrep -f %s"%proc).read().strip():
                    # out = os.popen("python %s &" % app_abs_path(proc)).read().strip()
                    out = os.popen("/bin/bash %s restart" % app_abs_path('bin/zops_agent.sh')).read().strip()
                    log.logger.info(out)
                    break
            except:
                log.logger.error(traceback.format_exc())

    def watch_update(self):
        force, new_version, update_fn, fn_md5 = unpackb(self.sock.recv(), encoding='utf-8')
        cur_version = read_config()['version']
        if force == 0 and new_version == cur_version:
            log.logger.info('current version is the latest version')
            return
        retry = 5
        index = 1
        while index <= retry:
            # wget update package and check md5
            ##
            ##
            try:
                shutil.copy(update_fn, os.path.join(prog_dir(), '..'))
                log.logger.info('copy update file done')
            except Exception, e:
                log.logger.error(e)
                index += 1
                continue
            if fn_md5 != get_file_md5(os.path.join(prog_dir(), '..', os.path.basename(update_fn))):
                log.logger.error("file md5 no match")
                index += 1
                continue
            else:
                break
        if index > retry:
            log.logger.error('out of try times')
            return
        ret_code, ret_msg = commands.getstatusoutput("/bin/bash %s/zops_agent.sh stop" % app_abs_path('bin'))
        if ret_code != 0:
            log.logger.error("stop zops_agent fail %s" % ret_msg)
            return
        log.logger.info('stop zops_agent done')
        try:
            self.backup_agent()
        except Exception,e:
            log.logger.error(e)
            call("/bin/bash %s/zops_agent.sh start" % app_abs_path('bin'), shell=True)
            return
        log.logger.info('backup zops_agent done')
        os.chdir(os.path.join(prog_dir(), '..'))
        # commands.getstatusoutput("chattr +i %s" % app_abs_path('conf/client.conf'))
        ret_code, ret_msg = commands.getstatusoutput("tar xf %s --exclude=agent/conf/client.conf" % os.path.basename(update_fn))
        log.logger.info('tar update file done')
        # commands.getstatusoutput("chattr -i %s" % app_abs_path('conf/client.conf'))
        commands.getstatusoutput("rm -f  %s" % os.path.basename(update_fn))
        log.logger.info('remove update package done')
        os.chdir(prog_dir())
        if ret_code != 0:
            log.logger.error(ret_msg)
            call("/bin/bash %s/zops_agent.sh start" % app_abs_path('bin'), shell=True)
            return
        write_config('version', new_version)
        ret_code, ret_msg = commands.getstatusoutput("/bin/bash %s/zops_agent.sh restart" % app_abs_path('bin'))
        if ret_code != 0:
            log.logger.error("restart agent fail %s" % ret_msg)
            return
        log.logger.info('update zops_agent done')

    def backup_agent(self):
        app_dir = os.path.join(prog_, '..')
        src = "%s/agent" % app_dir
        dst = "%s/agent.%s" % (app_dir, int(time.time()))
        backup_list = glob.glob('%s/agent.[0-9]*' % app_dir)
        max_backup = int(self.opts['max_backup'])
        if len(backup_list) >= max_backup:
            for bak in sorted(backup_list, key=lambda x: -int(os.path.basename(x).split('.')[1]))[max_backup - 1:]:
                shutil.rmtree(bak)
        shutil.copytree(src, dst)

if __name__ == '__main__':
    opts = read_config(config_file='conf/client.conf')
    wd = WatchDog(opts)
    #apscheduler.events
    def err_listener(ev):
        if ev.exception:
            aps_log.info('%s error.', str(ev.job))
        else:
            aps_log.info('%s miss', str(ev.job))
    from apscheduler.schedulers.blocking import BlockingScheduler
    from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_MISSED
    from apscheduler.triggers.interval import IntervalTrigger
    sched = BlockingScheduler()
    sched.add_listener(err_listener, EVENT_JOB_ERROR | EVENT_JOB_MISSED)
    sched.add_job(wd.watch_process, IntervalTrigger(seconds=10))
    sched.add_job(wd.watch_update, IntervalTrigger(seconds=10))
    sched.start()