>>> import itertools

>>> some_list = list(range(1000))
>>> some_list[:5]
[0, 1, 2, 3, 4]
>>> list(itertools.islice(some_list, 5))
[0, 1, 2, 3, 4]

>>> some_list[10:20:2]
[10, 12, 14, 16, 18]
>>> list(itertools.islice(some_list, 10, 20, 2))
[10, 12, 14, 16, 18]

------------------------------------------------------------------

>>> def islice(iterable, start, stop=None, step=1):
...     # `islice` has signatures: `islice(iterable, stop)` and:
...     # `islice(iterable, start, stop[, step])`
...     # `fill` stop with `start` if needed
...     if stop is None and step == 1 and start is not None:
...         start, stop = 0, start
...
...     # create an iterator and discard the first `start` items
...     iterator = iter(iterable)
...     for _ in range(start):
...         next(iterator)
...
...     # enumerate the iterator making `i` start at `start`
...     for i, item in enumerate(iterator, start):
...         # stop when we've reached `stop` items
...         if i >= stop:
...             return
...         # use modulo `step` to discard non-matching items
...         if i % step:
...             continue
...         yield item

>>> list(islice(range(1000), 10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> list(islice(range(1000), 900, 920, 2))
[900, 902, 904, 906, 908, 910, 912, 914, 916, 918]

>>> list(islice(range(1000), 900, 910))
[900, 901, 902, 903, 904, 905, 906, 907, 908, 909]
