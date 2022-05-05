try:
    import memory_profiler
except ImportError:
    print('Please install the memory profiler to run this example')
    print('pip install -U memory-profiler')
else:
    @memory_profiler.profile
    def main():
        n = 100000
        a = [i for i in range(n)]
        b = [i for i in range(n)]
        c = list(range(n))
        d = list(range(n))
        e = dict.fromkeys(a, b)
        f = dict.fromkeys(c, d)
        assert e
        assert f

    if __name__ == '__main__':
        main()

