>>> a = 3



>>> a = 3          # It's an integer
>>> a = 'spam'     # Now it's a string
>>> a = 1.23       # Now it's a floating point



>>> a = 3
>>> a = 'spam'



>>> x = 42
>>> x = 'shrubbery'      # Reclaim 42 now (unless referenced elsewhere)
>>> x = 3.1415           # Reclaim 'shrubbery' now
>>> x = [1, 2, 3]        # Reclaim 3.1415 now



>>> a = 3
>>> b = a
>>> a = 'spam'



>>> a = 3
>>> b = a
>>> a = a + 2



>>> L1 = [2, 3, 4]
>>> L2 = L1
>>> L1 = 24



>>> L1 = [2, 3, 4]    # A mutable object
>>> L2 = L1           # Make a reference to the same object
>>> L1[0] = 24        # An in-place change
>>> L1                # L1 is different
[24, 3, 4]
>>> L2                # But so is L2!
[24, 3, 4]



>>> L1 = [2, 3, 4]
>>> L2 = L1[:]        # Make a copy of L1
>>> L1[0] = 24
>>> L1
[24, 3, 4]
>>> L2                # L2 is not changed
[2, 3, 4]



import copy
X = copy.copy(Y)         # Make top-level "shallow" copy of any object Y
X = copy.deepcopy(Y)     # Make deep copy of any object Y: copy all nested parts



>>> x = 42
>>> x = 'shrubbery'      # Reclaim 42 now



>>> L = [1, 2, 3]
>>> M = L                # M and L reference the same object
>>> L == M               # Same value
True
>>> L is M               # Same object
True



>>> L = [1, 2, 3]
>>> M = [1, 2, 3]        # M and L reference different objects
>>> L == M               # Same values
True
>>> L is M               # Different objects
False



>>> X = 42
>>> Y = 42               # Should be two different objects
>>> X == Y
True
>>> X is Y               # Same object anyhow: caching at work!
True



>>> import sys
>>> sys.getrefcount(1)   # 837 pointers to this shared piece of memory
837



A = "spam"
B = A
B = "shrubbery"

A = ["spam"]
B = A
B[0] = "shrubbery"

A = ["spam"]
B = A[:]
B[0] = "shrubbery"

