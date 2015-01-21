def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
print mysum([1,2,3,4,5])

def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first,*rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first
def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

L = (1,2,3,4,5)
#print list(L)
#print min2(1,list)
print min1(*L)
print min2(1,*L)
print min3(*L)


def minmax(test, * args):
    res = args[0]
    for arg in args[1:]:
        if test(arg,res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y
print(minmax(lessthan,4,2,1,5,6,3))
print(minmax(grtrthan,4,2,1,5,6,3))