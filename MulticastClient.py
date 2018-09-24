from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class MulticastHelloer(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup("228.0.0.5")
        # Send to 228.0.0.5:8005 - all listeners on the multicast address
        # (including us) will receive this message.
        self.transport.write(b'Hello World', ("228.0.0.5", 8005))

    def datagramReceived(self, datagram, address):
        print("%s " % repr(datagram))
        reactor.stop()

        
reactor.listenMulticast(8005, MulticastHelloer(), listenMultiple=True)
reactor.run()

"""
Reference taken from the twisted website
"""