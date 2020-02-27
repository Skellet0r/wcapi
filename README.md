# wcapi

Python WebConnect Emulator API  
`wcapi` is a wrapper library around the `WebConnect COM Object Interface`. It allows users to interact with the System, Sessions, and Screen objects from within python.
The methods and properties of the various objects are described in the WebConnect COM Object Reference Guide Edition 7.

## Prerequisites

The `WebConnect Emulation APIs` need to be installed and registered on your system.
The MSI installer can be found at the following [link](https://webconnect-demo.openconnect.com) under **Downloads**. A torrent file for the MSI installer can also be found at the following [link](http://www.mediafire.com/file/50q6ho1bu0pm6ch/wccomobj.msi.torrent/file).

## Installation

**via pip**

```shell
$ pip install git+https://github.com/Skellet0r/wcapi.git#egg=wcapi
```

**via git**

```shell
$ git clone https://github.com/Skellet0r/wcapi.git
$ pip install ./wcapi
```

> To learn more about `pip` VCS Support check out the [docs](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support)
