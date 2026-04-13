import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def __init__(self, t):
        self.t = t

    def printString(self, s, current=None):
        print(self.t, s)
        return s + "*"

    def countWords(self, s, current=None):
        count = len(s.split())
        print(self.t, f"countWords({s!r}) = {count}")
        return count

    def toUpperCase(self, s, current=None):
        result = s.upper()
        print(self.t, f"toUpperCase({s!r}) = {result!r}")
        return result

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 5678")
object1 = PrinterI("Object1 says:")
object2 = PrinterI("Object2 says:")
adapter.add(object1, communicator.stringToIdentity("SimplePrinter1"))
adapter.add(object2, communicator.stringToIdentity("SimplePrinter2"))
adapter.activate()

communicator.waitForShutdown()
