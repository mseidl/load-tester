#!/usr/bin/env python
from config import *
import logging
from thread_pool import *
import time
from threading import Lock
from threshold import Threshold
from xmlrpcload import xmlrpc_call
from error import Error

logfile = 'load-test.log'
logging.basicConfig(filename = logfile,
                    format='(%(threadName)-10s) %*(hostname) %(message)s',
                    level = logging.DEBUG)

# Store dict of times, which will have keys of the thread count.
times = {}
# Store thread counts that will be run
pool_size = []

# Mutex
mutex = Lock()

# Error count
errors = Error()

def quit():
    """Report results and exit"""

    for thread_c, time_list in times.iteritems():
        if time_list:
            print '%s threads did %s things in %.1f seconds: average is %.2f seconds per thing' % \
                                    (thread_c, len(time_list), sum(time_list), sum(time_list)/len(time_list))
        else:
            print "Nothing happened with %s threads" % thread_c

def time_event(function, threads):
    global errors
    global mutex
    start = time.time()
    function(errors, mutex)
    end = time.time()
    times[threads].append(end - start)

if __name__=='__main__':
    # Define max threads to use
    # In range, start, end(plus 1 to include end) and steps
    pool_size = [x for x in range(min_thread, max_thread, thread_step)]
    # Create dict with thread sizes to keep track of time
    for thread_count in pool_size: times[thread_count] = []

    for i in pool_size:
        pool = ThreadPool(i)
        # Clients is the final goal, so it'll increase the number of threads till this number is 0
        clients = i * count
        while clients:
            # Change to your desired function... 
            pool.add_task(time_event, xmlrpc_call, i )
            clients -= 1
            if errors.error_count > errors_threshold:
                quit()
        pool.wait_completion()

    quit()
