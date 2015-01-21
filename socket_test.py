import socket, sys
port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print dir(socket.socket)
try:
    s.connect(host, port)
except socket.gaierror,e:
    print 'error connecteing to server %s' % e
    sys.exit(1)
s.sendall(filename+'\r\n')
while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)

