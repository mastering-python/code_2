import time
import threading


class Timer(threading.Thread):

    def __init__(self, name, steps, interval=0.1):
        self.steps = steps
        self.interval = interval
        # Small gotcha: threading.Thread has a built-in name
        # parameter so be careful not to manually override it
        super().__init__(name=name)

    def run(self):
        '''timer function that sleeps `steps * interval` '''
        for step in range(self.steps):
            print(self.name, step)
            time.sleep(self.interval)


a = Timer(name='a', steps=3)
b = Timer(name='b', steps=3)

# Start the threads
a.start()
# Sleep a tiny bit to keep the output order consistent
time.sleep(0.05)
b.start()
