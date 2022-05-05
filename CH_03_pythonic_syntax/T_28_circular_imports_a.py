import T_28_circular_imports_b


class FileA:
    pass


class FileC(T_28_circular_imports_b.FileB):
    pass
