import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # This is basically a TCP Socket

s.connect(("www.google.com", 80)) # Since this is an HTTP request so we are using the TCP port

print 'Socket Created'

