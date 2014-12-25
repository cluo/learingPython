# Note: all the code in this chapter is abstract -- it won't run as is


class C2: ...                      # Make class objects (ovals)
class C3: ...
class C1(C2, C3): ...              # Linked to superclasses

I1 = C1()                          # Make instance objects (rectangles)
I2 = C1()                          # Linked to their classes



# C2 and C3 must exist in the following


class C1(C2, C3):                # Make and link class C1
    def setname(self, who):      # Assign name: C1.setname
        self.name = who          # Self is either I1 or I2

I1 = C1()                        # Make two instances
I2 = C1()
I1.setname('bob')                # Sets I1.name to ‘bob’
I2.setname('mel')                # Sets I2.name to ‘mel’
print(I1.name)                   # Prints ‘bob’



class C1(C2, C3):
    def __init__(self, who):     # Set name when constructed
        self.name = who          # Self is either I1 or I2

I1 = C1('bob')                   # Sets I1.name to ‘bob’
I2 = C1('mel')                   # Sets I2.name to ‘mel’
print(I1.name)                   # Prints ‘bob’



class Employee:                      # General superclass
    def computeSalary(self): ...     # Common or default behavior
    def giveRaise(self): ...
    def promote(self): ...
    def retire(self): ...



class Engineer(Employee):            # Specialized subclass
     def computeSalary(self): ...    # Something custom here



bob = Employee()                     # Default behavior
mel = Engineer()                     # Custom salary calculator



company = [bob, mel]                   # A composite object
for emp in company:
    print(emp.computeSalary())         # Run this object's version



def processor(reader, converter, writer):
    while 1:
        data = reader.read()
        if not data: break
        data = converter(data)
        writer.write(data)



class Reader:
    def read(self): ...              # Default behavior and tools
    def other(self): ...
class FileReader(Reader):
    def read(self): ...              # Read from a local file
class SocketReader(Reader):
    def read(self): ...              # Read from a network socket
...
processor(FileReader(...),   Converter,  FileWriter(...))
processor(SocketReader(...), Converter,  TapeWriter(...))
processor(FtpReader(...),    Converter,  XmlWriter(...))



