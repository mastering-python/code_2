import sys
import datetime
from dask import distributed


def busy_wait(n):
    while n > 0:
        n -= 1


def benchmark_dask(client):
    start = datetime.datetime.now()

    # Run up to 1 million
    n = 1000000
    tasks = int(sys.argv[1])  # get number of tasks from argv

    # Submit the tasks to Dask
    futures = client.map(busy_wait, [n] * tasks, pure=False)
    # Gather the results, this blocks until the results are ready
    client.gather(futures)

    duration = datetime.datetime.now() - start
    per_second = int(tasks / duration.total_seconds())
    print(f'{tasks} tasks at {per_second} per '
          f'second, total time: {duration}')


if __name__ == '__main__':
    benchmark_dask(distributed.Client(processes=False))
