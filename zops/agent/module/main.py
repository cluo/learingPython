#!/usr/bin/env python
#-*- coding:utf8 -*-
__author__ = 'linzhonghong'
import os
import sys
import traceback
prog_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
prog_lib_dir = os.path.join(prog_, 'lib')
if prog_lib_dir not in sys.path:
    sys.path.insert(0, prog_lib_dir)
from util import get_cur_datetime, send_to_master, read_config, Command
from logger import Logger
import payload

log = Logger(config_file='conf/client.conf', logfile='logs/moudule.log')
opts = read_config(config_file='conf/client.conf')

def jetty(**kwargs):
    log.logger.info(str(kwargs))
    try:
        task_id = kwargs['task_id']
        url = kwargs['url']
        src_dir = kwargs['src_dir']
        domain = kwargs['domain']
        environment = kwargs['environment']
    except:
        log.logger.error(traceback.format_exc())
        return 0
    sreq = payload.SREQ("tcp://%(master)s:%(master_port)s"%opts)
    load = dict(
        come_from='task_proc',
        task_id=task_id,
        task_proc='%s 开始更新war包' % get_cur_datetime(),
    )
    send_to_master(sreq, load)
    pkg = url.split('/')[-1]
    business = url.split('/')[-3]
    try:
        if environment == 0:
            run_script = "/mnt/app_shell/meizuyw/release/zops/publish.sh"
        elif environment == 1:
            run_script = "/mnt/app_shell/meizuyw/release/zops/publish_gray.sh"
        else:
            load['task_proc'] = '%s 更新失败：指定环境错误'%(get_cur_datetime())
            send_to_master(sreq, load)
            return 0
        run_cmd = "/bin/bash %s jetty %s %s %s"%(run_script, business, os.path.join(src_dir, pkg),domain)
        log.logger.info(run_cmd)
        cmd = Command(run_cmd)
        status, output = cmd.run()
        os.system("chmod -R 755 /data/log/jetty")
        os.system("chmod -R 755 /data/jetty/webapps")
    except Exception,e:
        status = -1
        output = e
    if status == 0:
        load['task_proc'] = '%s 更新完毕\n%s'%(get_cur_datetime(), output)
    else:
        load['task_proc'] = '%s 更新失败：%s'%(get_cur_datetime(), output)
    send_to_master(sreq, load)
    return not status

def task(**kwargs):
    log.logger.info(str(kwargs))
    try:
        task_id = kwargs['task_id']
        url = kwargs['url']
        src_dir = kwargs['src_dir']
        environment = kwargs['environment']
    except:
        log.logger.error(traceback.format_exc())
        return 0
    sreq = payload.SREQ("tcp://%(master)s:%(master_port)s"%opts)
    load = dict(
        come_from='task_proc',
        task_id=task_id,
        task_proc='%s 开始更新zip包' % get_cur_datetime(),
    )
    send_to_master(sreq, load)
    pkg = url.split('/')[-1]
    business = url.split('/')[-3]
    try:
        if environment == 0:
            run_script = "/mnt/app_shell/meizuyw/release/zops/task.sh"
        elif environment == 1:
            run_script = "/mnt/app_shell/meizuyw/release/zops/task_gray.sh"
        else:
            load['task_proc'] = '%s 更新失败：指定环境错误'%(get_cur_datetime())
            send_to_master(sreq, load)
            return 0
        run_cmd = "/bin/bash %s %s %s"%(run_script, business, os.path.join(src_dir, pkg))
        log.logger.info(run_cmd)
        cmd = Command(run_cmd)
        status, output = cmd.run()
    except Exception,e:
        status = -1
        output = e
    if status == 0:
        load['task_proc'] = '%s 更新完毕\n%s'%(get_cur_datetime(), output)
    else:
        load['task_proc'] = '%s 更新失败：%s'%(get_cur_datetime(), output)
    send_to_master(sreq, load)
    return not status

