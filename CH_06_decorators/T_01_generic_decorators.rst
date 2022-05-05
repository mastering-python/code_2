>>> import functools

>>> def decorator(function):
...    @functools.wraps(function)
...    def _decorator(*args, **kwargs):
...        a, b = args
...        return function(a, b + 5)
...
...    return _decorator

>>> @decorator
... def func(a, b):
...     return a + b

>>> func(1, 2)
8

>>> func(a=1, b=2)
Traceback (most recent call last):
...
ValueError: not enough values to unpack (expected 2, got 0)


>>> def add(a, b, /):
...     return a + b

>>> add(a=1, b=2)
Traceback (most recent call last):
...
TypeError: add() got some positional-only arguments passed ...



>>> def add(*, a, b):
...     return a + b

>>> add(1, 2)
Traceback (most recent call last):
...
TypeError: add() takes 0 positional arguments but 2 were given



>>> import inspect
>>> import functools

>>> def decorator(function):
...    # Use the inspect module to get function signature. More
...    # about this in the logging chapter
...    signature = inspect.signature(function)
... 
...    @functools.wraps(function)
...    def _decorator(*args, **kwargs):
...        # Bind the arguments to the given *args and **kwargs.
...        # If you want to make arguments optional use
...        # signature.bind_partial instead.
...        bound = signature.bind(*args, **kwargs)
...
...        # Apply the defaults so b is always filled
...        bound.apply_defaults()
...
...        # Extract the filled arguments. If the amount of
...        # arguments is still expected to be fixed you can use
...        # tuple unpacking: `a, b = bound.arguments.values()`
...        a = bound.arguments['a']
...        b = bound.arguments['b']
...        return function(a, b + 5)
...
...    return _decorator

>>> @decorator
... def func(a, b=3):
...     return a + b

>>> func(1, 2)
8

>>> func(a=1, b=2)
8

>>> func(a=1)
9
