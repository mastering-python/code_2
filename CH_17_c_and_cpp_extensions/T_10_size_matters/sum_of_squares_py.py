def sum_of_squares(n):
    total = 0

    for i in range(n):
        if i * i < n:
            total += i * i
        else:
            break

    return total

