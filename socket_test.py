__author__ = 'rsukla'


import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

PORT = 7000

try:
    s.bind(('', PORT))
except socket.error, msg:
    print "Unable to bind the socket"

while 1:
    data, addr = s.recvfrom(1024)
    x = ('127.0.0.1', 42836)

    if not data:
        break
    print "The address that is now connected is ", addr
    s.sendto(data, x)
    s.sendto(data, addr)

s.close()