def static(**kwargs):
    log.logger.info(str(kwargs))
    try:
        task_id = kwargs['task_id']
        url = kwargs['url']
        src_dir = kwargs['src_dir']
        environment = kwargs['environment']
    except:
        log.logger.error(traceback.format_exc())
        return 0
    sreq = payload.SREQ("tcp://%(master)s:%(master_port)s"%opts)
    load = dict(
        come_from='task_proc',
        task_id=task_id,
        task_proc='%s 开始更新zip包' % get_cur_datetime(),
    )
    send_to_master(sreq, load)
    pkg = url.split('/')[-1]
    try:
        if environment == 0:
            run_script = "/mnt/app_shell/meizuyw/release/zops/static.sh"
        elif environment == 1:
            run_script = "/mnt/app_shell/meizuyw/release/zops/static_gray.sh"
        else:
            load['task_proc'] = '%s 更新失败：指定环境错误'%(get_cur_datetime())
            send_to_master(sreq, load)
            return 0
        run_cmd = "/bin/bash %s %s"%(run_script, os.path.join(src_dir, pkg))
        log.logger.info(run_cmd)
        cmd = Command(run_cmd)
        status, output = cmd.run()
        log.logger.info(output)
    except Exception,e:
        status = -1
        output = e
    if status == 0:
        load['task_proc'] = '%s 更新完毕\n%s'%(get_cur_datetime(), output)
    else:
        load['task_proc'] = '%s 更新失败：%s'%(get_cur_datetime(), output)
    send_to_master(sreq, load)
    return not status

def kive(**kwargs):
    log.logger.info(str(kwargs))
    try:
        task_id = kwargs['task_id']
        url = kwargs['url']
        src_dir = kwargs['src_dir']
        environment = kwargs['environment']
    except:
        log.logger.error(traceback.format_exc())
        return 0
    sreq = payload.SREQ("tcp://%(master)s:%(master_port)s"%opts)
    load = dict(
        come_from='task_proc',
        task_id=task_id,
        task_proc='%s 开始更新zip包' % get_cur_datetime(),
    )
    send_to_master(sreq, load)
    pkg = url.split('/')[-1]
    business = url.split('/')[-3]
    try:
        if environment == 0:
            run_script = "/mnt/app_shell/meizuyw/release/zops/kive.sh"
        elif environment == 1:
            run_script = "/mnt/app_shell/meizuyw/release/zops/kive_gray.sh"
        else:
            load['task_proc'] = '%s 更新失败：指定环境错误'%(get_cur_datetime())
            send_to_master(sreq, load)
            return 0
        run_cmd = "/bin/bash %s %s %s"%(run_script, business, os.path.join(src_dir, pkg))
        log.logger.info(run_cmd)
        cmd = Command(run_cmd)
        status, output = cmd.run()
    except Exception,e:
        status = -1
        output = e
    if status == 0:
        load['task_proc'] = '%s 更新完毕\n%s'%(get_cur_datetime(), output)
    else:
        load['task_proc'] = '%s 更新失败：%s'%(get_cur_datetime(), output)
    send_to_master(sreq, load)
    return not status

def php(**kwargs):
    log.logger.info(str(kwargs))
    try:
        task_id = kwargs['task_id']
        url = kwargs['url']
        src_dir = kwargs['src_dir']
        environment = kwargs['environment']
    except:
        log.logger.error(traceback.format_exc())
        return 0
    sreq = payload.SREQ("tcp://%(master)s:%(master_port)s"%opts)
    load = dict(
        come_from='task_proc',
        task_id=task_id,
        task_proc='%s 开始更新svn' % get_cur_datetime(),
    )
    send_to_master(sreq, load)
    pkg = url.split('/')[-1]
    business = url.split('/')[-3]
    try:
        if environment == 0:
            run_script = "/mnt/app_shell/meizuyw/release/zops/flymebbs.sh"
        elif environment == 1:
            run_script = "/mnt/app_shell/meizuyw/release/zops/flymebbs_gray.sh"
        else:
            load['task_proc'] = '%s 更新失败：指定环境错误'%(get_cur_datetime())
            send_to_master(sreq, load)
            return 0
        run_cmd = "/bin/bash %s %s %s"%(run_script, business, os.path.join(src_dir, pkg))
        log.logger.info(run_cmd)
        cmd = Command(run_cmd)
        status, output = cmd.run()
    except Exception,e:
        status = -1
        output = e
    if status == 0:
        load['task_proc'] = '%s 更新完毕\n%s'%(get_cur_datetime(), output)
    else:
        load['task_proc'] = '%s 更新失败：%s'%(get_cur_datetime(), output)
    send_to_master(sreq, load)
    return not status

def do_iptables(**kwargs):
    log.logger.info(str(kwargs))
    try:
        task_id = kwargs['task_id']
        action = kwargs['action']
    except:
        log.logger.error(traceback.format_exc())
        return 0
    try:
        if action == 'up':
            run_script = "/mnt/app_shell/meizuyw/release/zops/do_iptables.sh up"
        elif action == 'down':
            run_script = "/mnt/app_shell/meizuyw/release/zops/do_iptables.sh down"
        else:
            return 0
        run_cmd = "/bin/bash %s" % run_script
        log.logger.info(run_cmd)
        cmd = Command(run_cmd)
        status, output = cmd.run()
    except Exception, e:
        status = -1
    return not status