#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-23
import gevent
from gevent.queue import Queue
from gevent import Greenlet
from gevent_actors import Actor

__author__ = 'cluo'


class Pinger(Actor):
    def receive(self, message):
        print(message)
        pong.inbox.put('ping')
        gevent.sleep(0)

class Ponger(Actor):
    def receive(self, message):
        print(message)
        ping.inbox.put('pong')
        gevent.sleep(0)

ping = Pinger()
pong = Ponger()
ping.start()
pong.start()
ping.inbox.put('start')
gevent.joinall([ping, pong])