""" General Utilities """
from types import FunctionType


def all_fn(*args) -> bool:
    """ Determines if every argument is a function """
    for arg in args:
        if not isinstance(arg, FunctionType):
            return False

    return True
