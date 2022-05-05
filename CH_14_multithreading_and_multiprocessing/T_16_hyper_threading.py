import timeit
import multiprocessing


def busy_wait(n):
    while n > 0:
        n -= 1


def benchmark(n, processes, tasks):
    with multiprocessing.Pool(processes=processes) as pool:
        # Execute the busy_wait function `tasks` times with
        # parameter n
        pool.map(busy_wait, [n for _ in range(tasks)])
    # Create the executor


if __name__ == '__main__':
    n = 100000
    tasks = 128
    for exponent in range(6):
        processes = int(2 ** exponent)
        statement = f'benchmark({n}, {processes}, {tasks})'
        result = timeit.timeit(
            statement,
            number=5,
            setup='from __main__ import benchmark',
        )
        print(f'{statement}: {result:.3f}')
