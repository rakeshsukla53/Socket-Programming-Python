__author__ = 'rsukla'

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print "Socket is not created"
    sys.exit(0)

print 'Socket Created'

host = 'www.google.com'

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror, msg:
    print " Unable to resolve the error"
    sys.exit(0)

print remote_ip



# If you want to connect to a remote server, you need a IP Address and Port number

