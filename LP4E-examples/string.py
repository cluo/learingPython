__author__ = 'admin'
print len('abc')
print 'abc' + 'DEF'
print 'n1' * 4
mantra = """
always look
on the bright
side of life
"""
myjob = "hacker"
for c in myjob:print(c,)
S = 'spam'
print S[0],S[-1],S[-2],S[1:3],S[1:]
print S[:2]+'cluo'+S[2:]
print S.replace('am','cluo')
print 'That is %d %s bird' % (1, 'dead')
print 'That is {0} {1} bird'.format(1, 'dead')

S = 'spammy'
S = S[:3] + 'xx' + S[5:]
print S
S.replace('mm', 'xx')
print S

S = 'spammy'
L = list(S)
print L

L[1]='C'
L[2]='L'
print ''.join(L)

print ','.join(L)
L = ['eggs', 'sausage', 'ham', 'toast']
print 'SPAM'.join(L)

line = 'aaa bbb ccc'
cols = line.split()
print cols

line = 'bob,hacker,40'
cols = line.split(',')
print cols

line = 'the knights who say ni\n'
print line
line.rstrip()
print line
print line.upper()
print line.isalpha()
print line.startswith('the')
print line.endswith('ni\n')
print '%d %s %d your' % (1, 'spam', 4)
print "%s--%s--%s" %(42, 3.14159, [1, 2 ,3])
print '%f, %.2f, %.3f' % (1/3.0, 1/3.0, 1/3.0)



print "%(n)d %(x)s" %{"n":1, 'x':'spam'}

replay="""
Greeting..
Hello %(name)s!
your age squared is %(age)s
"""
values = {"name":'bob','age':40}
print(replay % values)


template = '{0},{1} and {2}'
print template.format('spam','ham', 'eggs')

template = '{name},{age},{sex}'
print template.format(name='cluo',age=16,sex='boy')

x =  '{motto},{0} and {food}'.format(42,motto=3.14,food=[1, 2])
arr = x.split(' and ')
print arr
print x.replace('and','cluocluocluo')
somelist = list('SPAM')
print somelist
print 'first={0[0]},third={0[2]}'.format(somelist)
print 'first={0},last={1}'.format(somelist[0],somelist[-1])

parts = somelist[0], somelist[-1], somelist[1:3]
x = 'first={0}, last={1}, middle={2}'.format(*parts)
print x
