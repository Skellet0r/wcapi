from wcapi._wraps import area, system, session


class Screen:
    def __init__(self, _object):
        self._screen = _object

    @property
    @system
    def Application(self):
        """Returns the System Object Read-only."""
        return self._screen.Application

    @property
    def Col(self):
        """Returns the column position of the cursor. First column is 1."""
        return self._screen.Col

    def setCol(self, value):
        """Sets the column position of the cursor. First column is 1."""
        self._screen.Col = value

    @property
    def InHiddenField(self):
        """Returns TRUE if the cursor is within a hidden (password) field,
        otherwise FALSE. This property is valid only for 3270 or 5250 emulation
        types. Read-only."""
        return True if self._screen.InHiddenField else False

    @property
    def Name(self):
        """Returns name of the object as a string Read-only."""
        return self._screen.Name

    @property
    def OIA(self):
        """Returns an OIA object."""
        return self._screen.OIA

    @property
    @session
    def Parent(self):
        """Returns parent for the specified object. (Session). Read-only"""
        return self._screen.Parent

    @property
    def Row(self):
        """Returns the row position of the cursor. First row is 1."""
        return self._screen.Row

    def setRow(self, value):
        """Returns the row position of the cursor. First row is 1."""
        self._screen.Row = value

    @property
    def Updated(self):
        """Returns TRUE if the Screen object has been updated since the last time
        this property was checked. If the object has not been updated
        the property returns FALSE
        NOT WORKING"""
        return self._screen.Updated

    @property
    def Rows(self):
        """Returns the number of rows in the presentation space. Read-only.
        First row is 1."""
        return self._screen.Rows

    @property
    @area
    def Selection(self):
        """Returns an Area object representing the area of the screen currently
        selected by the user. Read-only."""
        return self._screen.Selection

    @area
    def Area(self, StartRow, StartCol, EndRow, EndCol):
        """Returns an Area object with the defined coordinates"""
        return self._screen.Area(StartRow, StartCol, EndRow, EndCol)

    def Copy(self):
        """Copies the select text to the Clipboard but leaves the selected
        text unchanged in the display"""
        self._screen.Copy

    def CopyAppend(self):
        """Copies the selected text from a session to the existing contents
        of the Clipboard but leaves the selected text unchanged in the display"""
        self._screen.CopyAppend

    def Cut(self):
        """Removes selected text from the session and stores it in the Clipboard"""
        self._screen.Cut

    def CutAppend(self):
        """Removes selected text from a session and appends it to the existing
        contents of the Clipboard"""
        self._screen.CutAppend

    def Delete(self):
        """Removes selected text from the session"""
        self._screen.Delete

    def FieldAttribute(self, row, column):
        """Returns the field attribute value for a given row/column position on the
        current screen. Returns 0 if an invalid row or column is provided, or
        if the current screen does not contain field formatting. Valid only for
        3270 or 5250 emulation types"""
        return self._screen.FieldAttribute(row, column)

    def GetString(self, row, column, len):
        """Returns the text from the specified screen location given length"""
        return self._screen.GetString(row, column, len)

    def MoveRelative(self, NumOfRows, NumOfCols):
        """Moves the cursor a specified number of rows and columns
        from its current position"""
        self._screen.MoveRelative(NumOfRows, NumOfCols)

    def MoveTo(self, row, col):
        """Moves the cursor to the specified location"""
        self._screen.MoveTo(row, col)

    def Paste(self):
        """Pastes Clipboard text at the current position or over the current
        selection"""
        self._screen.Paste

    def PasteContinue(self):
        """Pastes Clipboard text at the current position or over the current
        selection"""
        self._screen.PasteContinue

    def PutString(self, text, row, col):
        """Puts text in the specified location on the screen"""
        self._screen.PutString(text, row, col)

    @area
    def Search(self, text, row, col):
        """Returns an Area object with the text specified in the search.
        if search finds the specified text, the coordinate properties
        Left(Starting Column)
        Top (Starting Row)
        Right (Ending Column)
        Bottom (Ending Row)
        of the returned Area object are set to the starting and ending row and
        column positions of the text
        The Value property of the Area object is set to the text located at those
        coordinates, the Value property of the Area changes.
        if search does not find the specified text, the Area object's Value property
        is set to an empty string, its Type property is set to xNone
        and its coordinate properties are set to -1"""
        return self._screen.Search(text, row, col)

    def Select(self, StartRow, StartCol, EndRow, EndCol):
        """Selects the area defined by the coordinates and returns
        an Area object"""
        return self._screen.Select(StartRow, StartCol, EndRow, EndCol)

    @area
    def SelectAll(self):
        """Selects the entire screen and returns an Area object"""
        return self._screen.SelectAll

    def SendKeys(self, String):
        """Sends keystrokes to the host, including function keys."""
        self._screen.SendKeys(String)

    def WaitForCursor(self, Row, Col, EndRow, EndCol):
        """Waits until the cursor is at the specified location. The method will
        wait for the length of time set in System.TimeoutValue (default. 30 sec)"""
        self._screen.WaitForCursor(Row, Col, EndRow, EndCol)

    def WaitForCursorMove(self, NumOfRows, NumOfCols):
        """Waits until the cursor has moved the specified number
        of rows and columns from its current position. the method will
        wait for the length of time set in System.TimeoutValue"""
        self._screen.WaitForCursorMove(NumOfRows, NumOfCols)

    def WaitForKeys(self):
        """Waits until the user presses a key or for the specified 
        time to elapse before the program will continue"""
        self._screen.WaitForKeys()

    def WaitForString(self, text, row, col):
        """Waits until the specified text appears on the screen at
        the row spcified. The match starts at therow and column
        specified and will match along the rest of the column positions
        in that row to the right of the specified starting column.
        The method will wait for the amount of time set in the System.TimeoutValue"""
        self._screen.WaitForString(text, row, col)

    def WaitHostQuiet(self, timeout=None):
        """Waits for the host to not send data for a specified number of
        milliseconds. The Screen object will wait for host compliance
        for the amount of time set in System.TimeoutValue"""
        if timeout:
            self._screen.WaitHostQuiet(timeout)
        else:
            self._screen.WaitHostQuiet()
