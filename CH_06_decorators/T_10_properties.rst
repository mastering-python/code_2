>>> import functools

>>> class Sandwich:
...     def get_eggs(self):
...         print('getting eggs')
...         return self._eggs
...
...     def set_eggs(self, eggs):
...         print('setting eggs to %s' % eggs)
...         self._eggs = eggs
...
...     def delete_eggs(self):
...         print('deleting eggs')
...         del self._eggs
...
...     eggs = property(get_eggs, set_eggs, delete_eggs)
...
...     @property
...     def spam(self):
...         print('getting spam')
...         return self._spam
...
...     @spam.setter
...     def spam(self, spam):
...         print('setting spam to %s' % spam)
...         self._spam = spam
...
...     @spam.deleter
...     def spam(self):
...         print('deleting spam')
...         del self._spam
...
...     @functools.cached_property
...     def bacon(self):
...         print('getting bacon')
...         return 'bacon!'

>>> sandwich = Sandwich()
>>> sandwich.eggs = 123
setting eggs to 123
>>> sandwich.eggs
getting eggs
123
>>> del sandwich.eggs
deleting eggs
>>> sandwich.bacon
getting bacon
'bacon!'
>>> sandwich.bacon
'bacon!'


------------------------------------------------------------------------------

>>> class Property(object):
...     def __init__(self, fget=None, fset=None, fdel=None):
...         self.fget = fget
...         self.fset = fset
...         self.fdel = fdel
... 
...     def __get__(self, instance, cls):
...         if instance is None:
...             # Redirect class (not instance) properties to self
...             return self
...         elif self.fget:
...             return self.fget(instance)
... 
...     def __set__(self, instance, value):
...         self.fset(instance, value)
... 
...     def __delete__(self, instance):
...         self.fdel(instance)
... 
...     def getter(self, fget):
...         return Property(fget, self.fset, self.fdel)
... 
...     def setter(self, fset):
...         return Property(self.fget, fset, self.fdel)
... 
...     def deleter(self, fdel):
...         return Property(self.fget, self.fset, fdel)

>>> class Sandwich:
...     @Property
...     def eggs(self):
...         return self._eggs
...
...     @eggs.setter
...     def eggs(self, value):
...         self._eggs = value
...
...     @eggs.deleter
...     def eggs(self):
...         del self._eggs

>>> sandwich = Sandwich()
>>> sandwich.eggs = 5
>>> sandwich.eggs
5

------------------------------------------------------------------------------

>>> class Sandwich(object):
...     def __init__(self):
...         self.registry = {}
...
...     def __getattr__(self, key):
...         print('Getting %r' % key)
...         return self.registry.get(key, 'Undefined')
...
...     def __setattr__(self, key, value):
...         if key == 'registry':
...             object.__setattr__(self, key, value)
...         else:
...             print('Setting %r to %r' % (key, value))
...             self.registry[key] = value
...
...     def __delattr__(self, key):
...         print('Deleting %r' % key)
...         del self.registry[key]


>>> sandwich = Sandwich()

>>> sandwich.a
Getting 'a'
'Undefined'

>>> sandwich.a = 1
Setting 'a' to 1

>>> sandwich.a
Getting 'a'
1

>>> del sandwich.a
Deleting 'a'
