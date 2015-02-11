#!/usr/bin/env python
#-*- coding:utf8 -*-
__author__ = 'linzhonghong'
import os
import sys
prog_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
prog_lib_dir = os.path.join(prog_, 'lib')
if prog_lib_dir not in sys.path:
    sys.path.insert(0, prog_lib_dir)
import datetime
import commands
import traceback
import time
import zmq
import gevent
from gevent import monkey
monkey.patch_all()
import payload
from util import get_cur_datetime, read_config, clean_proc, mysql_opts
import pymysql
from db import MysqlHandler
import multiprocessing
import signal
from logger import Logger
log = Logger(config_file='conf/server.conf',
             logfile=os.path.join('logs', os.path.basename(os.path.realpath(sys.argv[0])).replace(".py",'.log'))
            )


class JobHandler(multiprocessing.Process):
    def __init__(self, opts, data, job_id='', mod_type='main'):
        super(JobHandler, self).__init__()
        self.dir_suf = lambda :"{0:%Y%m%d}".format(datetime.datetime.now())
        self.tasks = []
        self.task_count = len(self.tasks)
        self.max_error_task = 0
        self.opts = opts
        self.data = data
        self.mod_type = mod_type
        self.mysql_handler = MysqlHandler()
        self.serial = payload.Serial()

    def run(self):
        try:
            analysis_data = self.data
            data_info = analysis_data['data']
            self.job_id = data_info['job_id']
            self.job_type = int(data_info['job_type'])
            release_type = data_info['release_type']
            domain = data_info['domain']
            url = data_info['url'].strip()
            environment = int(data_info.get('environment', 0))
            ip_list = data_info['ip_list']
        except Exception,e:
            log.logger.error('analysis data fail, please check the data format')
            log.logger.error(e)
            return
        log.logger.info(str(data_info))
        conn = self.mysql_handler.conn_db()
        sqlstr = """
        UPDATE `ops_job` SET `modify_timestamp`='%s', `status`=3  WHERE `job_id`='%s';
        """%(get_cur_datetime(), self.job_id)
        self.mysql_handler.exec_sql(sqlstr, conn)

        if release_type in ['jetty', 'task', 'static', 'kive']:
            # 根据任务类型把包下载到本地
            dist_dir = os.path.join(self.opts['pkg_dir'], release_type, self.dir_suf())
            if not os.path.isdir(dist_dir):
                os.makedirs(dist_dir)
            try:
                os.chdir(dist_dir)
            except Exception,e:
                log.logger.error(e)
                sqlstr = """
                UPDATE `ops_job` SET `ret_msg`='%s', `modify_timestamp`='%s', `ret_code`=%s, `status`=5  WHERE `job_id`='%s';
                """%(u'目录切换失败', get_cur_datetime(), 1001, self.job_id)
                self.mysql_handler.exec_sql(sqlstr, conn)
                self.mysql_handler.close_conn(conn)
                return
            if os.path.exists(os.path.join(dist_dir, os.path.basename(url))) is False:
                ret_code, ret_msg = commands.getstatusoutput("wget %s"%url)
                if ret_code != 0:
                    log.logger.error("%s"%ret_msg)
                    sqlstr = """
                    UPDATE `ops_job` SET `ret_msg`='%s', `modify_timestamp`='%s', `ret_code`=%s, `status`=5  WHERE `job_id`='%s';
                    """%(pymysql.escape_string("包下载失败:%s"%ret_msg[:200]), get_cur_datetime(), 1001, self.job_id)
                    log.logger.info(sqlstr)
                    self.mysql_handler.exec_sql(sqlstr, conn)
                    self.mysql_handler.close_conn(conn)
                    return
            else:
                log.logger.info("package %s is exists, no need to download" % os.path.join(dist_dir, os.path.basename(url)))
        elif release_type == 'php':
            dist_dir = ''
        else:
            sqlstr = """
            UPDATE `ops_job` SET `ret_msg`='%s', `modify_timestamp`='%s', `ret_code`=%s, `status`=5  WHERE `job_id`='%s';
            """%(u'错误的发布类型', get_cur_datetime(), 1001, self.job_id)
            self.mysql_handler.exec_sql(sqlstr, conn)
            self.mysql_handler.close_conn(conn)
            return
        if not isinstance(ip_list, list):
            sqlstr = """
            UPDATE `ops_job` SET `ret_msg`='%s', `modify_timestamp`='%s', `ret_code`=%s, `status`=5  WHERE `job_id`='%s';
            """%(u'作业ip列表格式错误', get_cur_datetime(), 1001, self.job_id)
            self.mysql_handler.exec_sql(sqlstr, conn)
            self.mysql_handler.close_conn(conn)
            return
        for ip in ip_list:
            if not ip: continue
            self.tasks.append(
                dict(
                    come_from='task',
                    job_id=self.job_id,
                    task_type=self.job_type,
                    task_id="{0:%Y%m%d%H%M%S%f}".format(datetime.datetime.now()),
                    server_ip=ip,
                    url=url,
                    domain=domain,
                    src_dir=dist_dir,
                    environment=environment,
                    func='%s.%s'%(self.mod_type, release_type)
                )
            )
        log.logger.info("job %s has %s tasks"%(self.job_id, len(self.tasks)))
        thread_list = []
        for task_info in self.tasks:
            thread_list.append(gevent.spawn(self.create_task, task_info))
        sqlstr = """
        UPDATE `ops_job` SET `ret_msg`='%s', `modify_timestamp`='%s', `ret_code`=%s, `status`=4  WHERE `job_id`='%s';
        """%(u'作业接收成功', get_cur_datetime(), 0, self.job_id)
        self.mysql_handler.exec_sql(sqlstr, conn)
        self.mysql_handler.close_conn(conn)
        #
        gevent.joinall(thread_list)

    def create_task(self, task_info):
        task = TaskHandler(self.opts)
        task.create_task(task_info)

    def __del__(self):
        clean_proc(self)

