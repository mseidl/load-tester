#!/usr/bin/env python
import sys
import logging
import time
from threading import Lock

from thread_pool import ThreadPool, Worker
from xmlrpcload import xmlrpc_call
from config import *
from error import Error
from overload import Overload

logfile = 'load-test.log'
logging.basicConfig(filename = logfile,
                    format='(%(threadName)-10s) %*(hostname) %(message)s',
                    level = logging.DEBUG)

# Overload object to test overloady-ness
ovrld = Overload(max_threshold, overload)
# Store dict of times, which will have keys of the thread count.
times = {}
# Store thread counts that will be run
pool_size = []

# Mutex
mutex = Lock()

# Error count
errors = Error()

# Clients
total_clients = 0
sched_clients = 0

def quit():
    """Report results and exit"""
    print "There were clients scheduled: %s, and %s ran" % (sched_clients, total_clients)
    print ovrld
    print "There were %s errors" % errors.error_count
    for thread_c, time_list in times.iteritems():
        if time_list:
            print '%s threads did %s things in %.1f seconds: average is %.2f seconds per thing' % \
                                    (thread_c, len(time_list), sum(time_list), sum(time_list)/len(time_list))
        else:
            print "Nothing happened with %s threads" % thread_c
    sys.exit()

def time_event(function, threads):
    global errors
    global mutex
    start = time.time()
    function(errors, mutex)
    end = time.time()
    times[threads].append(end - start)

def calculate_needed():
    if ovrld.overloaded:
        max = ovrld.opt_work_threads
    else:
        max = pool_size[-1]
    scheduled = sum(pool_size) * count
    difference = need_count - scheduled
    return difference / max

if __name__=='__main__':
    # Define max threads to use in config file
    # In range, start, end(plus 1 to include end) and steps
    pool_size = [x for x in range(min_thread, max_thread, thread_step)]
    # Create dict with thread sizes to keep track of time
    for thread_count in pool_size: times[thread_count] = []

    for i in pool_size:
        if ovrld.overloaded:
            i = ovrld.opt_work_threads
        if need_count and i == pool_size[-1] \
                or need_count and ovrld.overloaded and i == ovrld.opt_work_threads:
            clients = i * calculate_needed()
        else:
            clients= i * count

        pool = ThreadPool(i)

        # Clients is the final goal, it'll run the thread count for "count" iterations
        # count is from config
        sched_clients += clients
        while clients:
            # Change to your desired function... 
            pool.add_task(time_event, xmlrpc_call, i)
            clients -= 1
            total_clients += 1
            if errors.error_count > errors_threshold:
                quit()
        pool.wait_completion()
        avg_time = sum(times[i]) / len(times[i])
        ovrld.calc_time(avg_time, i)

    quit()
