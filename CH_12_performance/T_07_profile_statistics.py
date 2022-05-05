import sys
import pathlib
import pstats
import cProfile

import pyperformance

# pyperformance doesn't expose the benchmarks anymore so we need
# to manually add the path
pyperformance_path = pathlib.Path(pyperformance.__file__).parent
sys.path.append(str(pyperformance_path / 'data-files'))

# Now we can import the benchmark
from benchmarks.bm_float import run_benchmark as bm_float  # noqa


def benchmark():
    for i in range(10):
        bm_float.benchmark(bm_float.POINTS)


if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.runcall(benchmark)
    profiler.dump_stats('bm_float.profile')

    stats = pstats.Stats('bm_float.profile')
    stats.strip_dirs()
    stats.sort_stats('calls', 'cumtime')
    stats.print_stats(10)
