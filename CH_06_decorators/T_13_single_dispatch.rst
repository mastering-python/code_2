>>> import functools

>>> @functools.singledispatch
... def show_type(argument):
...     print(f'argument: {argument}')

>>> @show_type.register(int)
... def show_int(argument):
...     print(f'int argument: {argument}')

>>> @show_type.register
... def show_float(argument: float):
...     print(f'float argument: {argument}')

>>> show_type('abc')
argument: abc

>>> show_type(123)
int argument: 123

>>> show_type(1.23)
float argument: 1.23

-----------------------------------------------------------------

>>> import functools

>>> registry = dict()

>>> def register(function):
...     # Fetch the first type from the type annotation but be
...     # careful not to overwrite the `type` function
...     type_ = next(iter(function.__annotations__.values()))
...     # Emulate the Python 3.10+ inspect.get_annotations()
...     if isinstance(type_, str):
...         type_ = eval(type_)
...     registry[type_] = function
...
...     @functools.wraps(function)
...     def _register(argument):
...         # Fetch the function using the type of argument, and
...         # fall back to the main function
...         new_function = registry.get(type(argument), function)
...         return new_function(argument)
...
...     return _register

>>> @register
... def show_type(argument: any):
...     print(f'argument: {argument}')

>>> @register
... def show_int(argument: int):
...     print(f'int argument: {argument}')

>>> show_type('abc')
argument: abc

>>> show_type(123)
int argument: 123

-----------------------------------------------------------------

>>> import json
>>> import functools


>>> @functools.singledispatch
... def write_as_json(file, data):
...     json.dump(data, file)


>>> @write_as_json.register(str)
... @write_as_json.register(bytes)
... def write_as_json_filename(file, data):
...     with open(file, 'w') as fh:
...         write_as_json(fh, data)


>>> data = dict(a=1, b=2, c=3)
>>> write_as_json('test1.json', data)
>>> write_as_json(b'test2.json', 'w')
>>> with open('test3.json', 'w') as fh:
...     write_as_json(fh, data)

-----------------------------------------------------------------

>>> write_as_json.registry.keys() == set((bytes, object, str))
True
