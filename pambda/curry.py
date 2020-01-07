""" Function Currying """
from typing import Callable


def curry(fn: Callable, arity: int) -> Callable:
    def curried(*args):
        if len(args) < arity:
            return curry(lambda *largs: fn(*args, *largs), arity - len(args))

        return fn(*args)

    return curried


# def yeah(x, y, z, xx, yy, zz):
#     return x + y + z + xx + yy + zz
#
# cool = curry(yeah, 6)

# cool(1)
# cool(1)(2)
# cool(1)(2)(3)
# cool(1)(2)(3)(4)(5)(6)
# cool(1, 2, 3, 4, 5)(6)
