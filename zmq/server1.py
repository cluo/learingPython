__author__ = 'admin'
#-*- code:utf8 -*-
#REQ应答TCP 必须 等待应答返回，如果只请求不响应,客户端会一直等待返回
import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://127.0.0.1:5000')

while True:
    msg = socket.recv()
    print "Got server1",msg
    socket.send(msg)