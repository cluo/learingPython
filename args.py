from inter2 import intersect,union
s1,s2,s3 = "SPAM",'SCAM','SLAM'
print intersect(s1,s2)
print union(s1,s2)
def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])
print mysum([1,2,3,4,5])

def mysum(L):
    return L[0] if len(L)==1 else L[0] + mysum(L[1:])

print mysum([1,2,3,4,5])


def echo(message):
    print(message)
echo('Direct call')
x = echo
x('indirect call!')

def indirect(func,arg):
    func(arg)
indirect(echo,'Argument call')
schedule = [ (echo,'spam'),(echo,'ham') ]
for(func ,arg) in schedule:
    func(arg)
def make(label):
    def echo(message):
        print(label+':'+message)
    return echo
F = make('Spam')
F('Ham!')

F = make('bb')
F('cluoa')

def fun(a):
    b='spam'
    return b*a
print fun(3)
print fun.__name__
print dir(fun)
dir(fun.__code__)
print fun.__code__.co_varnames
print fun.__code__.co_argcount
fun.count =0
fun.count+=1
print fun.count
# def fun(a:int=1,b:float=2.2,c:(1,3)=3)->int:
#     return a + b + c

f = lambda x,y,z:x + y +z
print f(2, 3, 4)

def knights():
    title = 'sir'
    action = (lambda x:title + ' ' + x)
    return action
act = knights()
print act('sssss')
# L = [lambda x:x**2,
#      lambda x:x **3,
#      lambda x:x ** 4]
# for f in L:
#     print(f(2))

key = 'got'
ret = {
    'already':(lambda x: x + 2),
    'got':(lambda x: x * 4),
    'one':(lambda x: x ** 6)}[key]
print ret(3)

def inc(x): return x + 10
counters = [1, 2, 3, 4, 5]
print list(map(inc,counters))
print list(map((lambda x:x+3),counters))
def mymap(func, seq):
    res = []
    for x in seq:res.append(func(x))
    return res

print list( filter(lambda x:x>0, range(-5,5)))
res = []
for x in range(-5,5):
    if x > 0:
        res.append(x)
print res

def myreduce(fun,sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = fun(tally,next)
    return tally
print myreduce((lambda x,y:x +y),[1,2,3,4,5])

print [ord(x) for x in 'spam']
print [x ** 2 for x in range(10)]

print [x for x in range(5) if x % 2 == 0]
print list(filter(lambda x:  x % 2 ==0,range(5)))


res = [ x + y for x in [0, 1, 2] for y in [100, 200 ,300]]
print res

print [x + y for x in 'spam' for y in 'SPAM']
print [(x,y) for x in range(5) if x %2 ==0 for y in range(5) if y %2 ==1]

M = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print [row[1] for row in M]

print open('cluo').readlines()
print [line.rstrip() for line in open('cluo').readlines()]
print [line.rstrip() for line in open('cluo')]
print list( map((lambda line:line.rstrip()),open('cluo')))



def gensquares(N):
    for i in range(N):
        yield i ** 2
for i in gensquares(5):
    print i;

ret = gensquares(4)
print next(ret)
print next(ret)
print next(ret)

for x in [n ** 2 for n in range(5)]:
    print(x)
for x in map((lambda n:n ** 2),range(5)):
    print x

G =  (x ** 2 for x in range(4))
print next(G)
print next(G)
for num in (x ** 2 for x in range(4)):
    print('%s,%s' % (num,num/2.0))
print sum(x ** 2 for x in range(4))
print sorted((x ** 2 for x in range(4)),reverse=True)
G = (c * 4 for c in 'SPAM')
print iter(G) is G
I1 = iter(G)
print next(I1)

I2 = iter(G)
print next(I2)

L = [1, 2, 3, 4]
I1,I2 = iter(L),iter(L)
print next(I1)
print next(I2)
S1 = 'abcd'
S2 = 'xyz1'
print list(zip(S1,S2))

def mymap(fun, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(fun(*args))
    return res
print mymap(abs,[-2,1,3,4])

def myzip(*seqs):
    seqs =[list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)
def mymapPad(pad=22,*seqs):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)
S1, S2 = 'abc','xyz123'
print(list(myzip(S1,S2)))
print list(mymapPad('cctv',S1,S2))

def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]
def mymapPad(pad=None,*seqs):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S)>i else pad) for S in seqs) for i in index]



def myzip(*args):
    iters = map(iter,args)
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)

keys = [1,2,3,4]
values = ['a','b','c','d']
ret = {key:value for(key,value) in zip(keys,values)}
print ret
print dict(zip(keys,values))

# fun = [
#     (lambda x:x**2),
#     (lambda x:x**3)
# ]
# S =[1,2,3]
# funs = set(f(x) for x in fun)


print {x * x for x in range(10)}
print {x:x*x for x in range(10)}

print {x+y for x in [1, 2, 3] for y in [4, 5, 6]}#qu chong
print {x:y for x in [1, 2, 3] for y in [4, 5, 6]} #qu hcong

# import time
# reps = 1000
# repslist = range(reps)
# def timer(func,*pargs,**kargs):
#     start = time.clock()
#     for i in repslist:
#         ret = func(*pargs,**kargs)
#     elapsed = time.clock() - start
#     return (elapsed,ret)
import time
reps = 1000
reslist = range(reps)


