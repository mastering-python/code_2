import timeit
import multiprocessing


def triangle_number_local(n):
    total = 0
    for i in range(n + 1):
        total += i

    return total


def bench_local(n, count):
    with multiprocessing.Pool() as pool:
        results = pool.imap_unordered(
            triangle_number_local,
            (n for _ in range(count)),
        )
        print('Sum:', sum(results))


class Shared:
    pass


def initializer(shared_value):
    Shared.value = shared_value


def triangle_number_shared(n):
    for i in range(n + 1):
        with Shared.value.get_lock():
            Shared.value.value += i


def triangle_number_shared_efficient(n):
    total = 0
    for i in range(n + 1):
        total += i

    with Shared.value.get_lock():
        Shared.value.value += total


def bench_shared(n, count):
    shared_value = multiprocessing.Value('i', 0)

    # We need to explicitly share the shared_value. On Unix you
    # can work around this by forking the process, on Windows it
    # would not work otherwise
    pool = multiprocessing.Pool(
        initializer=initializer,
        initargs=(shared_value,),
    )

    iterable = (n for _ in range(count))
    list(pool.imap_unordered(triangle_number_shared, iterable))
    print('Sum:', shared_value.value)

    pool.close()


def triangle_number_namespace(namespace, lock, n):
    for i in range(n + 1):
        with lock:
            namespace.total += i


def triangle_number_namespace_efficient(namespace, lock, n):
    total = 0
    for i in range(n + 1):
        total += i

    with lock:
        namespace.total += i


def namespace_example():
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()
    namespace.spam = 123
    namespace.eggs = 456


def bench_manager(n, count):
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()
    namespace.total = 0
    lock = manager.Lock()

    with multiprocessing.Pool() as pool:
        list(pool.starmap(
            triangle_number_namespace_efficient,
            # WARNING: the following function is slow
            # triangle_number_namespace,
            ((namespace, lock, n) for _ in range(count)),
        ))
        print('Sum:', namespace.total)


if __name__ == '__main__':
    n = 1000
    count = 100
    number = 5

    functions = 'bench_local', 'bench_shared', 'bench_manager'
    for function in functions:
        statement = f'{function}(n={n}, count={count})'
        result = timeit.timeit(
            statement, number=number,
            setup=f'from __main__ import {function}',
        )
        print(f'{statement}: {result:.3f}')

