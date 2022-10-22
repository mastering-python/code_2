import pathlib
import sys
import warnings

CH_02 = pathlib.Path('CH_02_interactive_python')
CH_03 = pathlib.Path('CH_03_pythonic_syntax')
CH_04 = pathlib.Path('CH_04_design_patterns')
CH_10 = pathlib.Path('CH_10_testing_and_logging')
CH_11 = pathlib.Path('CH_11_debugging')
CH_12 = pathlib.Path('CH_12_performance')
CH_13 = pathlib.Path('CH_13_async_io')
CH_14 = pathlib.Path('CH_14_multithreading_and_multiprocessing')
CH_15 = pathlib.Path('CH_15_scientific_python')
CH_17 = pathlib.Path('CH_17_c_and_cpp_extensions')
CH_18 = pathlib.Path('CH_18_packaging')

collect_ignore_paths = [
    CH_03 / 'T_18_flake8.py',
    CH_03 / 'T_28_circular_imports_a.py',
    CH_03 / 'T_28_circular_imports_b.py',
    CH_10 / 'T_02_testing_with_documentation' / 'conf.py',
    CH_10 / 'T_11_representing_assertions.py',
    CH_10 / 'T_12_assert_representation.py',
    CH_10 / 'T_18_bad_code.py',
    CH_10 / 'T_22_tox' / 'test.py',
    CH_11 / 'T_07_faulthandler.py',
    CH_11 / 'T_08_faulthandler_try_catch.py',
    CH_11 / 'T_09_faulthandler_enabled.py',
    CH_11 / 'T_13_pdb_catching_exceptions.py',
    # CH_12 / 'T_07_profile_statistics.py',
    CH_12 / 'T_08_line_profiler.py',
    CH_13 / 'T_00_async_await.py',
    CH_13 / 'T_13_forgot_await.py',
    CH_14 / 'T_14_deadlocks.py',
    CH_14 / 'T_17_remote_multiprocessing' / 'client.py',
    CH_14 / 'T_17_remote_multiprocessing' / 'server.py',
    CH_14 / 'T_17_remote_multiprocessing' / 'submitter.py',
    CH_17 / 'T_00_platform_specific_libraries.rst',
    CH_17 / 'T_04_cffi.rst',
    CH_17 / 'T_05_cffi_open_library.rst',
    CH_18 / 'T_02_basic_setup_py' / 'entry_points.rst',
]

for filename in collect_ignore_paths:
    assert filename.exists(), f'{filename!r} is missing'

if sys.version_info < (3, 10):
    collect_ignore_paths.append(CH_03 / 'T_19_match_statement.rst')
else:
    warnings.warn(f'Skipping Python 3.10+ tests on {sys.version}')

try:
    import numpy

    assert numpy
except ImportError:
    warnings.warn(
        'Skipping Scientific Python, requirements not installed')
    for filename in CH_15.glob('*.rst'):
        collect_ignore_paths.append(filename)

collect_ignore = [str(p) for p in collect_ignore_paths]
