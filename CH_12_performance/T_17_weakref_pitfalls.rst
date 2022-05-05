>>> import weakref

>>> weakref.ref(dict(a=123))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot create weak reference to 'dict' object
>>> weakref.ref([1, 2, 3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot create weak reference to 'list' object
>>> weakref.ref('test')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot create weak reference to 'str' object
>>> weakref.ref(b'test')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot create weak reference to 'bytes' object
>>> a = weakref.WeakValueDictionary(a=123)
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'int' object

>>> class CustomDict(dict):
...     pass

>>> weakref.ref(CustomDict())
<weakref at 0x...; dead>

>>> class SomeClass:
...     def __init__(self, name):
...         self.name = name

>>> a = SomeClass('a')
>>> b = weakref.proxy(a)
>>> b.name
'a'
>>> del a
>>> b.name
Traceback (most recent call last):
    ...
ReferenceError: weakly-referenced object no longer exists
