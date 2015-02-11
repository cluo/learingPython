__author__ = 'admin'
import functools
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


# def A(*args,**kargs):
#     print args,kargs.get('d')
# print A(1,2,3,4,5,65,6,7,7,a=3,b=5)

def A(*args, **kargs):
    print args,kargs;

A = functools.partial(A,a="1",b='2');
A((1,2,3,4),b=4,c=5)


A = functools.partial(A,a="1",b='2');
A()




def add(a, b):
    return a + b
print add(4, 2)

plus3 = functools.partial(add,5)
print plus3(4)
