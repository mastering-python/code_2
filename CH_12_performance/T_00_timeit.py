import timeit


def test_list():
    return list(range(10000))


def test_list_comprehension():
    return [i for i in range(10000)]


def test_append():
    x = []
    for i in range(10000):
        x.append(i)

    return x


def test_insert():
    x = []
    for i in range(10000):
        x.insert(0, i)

    return x


def benchmark(function, number=100, repeat=10):
    # Measure the execution times. Passing the globals() is an
    # easy way to make the functions available.
    times = timeit.repeat(function, number=number,
                          globals=globals())
    # The repeat function gives `repeat` results so we take the
    # min() and divide it by the number of runs
    time = min(times) / number
    print(f'{number} loops, best of {repeat}: {time:9.6f}s :: ',
          function.__name__)


def autorange_benchmark(function):

    def print_result(number, time_taken):
        # The autorange function keeps trying until the total
        # runtime (time_taken) reaches 0.2 seconds. To get the
        # time per run we need to divide it by the number of runs
        time = time_taken / number
        name = function.__name__
        print(f'{number} loops, average: {time:9.6f}s :: {name}')

    # Measure the execution times. Passing the globals() is an
    # easy way to make the functions available.
    timer = timeit.Timer(function, globals=globals())
    timer.autorange(print_result)


if __name__ == '__main__':
    benchmark(test_list)
    benchmark(test_list_comprehension)
    benchmark(test_append)
    benchmark(test_insert)
