import gc
import time
import functools


assert time

TIMEIT_TEMPLATE = '''
def run(number):
    {setup}
    start = time.perf_counter()
    for i in range(number):
        {statement}
    stop = time.perf_counter()
    return stop - start
'''


def timeit(statement, setup='', number=1000000, globals_=None):
    # Get or create globals
    globals_ = globals() if globals_ is None else globals_

    # Create the test code so we can separate the namespace
    src = TIMEIT_TEMPLATE.format(
        statement=statement,
        setup=setup,
        number=number,
    )
    # Compile the source
    code = compile(src, '<source>', 'exec')

    # Define locals for the benchmarked code
    locals_ = {}

    # Execute the code so we can get the benchmark fuction
    exec(code, globals_, locals_)

    # Get the run function from locals() which was added by `exec`
    run = functools.partial(locals_['run'], number=number)

    # Disable garbage collection to prevent skewing results
    gc.disable()
    try:
        result = run()
    finally:
        gc.enable()

    return result


if __name__ == '__main__':
    statement = '[x for x in range(100)]'
    print('{:.7f}'.format(timeit(statement, number=1)))
    print('{:.7f}'.format(timeit(statement) / 1000000))
    print('{:.7f}'.format(timeit(statement, number=1)))
    print('{:.7f}'.format(timeit(statement) / 1000000))
