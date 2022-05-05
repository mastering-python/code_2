>>> import abc

>>> class AbstractClass(metaclass=abc.ABCMeta):
...
...     @abc.abstractmethod
...     def some_method(self):
...         raise NotImplemented()


>>> class ConcreteClass(AbstractClass):
...     pass


>>> ConcreteClass()
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class ConcreteClass ...


>>> class ImplementedConcreteClass(ConcreteClass):
...     def some_method():
...         pass


>>> instance = ImplementedConcreteClass()

------------------------------------------------------------------------------

>>> import abc

>>> class AbstractClass(object, metaclass=abc.ABCMeta):
...     @property
...     @abc.abstractmethod
...     def some_property(self):
...         raise NotImplemented()
...
...     @classmethod
...     @abc.abstractmethod
...     def some_classmethod(cls):
...         raise NotImplemented()
...
...     @staticmethod
...     @abc.abstractmethod
...     def some_staticmethod():
...         raise NotImplemented()
...
...     @abc.abstractmethod
...     def some_method():
...         raise NotImplemented()

------------------------------------------------------------------------------

>>> class AbstractMeta(type):
...     def __new__(metaclass, name, bases, namespace):
...         cls = super().__new__(metaclass, name, bases,
...                               namespace)
...         cls.__abstractmethods__ = frozenset(('something',))
...         return cls


>>> class ConcreteClass(metaclass=AbstractMeta):
...     pass

>>> ConcreteClass()
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class ConcreteClass ...

------------------------------------------------------------------------------

>>> import functools


>>> class AbstractMeta(type):
...     def __new__(metaclass, name, bases, namespace):
...         # Create the class instance
...         cls = super().__new__(metaclass, name, bases,
...                               namespace)
...
...         # Collect all local methods marked as abstract
...         abstracts = set()
...         for k, v in namespace.items():
...             if getattr(v, '__abstract__', False):
...                 abstracts.add(k)
...
...         # Look for abstract methods in the base classes and
...         # add them to the list of abstracts
...         for base in bases:
...             for k in getattr(base, '__abstracts__', ()):
...                 v = getattr(cls, k, None)
...                 if getattr(v, '__abstract__', False):
...                     abstracts.add(k)
...
...         # store the abstracts in a frozenset so they cannot be
...         # modified
...         cls.__abstracts__ = frozenset(abstracts)
...
...         # Decorate the __new__ function to check if all
...         # abstract functions were implemented
...         original_new = cls.__new__
...         @functools.wraps(original_new)
...         def new(self, *args, **kwargs):
...             for k in self.__abstracts__:
...                 v = getattr(self, k)
...                 if getattr(v, '__abstract__', False):
...                     raise RuntimeError(
...                         '%r is not implemented' % k)
...
...             return original_new(self, *args, **kwargs)
...
...         cls.__new__ = new
...         return cls


# Create a decorator that sets the `__abstract__` attribute

>>> def abstractmethod(function):
...     function.__abstract__ = True
...     return function


>>> class ConcreteClass(metaclass=AbstractMeta):
...     @abstractmethod
...     def some_method(self):
...         pass

# Instantiating the function, we can see that it functions as the
regular ABCMeta does

>>> ConcreteClass()
Traceback (most recent call last):
    ...
RuntimeError: 'some_method' is not implemented
