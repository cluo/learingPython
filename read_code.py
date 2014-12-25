fname = raw_input('enter file to read:')
try:
    fobj = open(fname,'r')
except IOError,e:
    print 'open file error:',e
else:
    for eachLine in fobj:
        print eachLine,
    fobj.close()


