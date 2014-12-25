>>> if 1:
...     print('true')
...
true



>>> if not 1:
...     print('true')
... else:
...     print('false')
...
false



>>> x = 'killer rabbit'
>>> if x == 'roger':
...     print("how's jessica?")
... elif x == 'bugs':
...     print("what's up doc?")
... else:
...     print('Run away! Run away!')
...
Run away! Run away!



>>> choice = 'ham'
>>> print({'spam':  1.25,         # A dictionary-based 'switch'’
...        'ham':   1.99,         # Use has_key or get for default
...        'eggs':  0.99,
...        'bacon': 1.10}[choice])
1.99



>>> if choice == 'spam':
...     print(1.25)
... elif choice == 'ham':
...     print(1.99)
... elif choice == 'eggs':
...     print(0.99)
... elif choice == 'bacon':
...     print(1.10)
... else:
...     print('Bad choice')
...
1.99



>>> branch = {'spam': 1.25,
...           'ham':  1.99,
...           'eggs': 0.99}

>>> print(branch.get('spam', 'Bad choice'))
1.25
>>> print(branch.get('bacon', 'Bad choice'))
Bad choice



>>> choice = 'bacon'
>>> if choice in branch:
...     print(branch[choice])
... else:
...     print('Bad choice')
...
Bad choice



x = 1
if x:
    y = 2
    if y:
        print('block2')
    print('block1')
print('block0')



  x = 'SPAM'                        # Error: first line indented
if 'rubbery' in 'shrubbery':
    print(x * 8)
        x += 'NI'                   # Error: unexpected indentation
        if x.endswith('NI'):
                x *= 2
            print(x)                # Error: inconsistent indentation



x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)                    # Prints "SPAMNISPAMNI"   



L = ["Good",
     "Bad",
     "Ugly"]                     # Open pairs may span lines



if a == b and c == d and   \
   d == e and f == g:
   print('olde')                 # Backslashes allow continuations...



if (a == b and c == d and
    d == e and e == f):
    print('new')                 # But parentheses usually do too



x = 1 + 2 + 3 \                  # Omitting the \ makes this very different...
+4



x = 1; y = 2; print(x)           # More than one simple statement


S = """
aaaa
bbbb        
cccc"""

S = ('aaaa'        
     'bbbb'                      # Comments here are ignored
     'cccc')



if 1: print('hello')             # Simple statement on header line



>>> 2 < 3, 3 < 2        # Less-than: return True or False (1 or 0)
(True, False)



>>> 2 or 3, 3 or 2      # Return left operand if true
(2, 3)                  # Else, return right operand (true or false)
>>> [] or 3
3
>>> [] or {}
{}



>>> 2 and 3, 3 and 2    # Return left operand if false
(3, 2)                  # Else, return right operand (true or false)
>>> [] and {}
[]
>>> 3 and []
[]



if X:
    A = Y
else:
    A = Z


A = Y if X else Z


>>> A = 't' if 'spam' else 'f'      # Nonempty is true
>>> A
't'
>>> A = 't' if '' else 'f'
>>> A
'f'


A = ((X and Y) or Z)

A = [Z, Y][bool(X)]

>>> ['f', 't'][bool('')]
'f'
>>> ['f', 't'][bool('spam')]
't'



X = A or B or C or None

X = A or default

if f1() or f2(): ...

tmp1, tmp2 = f1(), f2()
if tmp1 or tmp2: ...


             

