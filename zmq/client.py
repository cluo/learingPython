__author__ = 'admin'
#REQ应答TCP 必须 等待应答返回，如果只请求不响应,客户端会一直等待返回
import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://127.0.0.1:5000')
socket.connect('tcp://127.0.0.1:6000')
for i in range(10):
    msg  = "msg%s" %i
    socket.send(msg)
    print "sending",msg
    msg_in = socket.recv()
    print msg_in

