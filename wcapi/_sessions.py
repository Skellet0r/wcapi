from wcapi._wraps import system, session


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

    def setWCCertificate(self, value):
        """Sets the value of certificate fingerprint required by the
        WebConnect server to create a SSL connection between the COM object
        and WebConnect Server. To obtain the correct certificate fingerprint
        go to 'security' subdirectory within the home directory of
        WebConnect server. Run showcert program to get the cert.
        Make sure to remove all blanks before assigning it to WCCertificate.
        HTMLByPass property of Sessions has to be set for an SSL enabled Session AutoStart"""
        self._sessions.WCCertificate = value

    def setWCCipherSuite(self, value):
        """Assigned a predefined value of Cipher suites supported by WebConnect server
        for SSL connection. All support cipher suites are defined in SSLCipherSuites module part
        of the COM object and are listed below under Syntax. HTMLByPass property of Sessions
        has to be set for an SSL enabled Session AutoStart.
        The cipher selected by this property must match the cipher configured in the target WebConnect session."""
        self._sessions.WCCipherSuite = value

    def setWCHTMLByPass(self, value):
        """Sets the WebConnect session connenction mode. If HTMLByPass is set
        then a direct connection to WebConnect Server is performed and jhllapi.html is by passed"""
        self._sessions.WCHTMLByPass = value

    def setWCServerName(self, value):
        """Sets the server (host) name of machine where the WebConnect Server is running.
        This server is used to establish a session."""
        self._sessions.WCServerName = value

    def setWCSessionType(self, value):
        """Sets the WebConnect applet session type. Support session types are 3270 and 5250"""
        self._sessions.WCSessionType = value

    def setWCServerPort(self, value):
        """Sets the WebConnect Server HTML port. Takes a string"""
        self._sessions.WCServerPort = value

    def setWCServerUserid(self, value):
        """Sets the WebConnect Server Userid. If provided,
        Userid and Password will be used to do Userid/Password
        authentication with WebConnect Server before requested session is started."""
        self._sessions.WCServerUserid = value

    def setWCServerPasswd(self, value):
        """Sets the WebConnect Server Password. If provided, Userid and Password
        will be used to do Userid/Password authentication with WebConnect Server
        before requested session is started."""
        self._sessions.WCServerPasswd = value

    def setWCProxy(self, value):
        """Set the value of Proxy hostname required by the WebConnect
        server if a proxy is desired to connect to the server.
        HTMLByPass property of Sessions has to be set for an SSL enabled Session
        AutoStart."""
        self._sessions.WCProxy = value

    def CloseAll(self):
        """Disconnect from all active sessions."""
        self._sessions.CloseAll()

    @session
    def Item(self, index):
        """Returns an element in the collection. The numeric index refers to the
        sequence that the sessions were opened. For example, Item(1) refers to
        the first session opened, Item(2) refers to the second session opened
        and so on"""
        return self._sessions.Item(index)

    @session
    def Open(self, sessName):
        """Returns an existing session and add it to the Sessions collection.
        If WebConnect applet is not running at the time of this call, then an
        attempt will be made to load the JRE 1.4 JVM and start up the applet
        based on the most recent properties set prior to this call. After the
        connection is made then a session is return and it is added to the
        Sessions collection. Every autostarted session will invoke its own copy
        of the JRE. Autostarted sessions should be configured by the
        WebConnect administrator to disable the File>New menu option.
        Java console style error messages may be reviewed in the file jvm.txt
        within the Windows c:\\Temp subdirectory."""
        return self._sessions.Open(sessName)
