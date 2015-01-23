__author__ = 'rsukla'

import socket
import sys

host = ''  # All avaliable privilege interfaces
port = 8888  # Non - privilege ports

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket is created"

try:
    s.bind((host, port))
except socket.error, msg:
    print "Not able to bind the socket"
    sys.exit(0)

print "socket bind complete"

s.listen(10)

#The parameter of the function listen is called backlog. I
# t controls the number of incoming connections that are kept "waiting" if the program is already busy.
# So by specifying 10, it means that if 10 connections are already waiting to be processed,
# then the 11th connection request shall be rejected. This will be more clear after checking socket_accept.

print " Socket is listening "

