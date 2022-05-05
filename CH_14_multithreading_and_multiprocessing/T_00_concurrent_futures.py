import time
import concurrent.futures


def timer(name, steps, interval=0.1):
    '''timer function that sleeps `steps * interval` '''
    for step in range(steps):
        print(name, step)
        time.sleep(interval)


if __name__ == '__main__':
    # Replace with concurrent.futures.ProcessPoolExecutor for
    # multiple processes instead of threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit the function to the executor with some arguments
        executor.submit(timer, steps=3, name='a')
        # Sleep a tiny bit to keep the output order consistent
        time.sleep(0.05)
        executor.submit(timer, steps=3, name='b')
