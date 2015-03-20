class Overload(object):
    """
    Keeps track and calculates how much is getting done on average.
    Also keeps track of if we are putting too much strain on the server.
    """
    def __init__(self, max_threshold = 0, overload = False):
        # How many times can performance get worse before stopping
        self.max_threshold = max_threshold
        # Best result so far
        self.best_work_done = 0
        # Optimal work threads
        self.opt_work_threads = 0
        self.current_sessions = 0
        # How many times has it gotten worse before
        self.current_threshold = 0
        # Take it past peak performance
        self.overload = overload
        # Our current state, have we gone too far!
        self.overloaded = False

    def calc_time(self, avg_time, pool_size):
        work_done = pool_size / avg_time
        if work_done >= best_work_done:
            best_work_done = work_done
            opt_work_threads = pool_size
        elif self.max_threshold:
            self.current_threshold += 1
            if self.current_threshold > self.max_threshold:
                self.overloaded = True
        elif not self.overload:
            self.overloaded = True
        else:
            pass

    def __repr__(self):
        return "Best work was %s with %s threads" % \
                (self.best_work_done, self.opt_work_threads)
