>>> import functools

>>> def memoize(function):
...     # Store the cache as attribute of the function so we can
...     # apply the decorator to multiple functions without
...     # sharing the cache.
...     function.cache = dict()
...
...     @functools.wraps(function)
...     def _memoize(*args):
...         # If the cache is not available, call the function
...         # Note that all args need to be hashable
...         if args not in function.cache:
...             function.cache[args] = function(*args)
...         return function.cache[args]
...     return _memoize

>>> @memoize
... def fibonacci(n):
...     if n < 2:
...         return n
...     else:
...         return fibonacci(n - 1) + fibonacci(n - 2)

>>> for i in range(1, 7):
...     print(f'fibonacci {i}: {fibonacci(i)}')
fibonacci 1: 1
fibonacci 2: 1
fibonacci 3: 2
fibonacci 4: 3
fibonacci 5: 5
fibonacci 6: 8

>>> fibonacci.__wrapped__.cache
{(1,): 1, (0,): 0, (2,): 1, (3,): 2, (4,): 3, (5,): 5, (6,): 8}

# It breaks keyword arguments:

>>> fibonacci(n=2)
Traceback (most recent call last):
...
TypeError: ... got an unexpected keyword argument 'n'

# Unhashable types don't work as dict keys:

>>> fibonacci([123])
Traceback (most recent call last):
...
TypeError: unhashable type: 'list'


------------------------------------------------------------------------------

>>> import functools

# Create a simple call counting decorator

>>> def counter(function):
...     function.calls = 0
...     @functools.wraps(function)
...     def _counter(*args, **kwargs):
...         function.calls += 1
...         return function(*args, **kwargs)
...     return _counter

# Create a LRU cache with size 3 

>>> @functools.lru_cache(maxsize=3)
... @counter
... def fibonacci(n):
...     if n < 2:
...         return n
...     else:
...         return fibonacci(n - 1) + fibonacci(n - 2)

>>> fibonacci(100)
354224848179261915075

# The LRU cache offers some useful statistics

>>> fibonacci.cache_info()
CacheInfo(hits=98, misses=101, maxsize=3, currsize=3)

# The result from our counter function which is now wrapped both by
our counter and the cache

>>> fibonacci.__wrapped__.__wrapped__.calls
101
