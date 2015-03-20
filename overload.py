
class Overload(object):
    """
    Keeps track and calculates how much is getting done on average.
    """
    def __init__(self, max_threshold = 0, overload = False):
        # How many times can performance get worse before stopping
        self.max_threshold = max_threshold
        # Best result so far
        self.best_work_done = 0
        self.current_sessions = 0
        # How many times has it gotten worse before
        self.current_threshold = 0
        # Take it past peak performance
        self.overload = overload

    def calc_time(self, avg_time, pool_size):
        work_done = pool_size / avg_time
        if work_done >= best_work_done:
            best_work_done = work_done
            return True
        elif self.max_threshold != 0:
            self.current_threshold += 1
            if self.current_threshold > self.max_threshold and not self.overload:
                return False
