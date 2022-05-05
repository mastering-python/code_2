>>> import numpy

>>> from scipy import sparse

>>> x = numpy.identity(10000)
>>> y = sparse.identity(10000)

>>> x.data.nbytes
800000000

# Summing the memory usage of scipy.sparse objects require summing
of all internal arrays. We can test for these arrays using the
nbytes attribute.

>>> arrays = [a for a in vars(y).values() if hasattr(a, 'nbytes')]

# sum the bytes from all arrays

>>> sum(a.nbytes for a in arrays)
80004
