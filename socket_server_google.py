
import socket
import sys

HOST = ''    # it can accept request from every host
PORT = 8888  #unprivileged

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "Socket Created"

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print " Not able to bind the socket"

s.listen(10)
print " Socket is listening"

while 1:
    conn, addr = s.accept()
    print "Server is connected with", addr[0], "Port number is", str(addr[1])

    reply = conn.recv(1024)
    if not reply:
        break
    conn.sendall(reply)

conn.close()
s.close()


