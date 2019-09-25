from functools import wraps


def session(func):
    @wraps(func)
    def wrap_session(*args, **kwargs):
        from wccom._session import Session

        return Session(func(*args, **kwargs))

    return wrap_session


def area(func):
    @wraps(func)
    def wrap_area(*args, **kwargs):
        from wccom._area import Area

        return Area(func(*args, **kwargs))

    return wrap_area


def system(func):
    @wraps(func)
    def wrap_system(*args, **kwargs):
        from wccom._system import System

        return System(func(*args, **kwargs))

    return wrap_system


def screen(func):
    @wraps(func)
    def wrap_screen(*args, **kwargs):
        from wccom._screen import Screen

        return Screen(func(*args, **kwargs))

    return wrap_screen
