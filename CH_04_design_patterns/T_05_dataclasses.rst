>>> spam: int
>>> __annotations__['spam']
<class 'int'>
>>> spam = 'not a number'
>>> __annotations__['spam']
<class 'int'>


>>> import dataclasses

>>> @dataclasses.dataclass
... class Sandwich:
...     spam: int
...     eggs: int = 3

>>> Sandwich(1, 2)
Sandwich(spam=1, eggs=2)

>>> sandwich = Sandwich(4)
>>> sandwich
Sandwich(spam=4, eggs=3)
>>> sandwich.eggs
3
>>> dataclasses.asdict(sandwich)
{'spam': 4, 'eggs': 3}
>>> dataclasses.astuple(sandwich)
(4, 3)

>>> help(dataclasses.dataclass)
Help on ... dataclass(..., *, init=True, repr=True, eq=True, ...

>>> def __init__(self, spam, eggs=3):
...    self.spam = spam
...    self.eggs = eggs


>>> import typing

>>> @dataclasses.dataclass
... class Group:
...     name: str
...     parent: 'Group' = None

>>> @dataclasses.dataclass
... class User:
...     username: str
...     email: str = None
...     groups: typing.List[Group] = None

>>> users = Group('users')
>>> admins = Group('admins', users)
>>> rick = User('rick', groups=[admins])
>>> gvr = User('gvanrossum', 'guido@python.org', [admins])

>>> rick.groups
[Group(name='admins', parent=Group(name='users', parent=None))]

>>> rick.groups[0].parent
Group(name='users', parent=None)
