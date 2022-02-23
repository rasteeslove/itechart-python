from django.http import HttpResponseForbidden


def allow_admins_only(function):
    """
    This is a decorator for views for allowing only admins
    to access some data.
    """
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_staff:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return wrapper
