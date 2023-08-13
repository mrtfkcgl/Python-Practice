class IMultiFunctionDevice:
    def print(self):
        pass
    def scan(self):
        pass
    def copy(self):
        pass
    def fax(self):
        pass

class Printer(IMultiFunctionDevice): # type: ignore
    def print(self):
        print("Printing ..")
class Scanner(IMultiFunctionDevice):
    def scan(self):
        print("Scanning...")
class Copier(IMultiFunctionDevice):
    def copy(self):
        print("Copying ...")

"""
 ImultifunctionDevice interfac e with methods for printing,scanning copying and flaxing.
 -  This violates the ISP, Client should not be forced to depend on interfaces they do not use.
        ** Printer does not care copy etc..
"""

class IPrinter:
    def print(self):
        pass
class IScanner:
    def scan(self):
        pass
class ICopier:
    def copy(self):
        pass
class IFax:
    def fax(self):
        pass

class Printer(IPrinter):
    def print(self):
        print("Printing ..")
        
        
        
