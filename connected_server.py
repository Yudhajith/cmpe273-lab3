from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Echoer(DatagramProtocol):

    def datagramReceived(self, data, address):
        print("%s " % repr(data))
        self.transport.write(data, address)

reactor.listenUDP(8225, Echoer())
reactor.run()

"""
Reference taken from the twisted website
"""