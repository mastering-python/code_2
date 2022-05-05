import time
import threading


def timer(name, steps, interval=0.1):
    '''timer function that sleeps `steps * interval` '''
    for step in range(steps):
        print(name, step)
        time.sleep(interval)


# Create the threads declaratively
a = threading.Thread(target=timer, kwargs=dict(name='a', steps=3))
b = threading.Thread(target=timer, kwargs=dict(name='b', steps=3))

# Start the threads
a.start()
# Sleep a tiny bit to keep the output order consistent
time.sleep(0.05)
b.start()
