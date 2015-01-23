__author__ = 'rsukla'


import socket
import sys
from thread import *

HOST = ''    # it can accept request from every host
PORT = 8888  # unprivileged
x = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "Socket Created"

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print " Not able to bind the socket"
    sys.exit()

s.listen(10)
print " Socket is listening"

def clientthread(conn):

    conn.send("Welcome to the server, and type something")
    while True:
        data = conn.recv(1024)
        reply = data
        if not reply:
            break
        conn.sendall(reply)

    conn.close()

while 1:
    conn, addr = s.accept()
    print "Server is connected with", addr[0], "Port number is", str(addr[1])
    start_new_thread(clientthread, (conn,))

s.close()




