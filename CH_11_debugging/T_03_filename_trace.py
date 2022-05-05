import sys
import trace as trace_module
import contextlib


@contextlib.contextmanager
def trace(filename):
    tracer = trace_module.Trace()

    def custom_trace(frame, event, arg):
        # Only trace for the given filename
        if filename != frame.f_code.co_filename:
            return custom_trace

        # Let globaltrace handle the rest
        return tracer.globaltrace(frame, event, arg)

    sys.settrace(custom_trace)
    yield tracer
    sys.settrace(None)

    result = tracer.results()
    result.write_results(show_missing=False, summary=True)


def some_test_function(a, b):
    c = a + b
    return c


# Pass our current filename as `__file__`
with trace(filename=__file__):
    print(some_test_function('a', 'b'))
