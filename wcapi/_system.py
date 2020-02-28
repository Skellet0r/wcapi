import comtypes.client as cc
from wcapi._wraps import session, sessions


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
    def FullName(self) -> str:
        """Returns a string specifying the path and filename. Read-only."""
        return self._system.FullName

    @property
    def Name(self) -> str:
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
    def TimeoutValue(self) -> int:
        """Returns the timeout interval (or default timeout interval) in
        milliseconds used by some Wait operations."""
        return self._system.TimeoutValue

    def setTimeoutValue(self, value: int):
        """Sets the timeout interval (or default timeout interval) in
        milliseconds used by some Wait operations."""
        self._system.TimeoutValue = value

    @property
    def Version(self) -> str:
        return self._system.Version

    def Quit(self):
        """Closes all sessions."""
        self._system.Quit()
