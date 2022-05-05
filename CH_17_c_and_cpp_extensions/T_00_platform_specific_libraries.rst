# Windows

>>> import ctypes

>>> ctypes.cdll
<ctypes.LibraryLoader object at 0x...>
>>> libc = ctypes.cdll.msvcrt
>>> libc
<CDLL 'msvcrt', handle ... at ...>
>>> libc.printf
<_FuncPtr object at 0x...>

------------------------------------------------------------------------------

# Linux

>>> import ctypes

>>> ctypes.cdll
<ctypes.LibraryLoader object at 0x...>
>>> libc = ctypes.cdll.LoadLibrary('libc.so.6')
>>> libc
<CDLL 'libc.so.6', handle ... at ...>
>>> libc.printf
<_FuncPtr object at 0x...>

------------------------------------------------------------------------------

# OS X

>>> import ctypes

>>> libc = ctypes.cdll.LoadLibrary('libc.dylib')
>>> libc
<CDLL 'libc.dylib', handle ... at 0x...>
>>> libc.printf
<_FuncPtr object at 0x...>

------------------------------------------------------------------------------

# OS X

>>> from ctypes import util
>>> from ctypes import cdll

>>> library = util.find_library('libc')
>>> library
'/usr/lib/libc.dylib'

# Load the library

>>> libc = cdll.LoadLibrary(library)
>>> libc
<CDLL '/usr/lib/libc.dylib', handle ... at 0x...>

------------------------------------------------------------------------------

>>> c_string = ctypes.create_string_buffer(b'some bytes')
>>> ctypes.sizeof(c_string)
11
>>> c_string.raw
b'some bytes\x00'
>>> c_string.value
b'some bytes'
>>> libc.printf(c_string)
10
some bytes>>>

------------------------------------------------------------------------------

| >>> libc.printf(123)
| segmentation fault (core dumped)  python3

------------------------------------------------------------------------------

>>> format_string = b'Number: %d\n'
>>> libc.printf(format_string, 123)
Number: 123
12
>>> x = ctypes.c_int(123)
>>> libc.printf(format_string, x)
Number: 123
12

------------------------------------------------------------------------------

>>> format_string = b'Number: %.3f\n'
>>> libc.printf(format_string, 123.45)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ctypes.ArgumentError: argument 2: <class 'TypeError'>: Don't know how to convert parameter 2
>>> x = ctypes.c_double(123.45)
>>> libc.printf(format_string, x)
Number: 123.450
16

------------------------------------------------------------------------------

>>> x = ctypes.c_double(123.45)
>>> x.value
123.45
>>> x.value = 456
>>> x
c_double(456.0)
