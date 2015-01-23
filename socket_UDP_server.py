
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PORT = 5000
s.bind(('', PORT))

while 1:
    data = s.recv(1024)
    print 'The data you enter is', data

#The u flag indicates the udp protocol. Whatever message we send, should display on the server terminal.

#UDP doesn't have any connect or accept protocol


