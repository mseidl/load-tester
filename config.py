# Config file
# Get hostname
import socket
hostname = socket.gethostname()

# xmlrpc server, credentials
url = ''
user = ''
password = ''

# Set whether or not to overload server
overload = False
# How far past peak performance should we go (int)
max_threshold = 0

# How many errors to tolerate before we call it quits
errors_threshold = 100

# Thread settings
# Starts at min goes to max in defined steps:
# 2, 6, 2 would yield: 2, 4, 6
min_thread = 2
max_thread = 10
thread_step = 2

# Define pool mutliplier - this calls the pool_size * multiplier clients
# So, for every thread step it will run X times.  
count = 200

# Events done
# This sets a number that will be acheived.  If you have need to do a
# certain number of things, this will do it regardless of thread counts.
need_count = 0
