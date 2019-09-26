from wccom._wraps import system


class Sessions:
    def __init__(self, _object):
        self._sessions = _object

    @property
    @system
    def Application(self):
        """Returns the System Object"""
        self._sessions.Application

    @property
    def Count(self):
        """Returns the number of items in the collection of objects.
        Read-only. The number of open sessions."""
        self._sessions.Count

    @property
    @system
    def Parent(self):
        """Returns the parent of the specified object. Read-only.
        The parent for Sessions object is System object."""
        self._sessions.Parent

    @property
    def WCCertificate(self):
        """Sets the value of certificate fingerprint required by the
        WebConnect server to create a SSL connection between the COM object
        and WebConnect Server. To obtain the correct certificate fingerprint
        go to 'security' subdirectory within the home directory of 
        WebConnect server. Run showcert program to get the cert.
        Make sure to remove all blanks before assigning it to WCCertificate.
        HTMLByPass property of Sessions has to be set for an SSL enabled Session AutoStart"""
        self._sessions.WCCertificate

    @property
    def WCCipherSuite(self):
        """Assigned a predefined value of Cipher suites supported by WebConnect server
        for SSL connection. All support cipher suites are defined in SSLCipherSuites module part
        of the COM object and are listed below under Syntax. HTMLByPass property of Sessions
        has to be set for an SSL enabled Session AutoStart.
        The cipher selected by this property must match the cipher configured in the target WebConnect session."""
        self._sessions.WCCipherSuite

    @property
    def WCHTMLByPass(self):
        """Sets the WebConnect session connenction mode. If HTMLByPass is se
        then a direct connection to WebConnect Server is performed and jhllapi.html is by passed"""
        self._sessions.WCHTMLByPass

    @property
    def WCServerName(self):
        """Sets the server (host) name of machine where the WebConnect Server is running.
        This server is used to establish a session."""
        self._sessions.WCServerName

    @property
    def WCSessionType(self):
        """Sets the WebConnect applet session type. Support session types are 3270 and 5250"""
        self._sessions.WCSessionType

    @property
    def WCServerPort(self):
        """Sets the WebConnect Server HTML port. Takes a string"""
        self._sessions.WCServerPort

    @property
    def WCServerUserid(self):
        """Sets the WebConnect Server Userid. If provided,
        Userid and Password will be used to do Userid/Password
        authentication with WebConnect Server before requested session is started."""
        self._sessions.WCServerUserid

    @property
    def WCServerPasswd(self):
        """Sets the WebConnect Server Password. If provided, Userid and Password
        will be used to do Userid/Password authentication with WebConnect Server
        before requested session is started."""
        self._sessions.WCServerPasswd

    @property
    def WCProxy(self):
        """Set the value of Proxy hostname required by the WebConnect
        server if a proxy is desired to connect to the server.
        HTMLByPass property of Sessions has to be set for an SSL enabled Session
        AutoStart."""
        self._sessions.WCProxy
