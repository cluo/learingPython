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
             logfile=os.path.join('logs', os.path.basename(os.path.realpath(sys.argv[0])).replace(".py", '.log'))
)

mysql_handler = MysqlHandler()
opts = read_config()


def test(data):
    sreq = payload.SREQ("tcp://%(job_ip)s:%(job_port)s" % opts)
    try:
        ret = sreq.send(data, timeout=2)
    except Exception, e:
        print e


if __name__ == '__main__':
    # data = {
    #     "job_id": "201408271734511409132091",
    #     "job_type": 0,
    #     "release_type": "jetty",
    #     "url": "http://172.16.10.213:8081/artifactory/libs-release-local/com/meizu/www/www-web/1.0.2-RC05/www-web-1.0.2-RC05.war",
    #     "ip_list": [
    #         "172.16.10.20"
    #     ]
    #
    # }
# load = {
#     "data": {
#         "job_id": "201408271734511409132091",
#         "job_type": 0,
#         "release_type": "jetty",
#         "domain": "bbs.meizu.com",
#         "url": "http://172.16.10.213:8081/artifactory/libs-release-local/com/meizu/www/www-web/1.0.2-RC05/www-web-1.0.2-RC05.war",
#         "ip_list": [
#             "172.16.10.20"
#         ]
#     }
# }
    data = {
        "version": "1.0",
        "request_key": "XXXXXXX",
        "request_module": "XXX",
        "operator": "XXX",
        "data": {
            "job_id": "201408271734511409132091",
            "job_type": 0,
            "release_type": "jetty",
            "url": "http://172.16.10.213:8081/artifactory/libs-release-local/com/meizu/www/www-web/1.0.2-RC05/www-web-1.0.2-RC05.war",
            "ip_list": [
                "172.16.10.20"
            ]
        }

    }
    test(data)