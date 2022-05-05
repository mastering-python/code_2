import pdb


def print_value(value):
    print('value:', value)


if __name__ == '__main__':
    pdb.set_trace()
    for i in range(5):
        print_value(i)
