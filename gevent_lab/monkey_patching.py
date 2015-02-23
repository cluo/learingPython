import socket
print(socket.socket)
print("After monkey patch")
from gevent import monkey
monkey.patch_socket()
print(socket.socket)
import select
print(select.select)
monkey.patch_select()
print("After monkey patch")
print(select.select)


# <class 'socket._socketobject'>
# After monkey patch
# <class 'gevent.socket.socket'>
# <built-in function select>
# After monkey patch
# <function select at 0x10215e410>