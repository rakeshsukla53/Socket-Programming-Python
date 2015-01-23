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

# Abhi humko remote ip mil gaya hain , now we want to connect to that ip through a port number

s.connect((remote_ip, 80))

print "Socket connected to", host, "on remote ip", remote_ip

#It creates a socket and then connects. Try connecting to a port different from port 80
# and you should not be able to connect which indicates that the port is not open for connection. This logic can be used to build a port scanner.

#The concept of "connections" apply to SOCK_STREAM/TCP type of sockets. Connection means a reliable "stream" of data such
# that there can be multiple such streams each having communication of its own. Think of this as a pipe which is not interfered by data from other pipes. Another important property of stream connections is that packets have an "order" or "sequence".

#Other sockets like UDP , ICMP , ARP dont have a concept of "connection". These are non-connection based communication.
## Which means you keep sending or receiving packets from anybody and everybody.

