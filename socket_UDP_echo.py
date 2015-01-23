__author__ = 'rsukla'

import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

PORT = 6000

try:
    s.bind(('', PORT))
except socket.error, msg:
    print "Unable to bind the socket"

while 1:
    data, addr = s.recvfrom(1024)

    if not data:
        break
    print "The address that is now connected is ", addr
    s.sendto(data, addr)


s.close()







