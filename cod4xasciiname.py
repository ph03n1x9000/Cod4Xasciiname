__version__ = '0.0.1'
__author__ = 'Sh3llK0de'


import b3
import b3.plugin


class Cod4XasciinamePlugin(b3.plugin.Plugin):
    requiresConfigFile = False
    requiresVersion = '1.10'

    def onStartup(self):
        """
        Plugin startup.
        Hook into events.
        """
        self.registerEvent('EVT_CLIENT_AUTH', self.onauth)


    def onauth(self, event):
        """
        Handle clients as the are recognized by B3.
        Checks if the client's name is readable by B3 and changes it if not. 
        """
        client = event.client
        if not client.name or client.name == '':
            self.verbose('Client in slot %s has a name cannot be parsed, changing name.')
            self.console.write('b3_asciirename %s' % client.cid)
