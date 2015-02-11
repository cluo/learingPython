#!/usr/bin/env python
#-*- coding:utf8 -*-
__author__ = 'linzhonghong'
import os
import sys
import zmq
import time
from msgpack import packb
import pymysql
import multiprocessing
# prog_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# prog_lib_dir = os.path.join(prog_, 'lib')
# if prog_lib_dir not in sys.path:
#     sys.path.insert(0, prog_lib_dir)
from lib.util import mysql_opts, app_abs_path, get_file_md5
from lib.util import read_config
from lib.logger import Logger
log = Logger(config_file='conf/server.conf',
             logfile=os.path.join('logs', os.path.basename(os.path.realpath(sys.argv[0])).replace(".py",'.log'))
            )

class Publisher(multiprocessing.Process):
    """
    @note: 通过子进程方式，下发agent版本信息给客户端
    """
    def __init__(self, opts, m_opts, force_update=0):
        """

        @param opts: 配置项
        @param m_opts: mysql专有配置项
        @param force_update: 是否强制agent更新该版本，1为强制，0为非强制，默认为0
        """
        super(Publisher, self).__init__()
        self.opts = opts
        self.m_opts = m_opts
        self.force = force_update

    def run(self):
        context = zmq.Context(1)
        pub_sock = context.socket(zmq.PUB)
        # pub_sock.setsockopt(zmq.SNDHWM, 200)
        pub_sock.bind("tcp://%(master)s:%(update_port)s" % self.opts)
        time.sleep(1)
        agent_info = (0, '0.0.0', 0)
        sleeping = lambda :time.sleep(20)
        while 1:
            try:
                conn = pymysql.connect(**self.m_opts)
                cur = conn.cursor()
                count = cur.execute("SELECT `agent_id`, `version`, `flag` FROM `ops_agent` WHERE `agent_id`=(SELECT MAX(`agent_id`) FROM `ops_agent`);")
                if count==1:
                    # (2, '0.0.1', 0)
                   agent_info = cur.fetchone()
                cur.close()
                conn.close()
            except Exception, e:
                log.logger.error(e)
                sleeping()
                continue
            # if agent_info[2] == 0:
            #     log.logger.info("version %s doesn't need to be update"%agent_info[1])
            #     sleeping()
            #     continue
            # update_file = app_abs_path("src/agent-%s.tar.gz"%agent_info[1])
            update_file = os.path.join(self.opts.get('update_version_dir'), "agent-%s.tar.gz"%agent_info[1])
            if not os.path.isfile(update_file):
                log.logger.error("lack of update file: %s"%update_file)
                sleeping()
                continue
            update_file_md5 = get_file_md5(update_file)
            log.logger.info("publish update file: agent-%s.tar.gz#%s"%(agent_info[1], update_file_md5))
            pub_sock.send(packb([self.force, agent_info[1], update_file, update_file_md5], use_bin_type=True))
            sleeping()
            if self.force == 1:
                break

if __name__ == '__main__':
    opts = read_config()
    m_opts = mysql_opts()
    publish = Publisher(opts, m_opts, 0)
    publish.start()
    publish.join()