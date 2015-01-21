__author__ = 'admin'
import zmq
from random import choice
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5000")

countries = ["a",'b','c','d']
events = ['aa', 'bb', 'cc' ,'dd']
while True:
    msg = choice(countries) + " " + choice(events)
    print "->",msg
    socket.send(msg)