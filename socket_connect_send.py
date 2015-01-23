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

message = "GET / HTTP/1.1\r\n\r\n"  # this is actually an HTTP command to fetch the main page

try:
    s.sendall(message)   #sendall is basically used to send data to the remote server
except socket.error, msg:
    print "Message can't be sent"
    sys.exit(0)

print "Message sent successfully "

reply = s.recv(4096)

print reply # Jis socket is connect kiya hain ..use socket se hain toh wapas receive karega

s.close()

