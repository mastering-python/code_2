>>> import abc

>>> class CustomList(abc.ABC):
...     '''This class implements a list-like interface'''


>>> class CustomInheritingList(list, abc.ABC):
...     '''This class implements a list-like interface'''


>>> issubclass(list, CustomList)
False
>>> issubclass(list, CustomInheritingList)
False

>>> CustomList.register(list)
<class 'list'>

# We can't make it go both ways however

>>> CustomInheritingList.register(list)
Traceback (most recent call last):
    ...
RuntimeError: Refusing to create an inheritance cycle

>>> issubclass(list, CustomList)
True
>>> issubclass(list, CustomInheritingList)
False

# We need to inherit list to make it work the other way around

>>> issubclass(CustomList, list)
False
>>> isinstance(CustomList(), list)
False
>>> issubclass(CustomInheritingList, list)
True
>>> isinstance(CustomInheritingList(), list)
True

------------------------------------------------------------------------------

>>> import abc

>>> class UniversalClass(abc.ABC):
...    @classmethod
...    def __subclasshook__(cls, subclass):
...        return True


>>> issubclass(list, UniversalClass)
True
>>> issubclass(bool, UniversalClass)
True
>>> isinstance(True, UniversalClass)
True
>>> issubclass(UniversalClass, bool)
False
