__author__ = 'rsukla'

import socket
import sys     # this module we basically use to exit from the system

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # If socket fails then we will do this
except socket.error, msg:
    print "Failed to create a socket"
    sys.exit(0)

print "socket created"


# SOCK_STREAM refers to TCP protocol
# AF_INET it refers to IPv4

