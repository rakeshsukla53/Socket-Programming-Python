__author__ = 'rsukla'

#The other kind of socket activity is called a SERVER. A server is a system that uses sockets to receive incoming connections and provide them with data.
# It is just the opposite of Client. So www.google.com is a server and your web browser is a client.
# Or more technically www.google.com is a HTTP Server and your web browser is an HTTP client.

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

