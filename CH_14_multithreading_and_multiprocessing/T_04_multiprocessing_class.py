import time
import multiprocessing


class Timer(multiprocessing.Process):

    def __init__(self, name, steps, interval=0.1):
        self.steps = steps
        self.interval = interval
        # Similar to threading.Thread, multiprocessing.Process
        # also supports the name parameter but you are not
        # required to use it here.
        super().__init__(name=name)

    def run(self):
        '''timer function that sleeps `steps * interval` '''
        for step in range(self.steps):
            print(self.name, step)
            time.sleep(self.interval)


if __name__ == '__main__':
    a = Timer(name='a', steps=3)
    b = Timer(name='b', steps=3)

    # Start the processs
    a.start()
    # Sleep a tiny bit to keep the output order consistent
    time.sleep(0.1)
    b.start()
