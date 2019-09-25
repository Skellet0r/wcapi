import comtypes.client as cc


class System:
    def __init__(self, _object=None):
        self._system = _object if _object else cc.CreateObject("WebConnect.System")

    @property
    def ActiveSession(self):
        pass

    @property
    def Application(self):
        pass

    @property
    def FullName(self):
        pass

    @property
    def Name(self):
        pass

    @property
    def Parent(self):
        pass

    @property
    def Sessions(self):
        pass

    @property
    def TimeoutValue(self):
        pass

    @property
    def Version(self):
        pass

    def Quit(self):
        pass
