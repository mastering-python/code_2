
>>> a = 123
>>> b = 'test'
>>> c = True

------------------------------------------------------------------

>>> def pow(base: int, exponent: int) -> int:
...     return base ** exponent

>>> help(pow)
Help on function pow in module __main__:
<BLANKLINE>
pow(base: int, exponent: int) -> int
<BLANKLINE>

>>> pow.__annotations__
{'base': <class 'int'>,
 'exponent': <class 'int'>,
 'return': <class 'int'>}

>>> pow(2, 10)
1024
>>> pow(pow(9, 2) + pow(19, 2) / 22, 0.25) 
3.1415926525826463

------------------------------------------------------------------

>>> import typing

>>> int_or_float = typing.Union[int, float]

>>> def pow(base: int, exponent: int) -> int_or_float:
...     return base ** exponent

>>> help(pow)
Help on function pow in module __main__:
<BLANKLINE>
pow(base: int, exponent: int) -> Union[int, float]
<BLANKLINE>

------------------------------------------------------------------

>>> class Sandwich:
...     pass


>>> def get_sandwich() -> Sandwich:
...     return Sandwich()

------------------------------------------------------------------

>>> class A:
...     @staticmethod
...     def get_b() -> B:
...         return B()
Traceback (most recent call last):
    ...
NameError: name 'B' is not defined


>>> class B:
...     @staticmethod
...     def get_a() -> A:
...         return A()
Traceback (most recent call last):
...
NameError: name 'A' is not defined


------------------------------------------------------------------

>>> class A:
...     @staticmethod
...     def get_b() -> 'B':
...         return B()


>>> class B:
...     @staticmethod
...     def get_a() -> A:
...         return A()

------------------------------------------------------------------

# Works without an issue

>>> some_variable: 'some_non_existing_type'

# Error as expected

>>> some_variable: some_non_existing_type
Traceback (most recent call last):
...
NameError: name 'some_non_existing_type' is not defined

>>> if typing.TYPE_CHECKING:
...     # Add your import for some_non_existing_type here
...     ...

------------------------------------------------------------------

>>> import typing

>>> Username = typing.NewType('Username', str)

>>> rick = Username('Rick')

>>> type(rick)
<class 'str'>


------------------------------------------------------------------

>>> import typing

>>> T = typing.TypeVar('T', int, str)

>>> def add(a: T, b: T) -> T:
...     return a + b

>>> add(1, 2)
3
>>> add('a', 'b')
'ab'
