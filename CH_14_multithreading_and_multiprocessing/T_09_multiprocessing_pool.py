import timeit
import functools
import multiprocessing
import concurrent.futures


def triangle_number(n):
    total = 0
    for i in range(n + 1):
        total += i

    return total


def bench_mp(n, count, chunksize):
    with multiprocessing.Pool() as pool:
        # Generate a generator like [n, n, n, ..., n, n]
        iterable = (n for _ in range(count))
        list(pool.imap_unordered(triangle_number, iterable,
                                 chunksize=chunksize))


def bench_ft(n, count, chunksize):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Generate a generator like [n, n, n, ..., n, n]
        iterable = (n for _ in range(count))
        list(executor.map(triangle_number, iterable,
                          chunksize=chunksize))


if __name__ == '__main__':
    timer = functools.partial(timeit.timeit, number=5)

    n = 1000
    chunksize = 50
    for count in (100, 1000, 10000):
        # Using <6 formatting for consistent alignment
        args = ', '.join((
            f'n={n:<6}',
            f'count={count:<6}',
            f'chunksize={chunksize:<6}',
        ))
        time_mp = timer(
            f'bench_mp({args})',
            setup='from __main__ import bench_mp',
        )
        time_ft = timer(
            f'bench_ft({args})',
            setup='from __main__ import bench_ft',
        )

        print(f'{args} mp: {time_mp:.2f}, ft: {time_ft:.2f}')
