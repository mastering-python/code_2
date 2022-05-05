import time
import multiprocessing


class Forever(multiprocessing.Process):

    def run(self):
        while True:
            # Do whatever you need to do here
            time.sleep(0.1)


if __name__ == '__main__':
    process = Forever()
    process.start()

    # Kill our "unkillable" process
    process.terminate()

    # Wait for 10 seconds to properly exit
    process.join(10)

    # If it still didn't exit, kill it
    if process.exitcode is None:
        process.kill()
