#cython: language_level=3


def sum_of_squares(int n):
    cdef int i, total = 0

    for i in range(n):
        if i * i < n:
            total += i * i
        else:
            break

    return total

