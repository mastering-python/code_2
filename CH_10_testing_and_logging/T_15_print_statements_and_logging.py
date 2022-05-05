import os
import sys
import logging


def test_print():
    print('Printing to stdout')
    print('Printing to stderr', file=sys.stderr)
    logging.debug('Printing to debug')
    logging.info('Printing to info')
    logging.warning('Printing to warning')
    logging.error('Printing to error')
    # We don't want to display os.environ so hack around it
    fail = 'FAIL' in os.environ
    assert not fail
