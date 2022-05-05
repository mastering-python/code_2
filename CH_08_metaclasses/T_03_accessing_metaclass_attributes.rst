>>> class Meta(type):
...
...     @property
...     def some_property(cls):
...         return 'property of %r' % cls
...
...     def some_method(self):
...         return 'method of %r' % self


>>> class SomeClass(metaclass=Meta):
...     pass

# Accessing through the class definition

>>> SomeClass.some_property
"property of <class '...SomeClass'>"
>>> SomeClass.some_method
<bound method Meta.some_method of <class '__main__.SomeClass'>>
>>> SomeClass.some_method()
"method of <class '__main__.SomeClass'>"

# Accessing through an instance

>>> some_class = SomeClass()
>>> some_class.some_property
Traceback (most recent call last):
    ...
AttributeError: 'SomeClass' object has no attribute 'some_property'
>>> some_class.some_method
Traceback (most recent call last):
    ...
AttributeError: 'SomeClass' object has no attribute 'some_method'
