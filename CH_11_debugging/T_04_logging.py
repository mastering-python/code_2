import pprint
import inspect
import logging
import functools


def debug(function):
    @functools.wraps(function)
    def _debug(*args, **kwargs):
        # Make sure `result` is always defined
        result = None
        try:
            result = function(*args, **kwargs)
            return result
        finally:
            # Extract the signature from the function
            signature = inspect.signature(function)
            # Fill the arguments
            arguments = signature.bind(*args, **kwargs)
            # NOTE: This only works for Python 3.5 and up!
            arguments.apply_defaults()

            logging.debug('%s(%s): %s' % (
                function.__qualname__,
                ', '.join('%s=%r' % (k, v) for k, v in
                          arguments.arguments.items()),
                pprint.pformat(result),
            ))

    return _debug


@debug
def add(a, b=123):
    return a + b


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    add(1)
    add(1, 456)
    add(b=1, a=456)
