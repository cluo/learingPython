#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
redis的操作

"""
import redis
from redis.connection import UnixDomainSocketConnection

redisPool = redis.ConnectionPool(connection_class=UnixDomainSocketConnection, path = '/tmp/redis.sock')
r = redis.Redis(connection_pool = redisPool)
p = r.pipeline(transaction=False)

#放入队列
def redis_lpush(data,queue="VM_MONITOR"):
    r.lpush(queue,data)

#取出队列
def redis_rpop(queue="VM_MONITOR"):
    ret = r.rpop(queue)
    return ret

#队列取值
def redis_get(queue="VM_MONITOR"):
    ret = r.lindex(queue,0)
    return ret
