import comtypes.client as cc
from wccom._wraps import session, sessions


class System:
    def __init__(self, _object=None):
        self._system = _object if _object else cc.CreateObject("WebConnect.System")

    @property
    @session
    def ActiveSession(self):
        """Returns the currently active Session object. Read-only"""
        return self._system.ActiveSession

    @property
    def Application(self):
        """Returns the System object. Read-only"""
        return self._system.Application

    @property
    def FullName(self):
        """Returns a string specifying the path and filename. Read-only."""
        return self._system.FullName

    @property
    def Name(self):
        """Returns the name of the object as a string. Read-only."""
        return self._system.Name

    @property
    def Parent(self):
        """Returns the parent of the specified object. Read-only."""
        return self._system.Parent

    @property
    @sessions
    def Sessions(self):
        """Returns the Sessions collection containing the individual Session
        objects that are currently open. Read-only."""
        return self._system.Sessions

    @property
    def TimeoutValue(self):
        """Sets or returns the timeout interval (or default timeout interval) in
        milliseconds used by some Wait operations.
        The initial default timeout value is 30,000 milliseconds (30 seconds). If
        you change TimeoutValue, the new value becomes the default."""
        return self._system.TimeoutValue

    @property
    def Version(self):
        return self._system.Version

    def Quit(self):
        return self._system.Quit()
