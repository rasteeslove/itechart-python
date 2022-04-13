from typing import Callable, Union
from django.http import HttpResponseForbidden
from rest_framework.request import Request
from rest_framework.response import Response


def allow_admins_only(func: Callable) -> Callable:
    """
    This is a decorator for views for allowing only admins
    to access some data.
    """
    def wrapper(request: Request) -> Union[Response, HttpResponseForbidden]:
        if hasattr(request.user, 'is_staff') and request.user.is_staff:
            return func(request)
        else:
            return HttpResponseForbidden()

    return wrapper
