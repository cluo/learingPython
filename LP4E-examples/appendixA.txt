setenv PYTHONPATH /usr/home/pycode/utilities:/usr/lib/pycode/package1

export PYTHONPATH="/usr/home/pycode/utilities:/usr/lib/pycode/package1"



### file: C:\Python30\mypath.pth

c:\pycode\utilities
d:\pycode\package1




#### File: main.py
import sys
print(sys.argv)



c:\Python30> python main.py a b –c            # Most common: run a script file
['main.py', 'a', 'b', '-c']



c:\Python30> python -c "print(2 ** 100)"      # Read code from command argument
1267650600228229401496703205376

c:\Python30> python -c "import main"          # Import a file to run its code
['-c']

c:\Python30> python - < main.py a b –c        # Read code from standard input
['-', 'a', 'b', '-c']

c:\Python30> python - a b -c < main.py        # Same effect as prior line
['-', 'a', 'b', '-c']


c:\Python30> python -m main a b –c             # Locate/run module as script
['c:\\Python30\\main.py', 'a', 'b', '-c']




c:\Python30> python -m pdb main.py a b -c              # Debug a script
--Return--
> c:\python30\lib\io.py(762)closed()->False
-> return self.raw.closed
(Pdb) c

c:\Python30> C:\python26\python -m pdb main.py a b -c  # Better in 2.6?
> c:\python30\main.py(1)<module>()
-> import sys
(Pdb) c

c:\Python30> python -m profile main.py a b -c          # Profile a script

c:\Python30> python -m cProfile main.py a b -c         # Low-overhead profiler


c:\Python30> python –u main.py a b -c          # Unbuffered output streams 

c:\Python30> python -?





