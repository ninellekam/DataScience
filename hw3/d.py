import functools


def counter(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if wrapped.depth == 0:
            wrapped.rdepth = 0
            wrapped.ncalls = 0
        wrapped.depth += 1
        wrapped.ncalls += 1
        wrapped.rdepth = max(wrapped.rdepth, wrapped.depth)
        res = f(*args, **kwargs)
        wrapped.depth -= 1
        return res

    wrapped.depth = 0
    wrapped.rdepth = 0
    wrapped.ncalls = 0
    return wrapped
