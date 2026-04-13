import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 172.31.51.75 -p 5678")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 172.31.51.75 -p 5678")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

rep = printer1.printString("Hello World from printer1!")
print(rep)
rep = printer2.printString("Hello World from printer2!")
print(rep)

count = printer1.countWords("Hello World from printer1!")
print(f"printer1 word count: {count}")
count = printer2.countWords("Hello World from printer2!")
print(f"printer2 word count: {count}")

upper = printer1.toUpperCase("Hello World from printer1!")
print(f"printer1 upper: {upper}")
upper = printer2.toUpperCase("Hello World from printer2!")
print(f"printer2 upper: {upper}")

communicator.waitForShutdown()
