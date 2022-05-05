import functools


def coroutine(function):
    @functools.wraps(function)
    def _coroutine(*args, **kwargs):
        active_coroutine = function(*args, **kwargs)
        assert not next(active_coroutine)
        return active_coroutine
    return _coroutine
