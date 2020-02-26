from wcapi._wraps import system, screen, sessions


class Session:
    def __init__(self, _object):
        self._session = _object

    @property
    @system
    def Application(self):
        """Returns the System Object Read-only"""
        return self._session.Application

    @property
    def Connected(self):
        """Returns the connection status of the session—TRUE if
        connected, FALSE if disconnected. The property also connects
        or disconnects from the session. ReadWrite."""
        return True if self._session.Connected else False

    @property
    def FileTransferHostOS(self):
        """Returns or sets the host operating system used by file
        transfers. ReadWrite.
        This property should be set prior to executing a file transfer.
        Valid values are as follows:
        0 - CMS
        1 - TSO
        2 - CICS"""
        return self._session.FileTransferHostOS

    @property
    def FullName(self):
        """Returns a string specifying full name of session"""
        return self._session.FullName

    @property
    def Name(self):
        """Returns a string specifying name of session"""
        return self._session.Name

    @property
    @sessions
    def Parent(self):
        """Returns the parent of the specified object. (Sessions).
        Read-only"""
        return self._session.Parent

    @property
    @screen
    def Screen(self):
        """Returns the Screen object associated with the
        session.Read-only"""
        return self._session.Screen

    @property
    def Type(self):
        """Returns a value indicating the session type -- 3270, 5250. Read
        Only."""
        return self._session.Type

    def Close(self):
        """Closes the session."""
        self._session.Close

    def ReceiveFile(self, PCFile, HostFile, bQuiet):
        """Receives a file from the host. IND$FILE is only supported."""
        self._session.ReceiveFile(PCFile, HostFile, bQuiet)

    def SendFile(self, PCFile, HostFile, bQuiet):
        """Sends a file to the host. Only IND$FILE is supported."""
        self._session.SendFile(PCFile, HostFile, bQuiet)

    def WaitForTimer(self, milliseconds):
        """Waits for the specified number of milliseconds to elapse."""
        self._session.WaitForTimer(milliseconds)
