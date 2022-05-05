import os
import time
import glob
import pytest
import pathlib
import difflib
from datetime import datetime
from datetime import timedelta


PATH = pathlib.Path(__file__).parent.resolve()


@pytest.mark.parametrize('output_filename', glob.iglob('*/*.out'))
def test_output(xprocess, output_filename):
    output_filename = os.path.abspath(output_filename)

    def prepare(cwd):
        return '', ['python3', name + '.py']

    name, ext = os.path.splitext(output_filename)
    pid, log_file = xprocess.ensure(output_filename, prepare)

    timeout = datetime.now() + timedelta(seconds=5)
    while xprocess.getinfo(output_filename).isrunning():
        time.sleep(0.01)

        if datetime.now() > timeout:
            raise RuntimeError(
                f'Timeout while waiting for {name}')

    with open(output_filename) as output_file:
        expected_output = output_file.read()
        real_output = log_file.read()

        # Strip the base path
        real_output = real_output.replace(str(PATH), '')
        expected_output = expected_output.replace(str(PATH), '')

        print(f'Expected:\n{expected_output}')
        print(f'Real:\n{real_output}')

        differ = difflib.Differ()
        real_lines = real_output.splitlines()
        expected_lines = expected_output.splitlines()
        print('Diff:')
        for line in differ.compare(real_lines, expected_lines):
            print(line)

        # Support wildcards
        print('Comparing:')
        expected_outputs = expected_output.split('...')
        if len(expected_outputs) == 1:
            assert expected_output == real_output
        else:
            for expected_output in expected_outputs:
                print(f'Looking for:\n{expected_output}\nIn\n{real_output}')
                assert expected_output in real_output

