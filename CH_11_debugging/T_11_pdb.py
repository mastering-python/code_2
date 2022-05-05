import pdb


def go_to_debugger():
    some_variable = 123
    print('Starting pdb trace')
    pdb.set_trace()
    print(f'Finished pdb, some_variable: {some_variable}')


if __name__ == '__main__':
    go_to_debugger()
