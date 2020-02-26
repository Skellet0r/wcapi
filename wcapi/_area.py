from wcapi._wraps import screen, system


class Area:
    def __init__(self, _object):
        self._area = _object

    @property
    @system
    def Application(self):
        """Return System object. Read-only."""
        return self._area.Application

    @property
    def Bottom(self):
        """Returns the ending row of the Area object. ReadWrite."""
        return self._area.Bottom

    def setBottom(self, value):
        """Sets the ending row of the Area object. ReadWrite."""
        self._area.Bottom = value

    @property
    def Left(self):
        """Returns the screen column where the area begins. ReadWrite."""
        return self._area.Left

    def setLeft(self, value):
        """Sets the screen column where the area begins"""
        self._area.Left = value

    @property
    @screen
    def Parent(self):
        """Returns the parent (Screen) object for the Area object. Read-only."""
        return self._area.Parent

    @property
    def Right(self):
        """Returns the screen column where the area ends. ReadWrite."""
        return self._area.Right

    def setRight(self, value):
        """Returns the screen column where the area ends. ReadWrite."""
        self._area.Right = value

    @property
    def Top(self):
        """Returns the beginning row of the Area object. ReadWrite."""
        return self._area.Top

    def setTop(self, value):
        """Returns the beginning row of the Area object. ReadWrite."""
        self._area.Top = value

    @property
    def Type(self):
        """States how to interpreted the top, left, bottom and right coordinates. ReadWrite.
        WCOI only supports xSTREAM and xNONE options.
        Integer xSTREAM = 2
        Integer xNONE = 0"""
        return self._area.Type

    def setType(self, value):
        """States how to interpreted the top, left, bottom and right coordinates. ReadWrite.
        WCOI only supports xSTREAM and xNONE options.
        Integer xSTREAM = 2
        Integer xNONE = 0"""
        self._area.Type = value

    @property
    def Value(self):
        """Returns the text in the Area. ReadWrite."""
        return self._area.Value

    def setValue(self, value):
        """Returns the text in the Area. ReadWrite."""
        self._area.Value = value

    @property
    def Copy(self):
        """Copies the select text to the Clipboard."""
        return self._area.Copy

    @property
    def Select(self):
        """Selects the Object."""
        return self._area.Select
