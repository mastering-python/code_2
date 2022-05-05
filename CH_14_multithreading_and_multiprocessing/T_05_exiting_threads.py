import time
import threading


class Forever(threading.Thread):

    def __init__(self):
        self.stop = threading.Event()
        super().__init__()

    def run(self):
        while not self.stop.is_set():
            # Do whatever you need to do here
            time.sleep(0.1)


thread = Forever()
thread.start()
# Do whatever you need to do here
thread.stop.set()
thread.join()
