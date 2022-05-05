import sys
import timeit
import argparse
import functools

from sum_of_squares_py import sum_of_squares as sum_py

try:
    from sum_of_squares import sum_of_squares as sum_c
except ImportError:
    print('Please run "python setup.py build install" first')
    sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('repetitions', type=int)
    parser.add_argument('maximum', type=int)
    args = parser.parse_args()

    timer = functools.partial(
        timeit.timeit, number=args.repetitions, globals=globals())

    print(f'Testing {args.repetitions} repetitions with maximum: '
          f'{args.maximum}')

    result = sum_c(args.maximum)
    duration_c = timer('sum_c(args.maximum)')
    print(f'C: {result} took {duration_c:.3f} seconds')

    result = sum_py(args.maximum)
    duration_py = timer('sum_py(args.maximum)')
    print(f'Py: {result} took {duration_py:.3f} seconds')

    print(f'C was {duration_py / duration_c:.1f} times faster')
