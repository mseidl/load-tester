class Error(object):
    def __init__(self):
        self.error_count = 0

    def inc(self):
        self.error_count += 1
