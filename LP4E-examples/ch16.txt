if test:
    def func():            # Define func this way
        ...
else:
    def func():            # Or else this way
        ...
...
func()                     



othername = func           # Assign function object
othername()                # Call func again



def func(): ...            # Create function object
func()                     # Call object
func.attr = value          # Attach attributes



>>> def times(x, y):       # Create and assign function
...     return x * y        # Body executed when called
...



>>> times(2, 4)             # Arguments in parentheses
8



>>> x = times(3.14, 4)      # Save the result object
>>> x
12.56



>>> times('Ni', 4)          # Functions are "typeless"
'NiNiNiNi'



def intersect(seq1, seq2):
    res = []                     # Start empty
    for x in seq1:               # Scan seq1
        if x in seq2:            # Common item?
            res.append(x)        # Add to end
    return res



>>> s1 = "SPAM"
>>> s2 = "SCAM"
>>> intersect(s1, s2)            # Strings
['S', 'A', 'M']



>>> [x for x in s1 if x in s2]
['S', 'A', 'M']



>>> x = intersect([1, 2, 3], (1, 4))      # Mixed types
>>> x                                     # Saved result object
[1]



