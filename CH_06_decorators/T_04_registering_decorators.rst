>>> import collections


>>> class EventRegistry:
...     def __init__(self):
...         self.registry = collections.defaultdict(list)
... 
...     def on(self, *events):
...         def _on(function):
...             for event in events:
...                 self.registry[event].append(function)
...             return function
... 
...         return _on
... 
...     def fire(self, event, *args, **kwargs):
...         for function in self.registry[event]:
...             function(*args, **kwargs)

>>> events = EventRegistry()

>>> @events.on('success', 'error')
... def teardown(value):
...     print(f'Tearing down got: {value}')

>>> @events.on('success')
... def success(value):
...     print(f'Successfully executed: {value}')

>>> events.fire('non-existing', 'nothing to see here')
>>> events.fire('error', 'Oops, some error here')
Tearing down got: Oops, some error here
>>> events.fire('success', 'Everything is fine')
Tearing down got: Everything is fine
Successfully executed: Everything is fine
