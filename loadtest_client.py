# Load Test client app

import sys
import socket

HOST = 'localhost'
PORT = 8001

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, err:
    print "Error creating socket: %s" % str(err[0])

sock.connect((HOST, PORT))

sock.send('Foobar')
