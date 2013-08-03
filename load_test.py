#!/usr/bin/env python

import os
import logging
from datetime import datetime as dt
from thread_pool import *
import time

logfile = 'register.log'
logging.basicConfig(filename = logfile,
                    format='(%(threadName)-10s) %(message)s',
                    level = logging.DEBUG)

times = {}


def plot():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    #thread count
    tc = [x for x in times.keys()]
    #average time
    av = [sum(times[x])/ len(times[x]) for x in times.keys()]
    #make tuple
    data = zip(tc, av)
    #labels
    la = [l for l, t in data]
    bar = plt.bar([x for x in range(1, int(max(av)))], av, 1, color='y')
    plt.ylabel('time in seconds')
    plt.xlabel('thread count')

    plt.savefig('test.png')



def do_nothing(threads):
    start = time.time()
    time.sleep(.2)
    end = time.time()
    times[threads].append(end - start)


if __name__=='__main__':
    #define max threads to use
    #in range, start, end(plus 1 to include end) and steps
    pool_size = [x for x in range(1, 4, 2)]
    #create dict with thread sizes to keep track of time
    for _ in pool_size: times[_] = []

    #define pool mutliplier - this registers the pool_size * multiplier clients
    count = 4

    for i in pool_size:
        pool = ThreadPool(i)
        #clients is the final goal, so it'll increase the number of threads till this number is 0
        clients = i * count
        while clients:
            #Change do_nothing to your desired function... 
            pool.add_task(do_nothing, i)
            clients -= 1

        pool.wait_completion()

    for n in pool_size:
        print '%s threads did %s things in %.1f seconds: average is %.2f seconds per thing' % \
                                    (n, len(times[n]), sum(times[n]), sum(times[n])/len(times[n]))


