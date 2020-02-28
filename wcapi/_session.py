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
    def Connected(self) -> bool:
        """Returns the connection status of the session—TRUE if
        connected, FALSE if disconnected. The property also connects
        or disconnects from the session. ReadWrite."""
        return True if self._session.Connected else False

    def setConnected(self, value: int):
        """Sets the connection status of the session—TRUE if
        connected, FALSE if disconnected. The property also connects
        or disconnects from the session"""
        self._session.Connected = value

    @property
    def FileTransferHostOS(self) -> int:
        """Returns the host operating system used by file
        transfers. ReadWrite.
        This property should be set prior to executing a file transfer.
        Valid values are as follows:
        0 - CMS
        1 - TSO
        2 - CICS"""
        return self._session.FileTransferHostOS

    def setFileTransferHostOS(self, value):
        """Sets the host operating system used by file
        transfers. ReadWrite.
        This property should be set prior to executing a file transfer.
        Valid values are as follows:
        0 - CMS
        1 - TSO
        2 - CICS"""
        self._session.FileTransferHostOS = value

    @property
    def FullName(self) -> str:
        """Returns a string specifying full name of session"""
        return self._session.FullName

    @property
    def Height(self) -> int:
        """Returns the height of the session window in pixels."""
        return self._session.Height

    def setHeight(self, value: int):
        """Sets the height of the session window in pixels."""
        self._session.Height = value

    @property
    def KeyboardLocked(self) -> bool:
        """Returns the keyboard input state for the session
        TRUE to block keyboard input; FALSE to accept keyboard input."""
        return bool(self._session.KeyboardLocked)

    def setKeyboardLocked(self, value: int):
        """Sets the keyboard input state for the session
        TRUE to block keyboard input; FALSE to accept keyboard input."""
        self._session.KeyboardLocked = value

    @property
    def KeyMap(self) -> str:
        """Returns the keyboard input state for the session
        TRUE to block keyboard input; FALSE to accept keyboard input"""
        return self._session.KeyMap

    def setKeyMap(self, value: str):
        """Sets the keyboard input state for the session
        TRUE to block keyboard input; FALSE to accept keyboard input"""
        self._session.KeyMap = value

    @property
    def Language(self) -> str:
        """Returns the language for the session"""
        return self._session.Language

    def setLanguage(self, value: str):
        """Sets the language for the session"""
        self._session.Language = value

    @property
    def Left(self) -> int:
        """Returns the Left property returns the horizontal position of the session"""
        return self._session.Left

    def setLeft(self, value: int):
        """Sets the Left property returns the horizontal position of the session"""
        self._session.Left = value

    @property
    def Quiet(self) -> bool:
        """Returns the quiet status of the status.
        TRUE if quiet, FALSE if not quiet"""
        return bool(self._session.Quiet)

    def setQuiet(self, value):
        self._session.Quiet = value

    @property
    def Name(self) -> str:
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
    def Type(self) -> int:
        """Returns a value indicating the session type -- 3270, 5250. Read
        Only."""
        return self._session.Type

    @property
    def Top(self) -> int:
        """The Top property returns the vertical position of the session, in pixels"""
        return self._session.Top

    def setTop(self, value: int):
        """Sets the Top property, vertical position of the session"""
        self._session.Top = value

    @property
    def Visible(self) -> int:
        """Returns the visibility of the object
        TRUE if visible, FALSE if not"""
        return self._session.Visible

    def setVisible(self, value: int):
        """Sets the visiblity of the object"""
        self._session.Visible = value

    @property
    def Width(self) -> int:
        """Returns the width of the session window in pixels"""
        return self._session.Width

    def setWidth(self, value: int):
        """Sets the width of the session window in pixels"""
        self._session.Width = value

    def setWindowState(self, value: str):
        """Sets the state of the session window
        normal, maximized, minimized."""
        self._session.WindowState = value

    def Activate(self):
        """Makes the specified session the active window"""
        self._session.Activate()

    def Close(self):
        """Closes the session."""
        self._session.Close()

    def ReceiveFile(self, PCFile, HostFile, bQuiet):
        """Receives a file from the host. IND$FILE is only supported."""
        self._session.ReceiveFile(PCFile, HostFile, bQuiet)

    def SendFile(self, PCFile, HostFile, bQuiet):
        """Sends a file to the host. Only IND$FILE is supported."""
        self._session.SendFile(PCFile, HostFile, bQuiet)

    def WaitForTimer(self, milliseconds):
        """Waits for the specified number of milliseconds to elapse."""
        self._session.WaitForTimer(milliseconds)
