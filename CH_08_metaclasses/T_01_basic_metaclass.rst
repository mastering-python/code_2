# The metaclass definition, note the inheritance of type instead
of object

>>> class MetaSandwich(type):
...
...     # Notice how the __new__ method has the same arguments
...     # as the type function we used earlier?
...     def __new__(metaclass, name, bases, namespace):
...         name = 'SandwichCreatedByMeta'
...         bases = (int,) + bases
...         namespace['lettuce'] = 1
...         return type.__new__(metaclass, name, bases, namespace)


# First, the regular Sandwich:

>>> class Sandwich(object):
...     pass

>>> Sandwich.__name__
'Sandwich'
>>> issubclass(Sandwich, int)
False
>>> Sandwich.lettuce
Traceback (most recent call last):
    ...
AttributeError: type object 'Sandwich' has no attribute 'lettuce'


# Now the meta-Sandwich

>>> class Sandwich(object, metaclass=MetaSandwich):
...     pass

>>> Sandwich.__name__
'SandwichCreatedByMeta'
>>> issubclass(Sandwich, int)
True
>>> Sandwich.lettuce
1
