#!/usr/bin/env python
from config import *
import logging
from thread_pool import *
import time
from threshold import Threshold
from xmlrpcload import xmlrpc_call
import socket

hostname = socket.gethostname()

logfile = 'load-test.log'
logging.basicConfig(filename = logfile,
                    format='(%(threadName)-10s) %(message)s',
                    level = logging.DEBUG)

# Store dict of times, which will have keys of the thread count.
times = {}

# Error count
errors = 0

def time_event(function, threads):
    start = time.time()
    function()
    end = time.time()
    times[threads].append(end - start)

if __name__=='__main__':
    # Define max threads to use
    # In range, start, end(plus 1 to include end) and steps
    pool_size = [x for x in range(100, 110, 2)]
    # Create dict with thread sizes to keep track of time
    for _ in pool_size: times[_] = []

    # Define pool mutliplier - this calls the pool_size * multiplier clients
    count = 200

    for i in pool_size:
        pool = ThreadPool(i)
        # Clients is the final goal, so it'll increase the number of threads till this number is 0
        clients = i * count
        while clients:
            # Change to your desired function... 
            pool.add_task(time_event, xmlrpc_call, i )
            clients -= 1
            print i, "    ", clients

        pool.wait_completion()

    for n in pool_size:
        print '%s threads did %s things in %.1f seconds: average is %.2f seconds per thing' % \
                                    (n, len(times[n]), sum(times[n]), sum(times[n])/len(times[n]))
