class Screen:
    def __init__(self, _object):
        self._screen = _object

    @property
    def Application(self):
        """Returns the System Object Read-only."""
        return self._screen.Application

    @property
    def Col(self):
        """Returns or sets the column position of the cursor. First column is 1."""
        return self._screen.Col

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
    def Parent(self):
        """Returns parent for the specified object. (Session). Read-only"""
        return self._screen.Parent

    @property
    def Row(self):
        """Returns or sets the row position of the cursor. First row is 1."""
        return self._screen.Row

    @property
    def Rows(self):
        """Returns the number of rows in the presentation space. Read-only.
        First row is 1."""
        return self._screen.Rows

    @property
    def Selection(self):
        """Returns an Area object representing the area of the screen currently
        selected by the user. Read-only."""
        return self._screen.Selection

    def Area(self, StartRow, StartCol, EndRow, EndCol):
        pass

    def Copy(self):
        pass

    def CopyAppend(self):
        pass

    def Cut(self):
        pass

    def CutAppend(self):
        pass

    def Delete(self):
        pass

    def FieldAttribute(self, row, column):
        pass

    def GetString(self, row, column, len):
        pass

    def MoveRelative(self, NumOfRows, NumOfCols):
        pass

    def MoveTo(self, row, col):
        pass

    def Paste(self):
        pass

    def PasteContinue(self):
        pass

    def PutString(self, text, row, col):
        pass

    def Search(self, text, row, col):
        pass

    def Select(self, StartRow, StartCol, EndRow, EndCol):
        pass

    def SelectAll(self):
        pass

    def SendKeys(self, String):
        pass

    def WaitForCursor(self, Row, Col, EndRow, EndCol):
        pass

    def WaitForCursorMove(self, NumOfRows, NumOfCols):
        pass

    def WaitForKeys(self):
        pass

    def WaitForString(self, text, row, col):
        pass

    def WaitHostQuiet(self, timeout=None):
        pass
