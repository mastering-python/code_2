>>> import functools


>>> def coroutine(function):
...     # Copy the `function` description with `functools.wraps`
...     @functools.wraps(function)
...     def _coroutine(*args, **kwargs):
...         active_coroutine = function(*args, **kwargs)
...         # Prime the coroutine and make sure we get no values
...         assert not next(active_coroutine)
...         return active_coroutine
...     return _coroutine


>>> @coroutine
... def our_coroutine():
...     while True:
...         print('Waiting for yield...')
...         value = yield
...         print('our coroutine received:', value)

>>> generator = our_coroutine()
Waiting for yield...

>>> generator.send('a')
our coroutine received: a
Waiting for yield...
