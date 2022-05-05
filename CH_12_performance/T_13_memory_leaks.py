import tracemalloc


class SomeClass:
    pass


if __name__ == '__main__':
    # Initialize some variables to ignore them from the leak
    # detection
    n = 100000

    tracemalloc.start()
    # Your application should initialize here

    snapshot_a = tracemalloc.take_snapshot()
    instances = []

    # This code should be the memory leaking part
    for i in range(n):
        a = SomeClass()
        b = SomeClass()
        # Circular reference. a references b, b references a
        a.b = b
        b.a = a
        # Force Python to keep the object in memory for now
        instances.append(a)

    # Clear the list of items again. Now all memory should be
    # released, right?
    del instances
    snapshot_b = tracemalloc.take_snapshot()

    statistics = snapshot_b.compare_to(snapshot_a, 'lineno')
    for statistic in statistics[:10]:
        print(statistic)
