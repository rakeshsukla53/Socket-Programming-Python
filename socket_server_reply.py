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
    sys.exit()

print "socket bind complete"

s.listen(10)

print " Socket is listening "

conn, addr = s.accept()  # Ab accept kar le

print 'connected with ', addr[0], 'Port', addr[1]

data = conn.recv(1024)   # Jo receive kiya hain usko wapas reply karde
conn.sendall(data)

conn.close()
s.close()