>>> def sandwich(bacon: float, eggs: int):
...     pass

------------------------------------------------------------------------------

>>> import inspect
>>> import functools

>>> def enforce_type_hints(function):
...     # Construct the signature from the function which contains
...     # the type annotations
...     signature = inspect.signature(function)
... 
...     @functools.wraps(function)
...     def _enforce_type_hints(*args, **kwargs):
...         # Bind the arguments and apply the default values
...         bound = signature.bind(*args, **kwargs)
...         bound.apply_defaults()
... 
...         for key, value in bound.arguments.items():
...             param = signature.parameters[key]
...             # The annotation should be a callable
...             # type/function so we can cast as validation
...             if param.annotation:
...                 bound.arguments[key] = param.annotation(value)
... 
...         return function(*bound.args, **bound.kwargs)
... 
...     return _enforce_type_hints

>>> @enforce_type_hints
... def sandwich(bacon: float, eggs: int):
...     print(f'bacon: {bacon!r}, eggs: {eggs!r}')

>>> sandwich(1, 2)
bacon: 1.0, eggs: 2
>>> sandwich(3, 'abc')
Traceback (most recent call last):
...
ValueError: invalid literal for int() with base 10: 'abc'
