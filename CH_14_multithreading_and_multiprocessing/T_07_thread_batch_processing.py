import timeit
import socket
import concurrent.futures


def getaddrinfo(*args):
    # Call getaddrinfo but ignore the given parameter
    socket.getaddrinfo('localhost', None)


def benchmark(threads, n=1000):
    if threads > 1:
        # Create the executor
        with concurrent.futures.ThreadPoolExecutor(threads) \
                as executor:
            executor.map(getaddrinfo, range(n))
    else:
        # Make sure to use `list`. Otherwise the generator will
        # not execute because it is lazy
        list(map(getaddrinfo, range(n)))


if __name__ == '__main__':
    for threads in (1, 10, 50, 100):
        print(f'Testing with {threads} threads and n={10} took: ',
              end='')
        print('{:.1f}'.format(timeit.timeit(
            f'benchmark({threads})',
            setup='from __main__ import benchmark',
            number=10,
        )))
