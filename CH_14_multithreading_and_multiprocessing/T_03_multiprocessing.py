import time
import multiprocessing


def timer(name, steps, interval=0.1):
    '''timer function that sleeps `steps * interval` '''
    for step in range(steps):
        print(name, step)
        time.sleep(interval)


if __name__ == '__main__':
    # Create the processes declaratively
    a = multiprocessing.Process(target=timer, kwargs=dict(name='a', steps=3))
    b = multiprocessing.Process(target=timer, kwargs=dict(name='b', steps=3))

    # Start the processes
    a.start()
    # Sleep a tiny bit to keep the output order consistent
    time.sleep(0.1)
    b.start()

