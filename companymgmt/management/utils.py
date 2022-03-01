"""
This module provides some additional functionality for the implementation
of the management app (the point is mainly easier operation of the API).
"""


def apply_decorator_on_condition(dec, condition):
    def wrapper(func):
        if condition:
            func = dec(func)
        return func
        
    return wrapper
