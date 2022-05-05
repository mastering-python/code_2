import os
import psutil


def print_usage(message):
    process = psutil.Process(os.getpid())
    usage = process.memory_info().rss / (1 << 20)
    print(f'Memory usage {message}: {usage:.1f} MiB')


def allocate_and_release():
    # Allocate large block of memory
    large_list = list(range(1000000))
    print_usage('after allocation')

    del large_list
    print_usage('after releasing')


print_usage('initial')
allocate_and_release()
allocate_and_release()
