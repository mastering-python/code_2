# Note: the `grouper` sample is from the Python documentation:
https://docs.python.org/3/library/itertools.html?highlight=chunk#itertools-recipes

>>> import itertools


>>> def grouper(iterable, n, fillvalue=None):
...     '''Collect data into fixed-length chunks or blocks'''
...     args = [iter(iterable)] * n
...     return itertools.zip_longest(*args, fillvalue=fillvalue)

>>> list(grouper('ABCDEFG', 3, 'x'))
[('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]

------------------------------------------------------------------

>>> def chunker(iterable, chunk_size):
...     # Make sure `iterable` is an iterator
...     iterable = iter(iterable)
...
...     def chunk(value):
...         # Make sure not to skip the given value
...         yield value
...         # We already yielded a value so reduce the chunk_size
...         for _ in range(chunk_size - 1):
...             try:
...                 yield next(iterable)
...             except StopIteration:
...                 break
...
...     while True:
...         try:
...             # Check if we're at the end by using `next()`
...             yield chunk(next(iterable))
...         except StopIteration:
...             break


>>> for chunk in chunker('ABCDEFG', 3):
...     for value in chunk:
...         print(value, end=', ')
...     print()
A, B, C,
D, E, F,
G,

------------------------------------------------------------------

>>> import itertools


>>> def chunker(iterable, chunk_size):
...     # Make sure `iterable` is an iterator
...     iterable = iter(iterable)
...
...     while True:
...         # Because islice doesn't know how if the iterable has
...         # been exhausted, we need to manually check here. Alternatively
...         try:
...             value = next(iterable)
...         except StopIteration:
...             return
...         else:
...             sliced = itertools.islice(iterable, chunk_size - 1)
...             # Chain the pre-fetched value and the slice
...             yield itertools.chain([value], sliced)


>>> chunk_size = 3
>>> for chunk in chunker('ABCDEFG', chunk_size):
...     for i, value in enumerate(chunk, 1):
...         print(value, end=', ')
...     print()
A, B, C,
D, E, F,
G,
