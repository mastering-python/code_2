>>> import cffi

>>> ffi = cffi.FFI()

# In API mode we can in-line the actual C code

>>> ffi.set_source('_sum', '''
... int sum(int* input, int n){
...     int result = 0;
...     while(n--)result += input[n];
...     return result;
... }
... ''')

>>> ffi.cdef('int sum(int*, int);')

>>> library = ffi.compile()

# Now we can import the library

>>> import _sum

# Or use `ffi.dlopen()` with the results from the compile step

>>> _sum_lib = ffi.dlopen(library)

# Create an array with 5 items

>>> N = 5
>>> array = ffi.new('int[]', N)
>>> array[0:N] = range(N)

# Call our C function from either the import or the dlopen

>>> _sum.lib.sum(array, N)
10

>>> _sum_lib.sum(array, N)
10
