#!/usr/bin/env python
#-*- coding:utf8 -*-
__author__ = 'linzhonghong'
import os
import sys
import hashlib
import traceback
import random
from functools import wraps
prog_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
prog_lib_dir = os.path.join(prog_, 'lib')
if prog_lib_dir not in sys.path:
    sys.path.insert(0, prog_lib_dir)
import time
import zmq
import pymysql
import payload
from util import MysqlHandler, get_cur_datetime, read_config, post
from db_ar import DBActiveRec
from multiprocessing.pool import ThreadPool
# 设置线程沲的大小，用于异步处理
pool = ThreadPool(processes=16)
from logger import Logger

log = Logger(config_file='conf/server.conf',
             logfile=os.path.join('logs', os.path.basename(os.path.realpath(sys.argv[0])).replace(".py", '.log'))
)

DEFAULT_RETRIES = 3


def retry(max_tries, exceptions=(Exception,), hook=None):
    """Retry calling the decorated function
    """
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            tries = max_tries
            while tries > 1:
                try:
                    return f(*args, **kwargs)
                except exceptions, e:
                    # 防止同时请求
                    time.sleep(random.random()*10)
                    if hook is not None:
                        hook(e)
                    tries -= 1
                    log.logger.error(u'接口%s第%s次调用失败: %s' % (f.__name__, (max_tries-tries), e))
            return f(*args, **kwargs)

        return f_retry  # true decorator
    return deco_retry