class TaskHandler(object):
    def __init__(self, opts):
        self.opts = opts
        self.task_state = 0
        self.serial = payload.Serial()
        self.mysql_handler = MysqlHandler()

    def analysis_task(self, task_info):
        task_info.update(dict(
            create_timestamp=get_cur_datetime(),
            modify_timestamp=get_cur_datetime()
        ))
        return task_info

    def create_task(self, task_info):
        task_info = self.analysis_task(task_info)
        sqlstr = """
        INSERT INTO `ops_task`(`task_id`,`task_type`,`server_ip`,`job_id`,`modify_timestamp`,`status`)
        VALUES('%(task_id)s', %(task_type)s, '%(server_ip)s', '%(job_id)s',  '%(modify_timestamp)s', 0);
        """%task_info
        conn = self.mysql_handler.conn_db()
        self.mysql_handler.exec_sql(sqlstr, conn)
        # 检查该虚拟机是否正在被操作，比较恶心的实现，重新连接了一次mysql
        sqlstr = """
        SELECT * FROM `ops_task` WHERE `server_ip`='%(server_ip)s' AND `status`=0 AND `task_id`!='%(task_id)s';
        """%task_info
        tmp_conn = pymysql.connect(**mysql_opts())
        cur = tmp_conn.cursor()
        count = cur.execute(sqlstr)
        cur.close()
        tmp_conn.close()
        if count > 0:
            sqlstr = """
            UPDATE `ops_task` SET `ret_msg`='%s', `task_proc`='%s', `modify_timestamp`='%s', `ret_code`=%s, `status`=2  WHERE `task_id`='%s';
            """%(u'该IP正在执行任务', u'该IP正在执行任务', get_cur_datetime(), 1103, task_info['task_id'])
            self.mysql_handler.exec_sql(sqlstr, conn)
            self.mysql_handler.close_conn(conn)
            return
        sreq = payload.SREQ("tcp://%(master)s:%(master_port)s"%self.opts)
        try:
            ret = sreq.send(task_info)
        except Exception,e:
            log.logger.error(e)
            sqlstr = """
            UPDATE `ops_task` SET `ret_msg`='%s', `task_proc`='%s', `status`=2, `modify_timestamp`='%s' WHERE `task_id`='%s';
            """%('send to master time out', 'send to master time out', get_cur_datetime(), task_info['task_id'])
            self.mysql_handler.exec_sql(sqlstr, conn)
            self.mysql_handler.close_conn(conn)
            return
        if 'task_id' in ret:
            if task_info['task_id'] == ret['task_id']:
                if ret['ret'] == 'ok':
                    sqlstr = """
                    UPDATE `ops_task` SET `ret_msg`='%s', `modify_timestamp`='%s' WHERE `task_id`='%s';
                    """%('send to master succ', get_cur_datetime(), ret['task_id'])
                else:
                    sqlstr = """
                    UPDATE `ops_task` SET `ret_msg`='%s', `status`=0, `modify_timestamp`='%s' WHERE `task_id`='%s';
                    """%('unknown state', get_cur_datetime(), ret['task_id'])
                self.mysql_handler.exec_sql(sqlstr, conn)

        self.mysql_handler.close_conn(conn)

    def dispatch_task(self):
        pass

    def process_dispatch_task_result(self):
        pass

    def poll_task_state(self):
        pass

    def process_poll_task_state_result(self):
        pass

    def process_expire(self):
        pass

class JobServer(object):
    def __init__(self, opts):
        self.opts = opts
        self.serial = payload.Serial()
        self.context = zmq.Context()
        self.job = self.context.socket(zmq.REP)
        self.uri = "tcp://%(job_ip)s:%(job_port)s"%self.opts

    def __bind(self):
        self.job.bind(self.uri)
        time.sleep(1)

    def run(self):
        self.__bind()
        while True:
            try:
                body = self.serial.loads(self.job.recv())
            except:
                log.logger.error(traceback.format_exc())
                continue
            self.job.send(self.serial.dumps({'ret':'ok'}))
            job_handler = JobHandler(self.opts, body)
            job_handler.start()
            def sigterm_clean(signum, frame):
                clean_proc(job_handler)
                try:
                    os.kill(os.getpid(),signal.SIGKILL)
                except OSError:
                    pass
            signal.signal(signal.SIGTERM, sigterm_clean)

    def destroy(self):
        if self.job.closed is False:
            self.job.setsockopt(zmq.LINGER, 1)
            self.job.close()
        if self.context.closed is False:
            self.context.term()

    def __del__(self):
        self.destroy()

if __name__ == '__main__':
    opts = read_config()
    jobsvr = JobServer(opts)
    jobsvr.run()
