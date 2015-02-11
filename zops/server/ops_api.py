#!/usr/bin/env python
#-*- coding:utf8 -*-
__author__ = 'linzhonghong'

import os
import sys
import web
import json
import time
import hashlib
from lib import payload
from lib.util import MysqlHandler, read_config
from lib.logger import Logger
log = Logger(config_file='conf/server.conf',
             logfile=os.path.join('logs', os.path.basename(os.path.realpath(sys.argv[0])).replace(".py",'.log'))
            )

mysql_handler = MysqlHandler()
opts = read_config()

urls = (
    '/', 'Index'
)

class Index(object):
    def GET(self):
        pass

    def POST(self):
        response = dict(
            version="",
            code="",
            message="",
            value=dict()
        )
        web.header('Content-Type', 'application/json')
        remote_ip = web.ctx.get('ip', '')
        body = json.loads(web.data())
        response['version'] = body.pop('version', '1.0')
        request_key = body.get('request_key')
        if request_key:
            code, message = self.check_acl(request_key, remote_ip)
            if code != 0:
                response['code'] = code
                response['message'] = message
                log.logger.error(
                    "request fail, ip:%s, reason:%s"%(remote_ip, response['message'])
                )
                return json.dumps(response)
        else:
            response['code'] = 1101
            response['message'] = u"鉴权失败：key错误"
            log.logger.error(
                "request fail, ip:%s, reason:%s"%(remote_ip, response['message'])
            )
            return json.dumps(response)
        code, message = self.check_args(body)
        if code != 0:
            response['code'] = code
            response['message'] = message
            log.logger.error(
                "request fail, ip:%s, reason:%s"%(remote_ip, response['message'])
            )
            return json.dumps(response)
        log.logger.info(
            "get request, function:%s, operator:%s, ip:%s"%(body.get('method'), body.get('operator'), remote_ip)
        )
        sreq = payload.SREQ("tcp://%(job_ip)s:%(job_port)s"%opts)
        try:
            ret = sreq.send(body, timeout=2)
        except Exception,e:
            log.logger.error(e)
            log.logger.error(
                "function:%s, execute:fail, reason:timeout"%body.get('method')
            )
            response['code'] = 1003
            response['message'] = u"服务器忙：timeout"
            return json.dumps(response)
        if 'ret' in ret and ret['ret'] == 'ok':
            job_id = ret.get('job_id')
            response['code'] = 0
            response['message'] = u"成功"
            response['value']['job_id'] = job_id
            log.logger.info(
                "function:%s, execute:succ, jod_id:%s"%(body.get('method'), job_id)
            )
        else:
            response['code'] = 1001
            response['message'] = u"系统错误"
            log.logger.error(
                "function:%s, execute:fail, reason:%s"%(body.get('method'), response['message'])
            )
        return json.dumps(response)

    def check_acl(self, request_key, remote_ip):
        conn = mysql_handler.conn_db()
        sqlstr = "SELECT `access_num` FROM `z_acl` WHERE `ip`='%s';"%remote_ip
        res = mysql_handler.exec_sql(sqlstr, conn)
        if res and isinstance(res, tuple):
            access_num = res[0][0]
            if hashlib.md5("%s%s"%(access_num, remote_ip)).hexdigest() != request_key:
                code = 1101
                message = u"鉴权失败：key错误"
            else:
                code = 0
                message = ""
        else:
            code = 1101
            message = u"鉴权失败：该IP未授权"
        return (code, message)

    def check_args(self, body):
        (code, message) = (0, "")
        request_module = body.get('request_module')
        operator = body.get('operator')
        method = body.get('method')
        data = body.get('data')
        arg_dict = dict(
            request_module=request_module,
            operator=operator,
            method=method,
            data=data
        )
        if not all(arg_dict.values()):
            code = 1102
            message = u"参数错误：%s 为空"%','.join([k for k,v in arg_dict.iteritems() if not v])
            return (code, message)
        if method == 'instance_create':
            data_dict = dict(
                hypervisor=data.get('hypervisor'),
                type=data.get('type'),
                max_count=data.get('max_count'),
                volume=data.get('volume'),
                dept_id=data.get('dept_id'),
                department=data.get('department'),
                business1=data.get('business1'),
                business2=data.get('business2'),
                business3=data.get('business3'),
                pri_operator=data.get('pri_operator'),
                bk_operator=data.get('bk_operator'),
                group_id=data.get('group_id'),
                group=data.get('group'),
                alarm_level=data.get('alarm_level'),
                server_statusId=data.get('server_statusId')
            )
            if not all(data_dict.values()):
                code = 1102
                message = u"参数错误：%s 为空"%','.join([k for k,v in data_dict.iteritems() if not v])
                return (code, message)
            volume = data.get('volume')
            if isinstance(volume, list):
                if len(volume) < 2:
                    code = 1102
                    message = u"参数错误：data['volume']必须有2个以上元素"
                    return (code, message)
                for idx, vol in enumerate(volume):
                    vol_dict = dict(
                        img_id=vol.get('img_id'),
                        target=vol.get('target'),
                        type=vol.get('type'),
                        partition_type=vol.get('partition_type'),
                        fstype=vol.get('fstype')
                    )
                    if not all(vol_dict.values()):
                        code = 1102
                        message = u"参数错误：data['volume']第%s个元素的%s 为空"%((idx+1), ','.join([k for k,v in vol_dict.iteritems() if not v]))
                        return (code, message)
            else:
                code = 1102
                message = u"参数错误：data['volume']必须为列表格式"
                return (code, message)
        else:
            data_dict = dict(
                uuid_list=data.get('uuid_list'),
                task_id=data.get('task_id'),
                type=data.get('type')
            )
            if not any(data_dict.values()):
                code = 1102
                message = u"参数错误：data参数内容只支持uuid_list,task_id,type且不为空"
                return (code, message)
            uuid_list = data.get('uuid_list')
            if uuid_list and not isinstance(uuid_list, list):
                code = 1102
                message = u"参数错误：data参数uuid_list元素必须为列表"
                return (code, message)

        return (code, message)

    def handler(self, data):

        time.sleep(10)
        print data,type(data)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()