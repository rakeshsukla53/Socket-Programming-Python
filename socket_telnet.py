__author__ = 'rsukla'

import socket, sys, string, select

#define the main function

if __name__ == "__main__":


    if(len(sys.argv) < 3):
        print "Usage: python telnet.py hostname port"
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect((host, port))
    except socket.error, msg:
        print "Not able to connect to the socket"
        sys.exit()

    print "connected to the remote server"

    while 1:

        socket_list = [sys.stdin, s]
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            if sock == s:
                data = sock.recv(1024)
                if not data:
                    print "Connection closed"   #read the data coming to the socket
                else:
                    sys.stdout.write(data)   #print data
            else:
                msg = sys.stdin.readline() #user entered some values
                s.send(msg)

