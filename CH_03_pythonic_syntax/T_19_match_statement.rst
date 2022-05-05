>>> some_variable = 123

>>> match some_variable:
...     case 1:
...         print('Got 1')
...     case 2:
...         print('Got 2')
...     case _:
...         print('Got something else')
Got something else

>>> if some_variable == 1:
...     print('Got 1')
... elif some_variable == 1:
...     print('Got 2')
... else:
...     print('Got something else')
Got something else

##################################################################

>>> some_variable = 123

>>> match some_variable:
...     case 1:
...         print('Got 1')
...     case other:
...         print('Got something else:', other)
Got something else: 123

##################################################################

>>> class Direction:
...     LEFT = -1
...     RIGHT = 1

>>> some_variable = Direction.LEFT

>>> match some_variable:
...     case Direction.LEFT:
...         print('Going left')
...     case Direction.RIGHT:
...         print('Going right')
Going left

##################################################################

>>> class Direction:
...     LEFT = -1
...     UP = 0
...     RIGHT = 1
...     DOWN = 2

>>> some_variable = Direction.LEFT

>>> match some_variable:
...     case Direction.LEFT | Direction.RIGHT:
...         print('Going horizontal')
...     case Direction.UP | Direction.DOWN:
...         print('Going vertical')
Going horizontal

##################################################################

>>> values = -1, 0, 1
>>> for value in values:
...     print('matching', value, end=': ')
...     match value:
...         case negative if negative < 0:
...             print(f'{negative} is smaller than 0')
...         case positive if positive > 0:
...             print(f'{positive} is greater than 0')
...         case _:
...             print('no match')
matching -1: -1 is smaller than 0
matching 0: no match
matching 1: 1 is greater than 0

##################################################################

>>> values = (0, 1), (0, 2), (1, 2)
>>> for value in values:
...     print('matching', value, end=': ')
...     match value:
...         case 0, 1:
...             print('exactly matched 0, 1')
...         case 0, y:
...             print(f'matched 0, y with y: {y}')
...         case x, y:
...             print(f'matched x, y with x, y: {x}, {y}')
matching (0, 1): exactly matched 0, 1
matching (0, 2): matched 0, y with y: 2
matching (1, 2): matched x, y with x, y: 1, 2

##################################################################

>>> def get_uri(*args):
...     # Set defaults so we only have to store changed variables
...     protocol, port, paths = 'https', 443, ()
...     match args:
...         case (hostname,):
...             pass
...         case (hostname, port):
...             pass
...         case (hostname, port, protocol, *paths):
...             pass
...         case _:
...             raise RuntimeError(f'Invalid arguments {args}')
...
...     path = '/'.join(paths)
...     return f'{protocol}://{hostname}:{port}/{path}'

>>> get_uri('localhost')
'https://localhost:443/'
>>> get_uri('localhost', 12345)
'https://localhost:12345/'
>>> get_uri('localhost', 80, 'http')
'http://localhost:80/'
>>> get_uri('localhost', 80, 'http', 'some', 'paths')
'http://localhost:80/some/paths'

##################################################################

>>> values = (0, 1), (0, 2), (1, 2)
>>> for value in values:
...     print('matching', value, end=': ')
...     match value:
...         case 0 as x, (1 | 2) as y:
...             print(f'matched x, y with x, y: {x}, {y}')
...         case _:
...             print('no match')
matching (0, 1): matched x, y with x, y: 0, 1
matching (0, 2): matched x, y with x, y: 0, 2
matching (1, 2): no match

##################################################################

>>> values = dict(a=0, b=0), dict(a=0, b=1), dict(a=1, b=1)
>>> for value in values:
...     print('matching', value, end=': ')
...     match value:
...         case {'a': 0}:
...             print('matched a=0:', value)
...         case {'a': 0, 'b': 0}:
...             print('matched a=0, b=0:', value)
...         case _:
...             print('no match')
matching {'a': 0, 'b': 0}: matched a=0: {'a': 0, 'b': 0}
matching {'a': 0, 'b': 1}: matched a=0: {'a': 0, 'b': 1}
matching {'a': 1, 'b': 1}: no match

##################################################################

>>> class Person:
...     def __init__(self, name):
...         self.name = name

>>> values = Person('Rick'), Person('Guido')
>>> for value in values:
...     match value:
...         case Person(name='Rick'):
...             print('I found Rick')
...         case Person(occupation='Programmer'):
...             print('I found a programmer')
...         case Person() as person:
...             print('I found a person:', person.name)
I found Rick
I found a person: Guido

##################################################################

>>> class Person:
...     def __init__(self, name):
...         self.name = name

>>> value = Person(123)
>>> match value:
...     case Person(name=str() as name):
...         print('Found person with str name:', name)
...     case Person(name=int() as name):
...         print('Found person with int name:', name)
Found person with int name: 123
