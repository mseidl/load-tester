# Load Test server app

import sys
import socket

HOST = socket.gethostname()
PORT = 8001

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, err:
    print "Error opening socket: %s" % str(err[0])

try:
    sock.bind((HOST, PORT))
    print "Socket was bound"
except socket.error, err:
    print "Error binding to port: %s %s" % (str(err[0]), err[1])
    sys.exit()

sock.listen(15)

while True:
    connection, address = sock.accept()
    buff = connection.recv(128)
    if buff > 0:
        print buff
        break

sock.shutdown()
sock.close()
