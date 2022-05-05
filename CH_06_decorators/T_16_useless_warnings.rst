>>> import warnings
>>> import functools

>>> def ignore_warning(warning, count=None):
...     def _ignore_warning(function):
...         @functools.wraps(function)
...         def __ignore_warning(*args, **kwargs):
...             # Execute the code while catching all warnings
...             with warnings.catch_warnings(record=True) as ws:
...                 # Catch all warnings of the given type
...                 warnings.simplefilter('always', warning)
...                 # Execute the function
...                 result = function(*args, **kwargs)
... 
...             # Re-warn all warnings beyond the expected count
...             if count is not None:
...                 for w in ws[count:]:
...                     warnings.warn(w.message)
... 
...             return result
...         return __ignore_warning
...     return _ignore_warning

>>> @ignore_warning(DeprecationWarning, count=1)
... def spam():
...     warnings.warn('deprecation 1', DeprecationWarning)
...     warnings.warn('deprecation 2', DeprecationWarning)


# Note, we use catch_warnings here because doctests normally
capture the warnings quietly

>>> with warnings.catch_warnings(record=True) as ws:
...     spam()
...
...     for i, w in enumerate(ws):
...         print(w.message)
deprecation 2
