__author__ = 'admin'
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

