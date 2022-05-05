>>> def decorator(function):
...     return function

>>> def add(a, b):
...     return a + b

>>> add = decorator(add)


>>> @decorator
... def add(a, b):
...     return a + b


>>> import functools

>>> def decorator(function):
...    # This decorator makes sure we mimic the wrapped function
...    @functools.wraps(function)
...    def _decorator(a, b):
...        # Pass the modified arguments to the function
...        result = function(a, b + 5)
...
...        # Logging the function call
...        name = function.__name__
...        print(f'{name}(a={a}, b={b}): {result}')
...
...        # Return a modified result
...        return result + 4
...
...    return _decorator

>>> @decorator
... def func(a, b):
...     return a + b

>>> func(1, 2)
func(a=1, b=2): 8
12
