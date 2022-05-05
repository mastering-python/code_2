>>> import numpy as np
>>> import stumpy

>>> temperatures = np.array([22., 21., 22., 21., 22., 23.])

>>> window_size = 3

# Calculate a Euclidean distance matrix between the windows

>>> stump = stumpy.stump(temperatures, window_size)

# Show the distance matrix. The row number is the index in the
input array. The first column is the distance, the next columns
are the indices of the nearest match, the left match and the
right match.

>>> stump
array([[0.0, 2, -1, 2],
      [2.449489742783178, 3, -1, 3],
      [0.0, 0, 0, -1],
      [2.449489742783178, 1, 1, -1]], dtype=object)

# As we can see in the matrix above, the first window has a
distance of 0 to the window at index 2 meaning that they are
identical. We can easily verify that by showing both windows:

# The first window:

>>> temperatures[0:window_size]
array([22., 21., 22.])

# The window at index 2:

>>> temperatures[2:2 + window_size]
array([22., 21., 22.])
