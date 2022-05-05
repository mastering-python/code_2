import builtins
import inspect
import pprint
import re


def pp(*args, **kwargs):
    '''PrettyPrint function that prints the variable name when
    available and pprints the data

    >>> x = 10
    >>> pp(x)
    # x: 10
    '''
    # Fetch the current frame from the stack
    frame = inspect.currentframe().f_back
    # Prepare the frame info
    frame_info = inspect.getframeinfo(frame)

    # Walk through the lines of the function
    for line in frame_info[3]:
        # Search for the pp() function call with a fancy regexp
        m = re.search(r'\bpp\s*\(\s*([^)]*)\s*\)', line)
        if m:
            print('# %s:' % m.group(1), end=' ')
            break

    pprint.pprint(*args, **kwargs)


builtins.pf = pprint.pformat
builtins.pp = pp
