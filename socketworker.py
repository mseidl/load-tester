from Queue import Queue
from threading import Thread
import copy

class SocketWorker(Thread):
    def __init__(self, inq, outq):
        super(SocketWorker, self).__init__()
        self.inq = inq
        self.outq = outq

    def run_client(self):
        while not self.stoprequest.isSet():
            try:
                print "foo"
                self.outq.put("foo", block=False)
            except Queue.Empty:
                continue

    def run_server(self):
        while not self.stoprequest.isSet():
            try:
                print "foo"
                self.outq.put("foo", block=False)
            except Queue.Empty:
                continue

    def join(self):
        self.stoprequest.set()
        super(SocketWorker, self).join()
