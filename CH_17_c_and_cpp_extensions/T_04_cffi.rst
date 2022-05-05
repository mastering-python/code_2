>>> import cffi

>>> ffi = cffi.FFI()
>>> ffi.cdef('int printf(const char* format, ...);')
>>> libc = ffi.dlopen(None)
>>> arg = ffi.new('char[]', b'Printing using CFFI\n')
>>> libc.printf(arg)
20

