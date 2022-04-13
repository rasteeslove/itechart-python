"""
This module provides some additional functionality for the implementation
of the management app (the point is mainly easier operation of the API).
"""


from typing import Callable


def apply_decorator_on_condition(dec: Callable, condition: bool) -> Callable:
    def wrapper(func: Callable) -> Callable:
        if condition:
            func = dec(func)
        return func

    return wrapper
