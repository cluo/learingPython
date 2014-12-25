__author__ = 'admin'


def hello():
    "this is a dodument"
    return 'hello world';


print hello()

name = 'cluo'
sex = 'boy'

str = 'python'
print str[0]
print str[-1]
print str[1:-1]
print str[:3]

str = str + name + sex
print str

print str * 2
print '_' * 20
print str + '\n' + str

aList = [1, 2, 3, 4]
aTuple = (1, 2, 3, 3)
print aList[0]
print aList[:3]
print aTuple[:2]
print aTuple[:-1]
print aTuple[-1]

aDict = {'HOST': '19851129'}
aDict['port'] = 80
print aDict
print aDict['HOST']

x = 2
if x < 0:
    print 'less than 0'
elif x > 0:
    print 'more than 0'
else:
    print 'eq 0'

while x > 0:
    print 'x%d ' % (x)
    x -= 1
ret = ""
for item in ['hello', 'world', 'come', 'on']:
    ret += item
    print ret

ret = ""
for item in ['hello', 'world', 'come', 'on']:
    ret += item
    print ret,

for eachNum in range(4):
    print eachNum

who = 'knights'
what = 'ni!!'
print 'we are the %s say %s' % (who, (what + ' ') * 4)

foo = 'abc'
for c in foo:
    print c

foo = 'abc'
for c in foo:
    print c,

foo = 'abc'
for i in range(len(foo)):
    print foo[i], '(%d)' % i

for i, ch in enumerate(foo):
    print ch, '(%d)' % (i)

squared = [x ** 2 for x in range(4)]
for i in squared:
    print i

sqdEvents = [x ** 2 for x in range(8) if not x % 2]
for i in sqdEvents:
    print i

filename = raw_input('what is cluo?')
fobj = open('/Users/admin/cluo.txt', 'r')
for eachLine in fobj:
    print eachLine,
fobj.close()

# try:
#     filename = raw_input('what is cluo?')
#     fobj = open('/Users/admin/cluo.txt1', 'r')
#     for eachLine in fobj:
#      print eachLine,
#     fobj.close()
# except IOError,e:
#     print 'file open error:',e

def make_love(x,y):
    "aa bb cc"
    return (x + y)



def default_argument_test\
                (x=1,y=2):
    "aa bb cc"
    return (x + y)

print default_argument_test();print make_love(1,2);

x = y = z = 2
print x


#x, y, z = 1, 2, 'a string'
#print x,y,z


x = 3.14
y = x
y += 1
print x
print y