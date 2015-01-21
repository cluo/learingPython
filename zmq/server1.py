__author__ = 'admin'
import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://127.0.0.1:5000')
while True:
    msg = socket.recv()
    print "Got server1",msg
    socket.send(msg)