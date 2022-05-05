>>> import functools

>>> def track(function=None, label=None):
...     # Trick to add an optional argument to our decorator
...     if label and not function:
...         return functools.partial(track, label=label)
...
...     print(f'initializing {label}')
...
...     @functools.wraps(function)
...     def _track(*args, **kwargs):
...         print(f'calling {label}')
...         function(*args, **kwargs)
...         print(f'called {label}')
...
...     return _track

>>> @track(label='outer')
... @track(label='inner')
... def func():
...     print('func')
initializing inner
initializing outer

>>> func()
calling outer
calling inner
func
called inner
called outer