class ReqServer(object):
    def __init__(self, opts):
        self.opts = opts
        self.serial = payload.Serial()
        self.mysql_handler = MysqlHandler()
        self.context = zmq.Context()
        self.req = self.context.socket(zmq.REP)
        self.uri = "tcp://%(master)s:%(master_port)s" % self.opts
        self.poller = zmq.Poller()
        self.db = DBActiveRec(cursorclass=pymysql.cursors.DictCursor)

    def __bind(self):
        self.req.bind(self.uri)
        time.sleep(1)

    def do(self, recv):
        if recv['come_from'] == 'HB':
            try:
                value = self.get_assets_by_ip([recv['host_ip']])
                if len(value['rows']) == 0:
                    log.logger.error('ip %s have not device in cmdb' % recv['host_ip'])
                    return
                device = value['rows'][0]
                check_host = self.db.find_by_host_ip(recv['host_ip'], 'ops_hosts')
                log.logger.info(str(device))
                if isinstance(check_host, list) and check_host[0]:
                    exists = True
                else:
                    exists = False
                device['agent_version'] = recv['agent_version']
                items = device.items()
                if exists is True:
                    for k, v in items:
                        if k not in check_host[0] or v is None:
                            device.pop(k)
                    device['update_time'] = get_cur_datetime()
                    self.db.update('ops_hosts', device, {'host_ip': recv['host_ip']}, 1)
                    if self.db.error_msg is not None:
                        log.logger.info(self.db.error_msg)
                if exists is False:
                    columns = [col['Field'] for col in self.db.get_fields('ops_hosts')]
                    for k, v in items:
                        if k not in columns or v is None:
                            device.pop(k)
                    device['host_ip'] = recv['host_ip']
                    log.logger.info(str(device))
                    self.db.insert('ops_hosts', device)
                    if self.db.error_msg is not None:
                        log.logger.info(self.db.error_msg)
                return

            except:
                log.logger.error(traceback.format_exc())
                return

        conn = self.mysql_handler.conn_db()
        if recv['come_from'] == 'task':
            sreq = payload.SREQ("tcp://%s:%s" % (recv['server_ip'], self.opts['client_port']))
            timestamp = int(time.time())
            secret = self.opts.get('secret')
            auth_key = hashlib.md5("%s%s" % (secret, timestamp)).hexdigest()
            load = dict(
                come_from='master',
                func=recv['func'],
                task_id=recv['task_id'],
                url=recv['url'],
                domain=recv['domain'],
                src_dir=recv['src_dir'],
                environment=recv['environment'],
                auth_key=auth_key,
                timestamp=timestamp
            )
            log.logger.info("send task %s to client %s" % (load['task_id'], recv['server_ip']))
            try:
                ret = sreq.send(load)
            except Exception, e:
                log.logger.error(e)
                sqlstr = """
                UPDATE `ops_task` SET `ret_msg`='%s', `task_proc`='%s', `status`=2, `modify_timestamp`='%s' WHERE `task_id`='%s';
                """ % ('send to agent time out', 'send to agent time out', get_cur_datetime(), load['task_id'])
                self.mysql_handler.exec_sql(sqlstr, conn)
            finally:
                self.mysql_handler.close_conn(conn)
        elif recv['come_from'] == 'agent':
            log.logger.info("update task %s state" % recv['task_id'])
            sqlstr = """
            UPDATE `ops_task` SET `ret_msg`='%s', `task_proc`=CONCAT(IFNULL(`task_proc`, ''),'%s\n'), `status`=%s, `modify_timestamp`='%s', `ret_code`=%s WHERE `task_id`='%s';
            """ % (recv['ret_msg'], recv['ret_msg'], recv['status'], get_cur_datetime(), recv['ret_code'], recv['task_id'])
            self.mysql_handler.exec_sql(sqlstr, conn)
            self.mysql_handler.close_conn(conn)
        elif recv['come_from'] == 'task_proc':
            log.logger.info("update task %s process" % recv['task_id'])
            sqlstr = r"""
            UPDATE `ops_task` SET `task_proc`=CONCAT(IFNULL(`task_proc`, ''),'%s\n'), `modify_timestamp`='%s' WHERE `task_id`='%s';
            """ % (pymysql.escape_string(recv['task_proc']), get_cur_datetime(), recv['task_id'])
            self.mysql_handler.exec_sql(sqlstr, conn)
            self.mysql_handler.close_conn(conn)

    def gen_app_key(self, timestamp):
        return hashlib.md5(
            "%s%s%s%s" % (self.opts['app_name'], self.opts['access_num'], self.opts['master'], timestamp)
        ).hexdigest()

    @retry(DEFAULT_RETRIES)
    def get_assets_by_ip(self, ip_list):
        timestamp = int(time.time())
        app_key = self.gen_app_key(timestamp)
        data = {
            "version": "1.0",
            "app_key": app_key,
            "app_name": self.opts['app_name'],
            "operator": 'system',
            "method": "get_device_by_ip",
            "timestamp": timestamp,
            "data": {
                "ip_list": ip_list
            }
        }
        try:
            result = post(self.opts['zcmdb_url'], data)
        except:
            log.logger.error(traceback.format_exc())
            raise Exception, u'zcmdb查询设备接口调用失败'
        if not result:
            raise Exception, u'zcmdb查询设备接口调用失败'
        if result['code'] != 0 and result['code'] != 1104:
            raise Exception, u'zcmdb查询设备接口调用失败，%s' % result['message']
        return result['value']

    def run(self):
        self.__bind()
        while True:
            self.poller.register(self.req, zmq.POLLIN)
            socks = dict(self.poller.poll(60 * 1000))
            if socks:
                if socks.get(self.req) == zmq.POLLIN:
                    recv = self.serial.loads(self.req.recv())
            else:
                continue
            if not recv:
                break
            if 'come_from' not in recv:
                log.logger.error("unknown source")
                self.req.send(self.serial.dumps({'ret': 'unknown source'}))
                continue
            self.req.send(self.serial.dumps({'task_id': recv.get('task_id'), 'ret': 'ok'}))
            pool.apply_async(self.do, (recv, ))

    def destroy(self):
        if self.req.closed is False:
            self.req.setsockopt(zmq.LINGER, 1)
            self.req.close()
        if self.context.closed is False:
            self.context.term()

    def __del__(self):
        self.destroy()


if __name__ == '__main__':
    opts = read_config()
    rs = ReqServer(opts)
    rs.run()