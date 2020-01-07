""" Function Composition and Function Composition Utilities """
from functools import reduce, partial
from types import FunctionType
from typing import Any, Callable


def all_fn(*args) -> bool:
    """ Determines if every argument is a function """
    for arg in args:
        if not isinstance(arg, (FunctionType, partial)):
            return False

    return True


def identity(x: Any) -> Any:
    return x


def tap_(fn: Callable, x: Any) -> Any:
    fn(x)
    return x


def curry(fn: Callable, arity: int) -> Callable:
    def curried(*args):
        if len(args) < arity:
            return curry(lambda *largs: fn(*args, *largs), arity - len(args))

        return fn(*args)

    return curried


cmap = curry(map, 2)
cfilter = curry(filter, 2)
tap = curry(tap_, 2)


def compose(*args) -> Callable:
    if not all_fn(*args):
        raise TypeError("All parameters passed to `compose` must be a function")

    def combine(f: Callable, g: Callable) -> Callable:
        def result(x: Any) -> Any:
            return f(g(x))

        return result

    return reduce(combine, args, identity)


def pipe(*args) -> Callable:
    reversed_args = args[::-1]
    return compose(*reversed_args)


# cool_composition = compose(
#     lambda x: list(x),
#     cfilter(lambda x: x >= 4),
#     cmap(lambda x: x + 1),
#     cmap(lambda x: int(x))
# )
#
# cool_pipe = pipe(
#     cmap(lambda x: int(x)),
#     tap(print),
#     cmap(lambda x: x + 1),
#     cfilter(lambda x: x >= 4),
#     lambda x: list(x),
# )
#
# awesome = cool_pipe(["1", "2", "3", "4"])
#
# print(awesome)

