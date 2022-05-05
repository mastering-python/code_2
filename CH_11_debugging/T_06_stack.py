import traceback


class ShowMyStack:

    def run(self, limit=None):
        print('Before stack print')
        traceback.print_stack(limit=limit)
        print('After stack print')


class InheritShowMyStack(ShowMyStack):
    pass


if __name__ == '__main__':
    show_stack = InheritShowMyStack()

    print('Stack without limit')
    show_stack.run()
    print()

    print('Stack with limit 1')
    show_stack.run(1)
