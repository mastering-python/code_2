>>> import cffi

>>> ffi = cffi.FFI()

# Create the structures as C structs

>>> ffi.cdef('''
... typedef struct {
...     int x;
...     int y;
... } point;
...
... typedef struct {
...     point a;
...     point b;
... } vertex;
... ''')

# Create a vertex and return the pointer

>>> v = ffi.new('vertex*')

# Set the data

>>> v.a.x, v.a.y, v.b.x, v.b.y = (0, 1, 2, 3)

# Print before change

>>> v.a.x, v.a.y, v.b.x, v.b.y
(0, 1, 2, 3)

>>> v.a, v.b = v.b, v.a

# Print after change

>>> v.a.x, v.a.y, v.b.x, v.b.y
(2, 3, 2, 3)

