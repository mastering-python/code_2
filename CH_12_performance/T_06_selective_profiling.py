import cProfile
import datetime
import functools


def timer(function):
    @functools.wraps(function)
    def _timer(*args, **kwargs):
        start = datetime.datetime.now()
        try:
            return function(*args, **kwargs)
        finally:
            end = datetime.datetime.now()
            print(f'{function.__name__}: {end - start}')
    return _timer


def profiler(function):
    @functools.wraps(function)
    def _profiler(*args, **kwargs):
        profiler = cProfile.Profile()
        try:
            profiler.enable()
            return function(*args, **kwargs)
        finally:
            profiler.disable()
            profiler.print_stats()
    return _profiler


@profiler
def profiled_fibonacci(n):
    return fibonacci(n)


@timer
def timed_fibonacci(n):
    return fibonacci(n)


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    timed_fibonacci(32)
    profiled_fibonacci(32)

