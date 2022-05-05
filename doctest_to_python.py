import argparse
import doctest
import functools
import pathlib
import sys

import python_utils

print_err = functools.partial(print, file=sys.stderr)

USAGE = f'''
Defaults to reading from stdin and writing to stdout when no
files are given. When `somefile.rst` file is given,
the doctest is extracted from that file and written to
`somefile.py`.

Usage:
# cat somefile.rst | python3 {sys.argv[0]}

Or:
# python3  {sys.argv[0]} somefile.rst
'''


@python_utils.listify(lambda x: ''.join(x))
def doctest_to_python(test: str) -> str:
    r'''
    Convert a doctest to regular Python

    >>> doctest_to_python('>>> 1 + 1')
    '1 + 1\n'

    >>> doctest_to_python('>>> "Hi there"')
    '"Hi there"\n'
    '''

    # Use the doctest module to parse the doctest
    parser = doctest.DocTestParser()

    # Pieces are either literal strings or doctest examples
    for piece in parser.parse(test):
        if isinstance(piece, str):
            # Strip some overly verbose output
            stripped_piece = piece.strip()
            if '\n' in stripped_piece:
                if piece[0] == '\n':
                    yield '\n'

                # Multiline comments are encapsulated in triple
                # quoted strings
                yield f"""'''\n{stripped_piece}\n'''\n"""
            elif stripped_piece:
                # Single line comments get a # prefix
                yield f'\n# {stripped_piece.lstrip("# ")}\n'
            else:
                # Empty strings become a newline
                yield piece

        elif isinstance(piece, doctest.Example):
            if piece.want.strip():
                # If the example has a result, it's a doctest
                yield f'# {piece.want}'

            # The example source
            yield piece.source

        else:
            raise TypeError(f'Unknown type: {type(piece)}')


def main():
    parser = argparse.ArgumentParser(
        description='Convert a doctest to regular Python',
        usage=USAGE,
    )
    parser.add_argument(
        'paths',
        help='Path to the doctest file',
        nargs='*',
        default=['-'],
        type=pathlib.Path,
    )
    parser.add_argument('-o', '--overwrite', action='store_true',
                        help='Overwrite existing files')

    args = parser.parse_args()

    for input_path in args.paths:
        if input_path == '-':
            print_err('Reading from stdin...')
            print(''.join(doctest_to_python(sys.stdin.read())))

        elif isinstance(input_path, pathlib.Path):
            output_path = input_path.with_suffix('.py')
            if output_path.exists() and not args.overwrite:
                print_err(f'Skipping existing file {output_path}')
                continue

            elif not input_path.exists():
                print_err(f'Skipping missing file {input_path}')
                continue

            print_err(f'Writing to {output_path}...')
            with input_path.open('r') as input_fh:
                with output_path.open('w') as output_fh:
                    output = doctest_to_python(input_fh.read())
                    output_fh.write(output)

        else:
            raise TypeError(f'Unknown type: {type(input_path)}')


if __name__ == '__main__':
    main()
