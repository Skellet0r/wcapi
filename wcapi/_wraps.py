from functools import wraps


def session(func):
    @wraps(func)
    def wrap_session(*args, **kwargs):
        from wcapi._session import Session

        return Session(func(*args, **kwargs))

    return wrap_session


def area(func):
    @wraps(func)
    def wrap_area(*args, **kwargs):
        from wcapi._area import Area

        return Area(func(*args, **kwargs))

    return wrap_area


def system(func):
    @wraps(func)
    def wrap_system(*args, **kwargs):
        from wcapi._system import System

        return System(func(*args, **kwargs))

    return wrap_system


def screen(func):
    @wraps(func)
    def wrap_screen(*args, **kwargs):
        from wcapi._screen import Screen

        return Screen(func(*args, **kwargs))

    return wrap_screen


def sessions(func):
    @wraps(func)
    def wrap_sessions(*args, **kwargs):
        from wcapi._sessions import Sessions

        return Sessions(func(*args, **kwargs))

    return wrap_sessions
