# Config file
import socket

# Get hostname
hostname = socket.gethostname()

# xmlrpc server, credentials
url = ''
user = ''
password = ''

# Set whether or not to overload server
overload = False

# How many errors to tolerate before we call it quits
errors_threshold = 100
