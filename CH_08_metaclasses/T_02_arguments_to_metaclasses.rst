>>> class AddClassAttributeMeta(type):
...     def __init__(metaclass, name, bases, namespace, **kwargs):
...         # The kwargs should not be passed on to the
...         # type.__init__
...         type.__init__(metaclass, name, bases, namespace)
...
...     def __new__(metaclass, name, bases, namespace, **kwargs):
...         for k, v in kwargs.items():
...             # setdefault so we don't overwrite attributes
...             namespace.setdefault(k, v)
...
...         return type.__new__(metaclass, name, bases, namespace)


>>> class WithArgument(metaclass=AddClassAttributeMeta, a=1234):
...     pass


>>> WithArgument.a
1234
>>> with_argument = WithArgument()
>>> with_argument.a
1234

------------------------------------------------------------------

>>> class AddClassAttribute:
...     def __init_subclass__(cls, **kwargs):
...         super().__init_subclass__()
...
...         for k, v in kwargs.items():
...             setattr(cls, k, v)


>>> class WithAttribute(AddClassAttribute, a=1234):
...     pass


>>> WithAttribute.a
1234
>>> with_attribute = WithAttribute()
>>> with_attribute.a
1234
