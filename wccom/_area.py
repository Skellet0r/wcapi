from wccom._screen import Screen
from wccom._system import System


class Area:
    def __init__(self, _object):
        self._area = _object

    @property
    def Application(self):
        """Return System object. Read-only."""
        return System(self._area.Application)

    @property
    def Bottom(self):
        """Returns or sets the ending row of the Area object. ReadWrite."""
        return self._area.Bottom

    @property
    def Left(self):
        """Returns or sets the screen column where the area begins. ReadWrite."""
        return self._area.Left

    @property
    def Parent(self):
        """Returns the parent (Screen) object for the Area object. Read-only."""
        return Screen(self._area.Parent)

    @property
    def Right(self):
        """Returns or sets the screen column where the area ends. ReadWrite."""
        return self._area.Right

    @property
    def Top(self):
        """Returns or sets the beginning row of the Area object. ReadWrite."""
        return self._area.Top

    @property
    def Type(self):
        """States how to interpreted the top, left, bottom and right coordinates. ReadWrite.
        WCOI only supports xSTREAM and xNONE options.
        Integer xSTREAM = 2
        Integer xNONE = 0"""
        return self._area.Type

    @property
    def Value(self):
        """Returns or sets the text in the Area. ReadWrite."""
        return self._area.Value

    @property
    def Copy(self):
        """Copies the select text to the Clipboard."""
        return self._area.Copy

    @property
    def Select(self):
        """Selects the Object."""
        return self._area.Select
