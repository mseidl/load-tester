
class Threshold(object):
    def __init__(self, max_threshold = 0):
        self.max_threshold = max_threshold     
   
    best_avg_time = 0
    current_sessions = 0
    current_threshold = 0
   
    def calc_time(self, time, pool_size):
        avg_time = time / pool_size
        if avg_time < best_avg_time:
            best_avg_time = avg_time
        else:
            current_threshold += 1
