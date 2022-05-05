>>> import cffi

>>> ffi = cffi.FFI()

# Create arrays of size 10:

>>> x = ffi.new('int[10]')
>>> y = ffi.new('int[]', 10)

>>> x
<cdata 'int[10]' owning 40 bytes>
>>> y
<cdata 'int[]' owning 40 bytes>

>>> x[0:10] = range(10)
>>> list(x)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> y[:] = range(10)
Traceback (most recent call last):
    ...
IndexError: slice start must be specified

>>> x[0:100] = range(100)
Traceback (most recent call last):
    ...
IndexError: index too large (expected 100 <= 10)

