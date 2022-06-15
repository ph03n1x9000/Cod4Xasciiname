__version__ = '1.0.0'
__author__ = 'Sh3llK0de'


import b3
import b3.plugin
from re import search


class Cod4XasciinamePlugin(b3.plugin.Plugin):
    requiresConfigFile = False
    requiresVersion = '1.10'

    def onStartup(self):
        """
        Plugin startup.
        Hook into auth events.
        """
        self.registerEvent('EVT_CLIENT_CONNECT', self.onconnect)

    def onconnect(self, event):
        """
        Handle connecting clients.
        Perform regex search for non-printable ASCII characters in name.
        Sends server request to name change script if found.
        """
        if search('[\x80-\xff]', event.client.exactName) is not None:
            self.console.write('b3_asciirename %s' % event.client.cid)
            self.verbose('Non-ASCII name detected: %s > CID%s' % (event.client.name, event.client.cid))
