
# Note: Remember to ``pip install pyzmq gevent_zeromq``
import gevent
import zmq

# Global Context
context = zmq.Context()

def server():
    server_socket = context.socket(zmq.REQ)
    server_socket.bind("tcp://127.0.0.1:5000")

    for request in range(1,10):
        server_socket.send("Hello")
        print('Switched to Server for %s' % request)
        # Implicit context switch occurs here
        server_socket.recv()

def client():
    client_socket = context.socket(zmq.REP)
    client_socket.connect("tcp://127.0.0.1:5000")

    for request in range(1,10):

        client_socket.recv()
        print('Switched to Client for %s' % request)
        # Implicit context switch occurs here
        client_socket.send("World")

publisher = gevent.spawn(server)
client    = gevent.spawn(client)

gevent.joinall([publisher, client])



# Switched to Server for 1
# Switched to Server for 2
# Switched to Server for 3
# Switched to Server for 4
# Switched to Server for 5
# Switched to Server for 6
# Switched to Server for 7
# Switched to Server for 8
# Switched to Server for 9