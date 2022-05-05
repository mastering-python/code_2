>>> from ctypes import util
>>> import cffi

# Initialize the FFI builder

>>> ffi = cffi.FFI()

# Find the libc library on OS X. Look back at the ctypes examples
for other platforms.

>>> library = util.find_library('libc.dylib')
>>> library
'/usr/lib/libc.dylib'

# Load the library

>>> libc = ffi.dlopen(library)
>>> libc
<cffi.api._make_ffi_library.<locals>.FFILibrary object at ...>

# We do have printf available, but CFFI requires a signature

>>> libc.printf
Traceback (most recent call last):
  ...
AttributeError: printf

# Define the printf signature and call printf

>>> ffi.cdef('int printf(const char* format, ...);')
>>> libc.printf
<cdata 'int(*)(char *, ...)' ...>
