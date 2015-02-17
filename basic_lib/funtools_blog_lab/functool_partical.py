#-*- coding:utf8 -*-

__author__ = 'admin'
# 应用:
#
# 典型的，函数在执行时，要带上所有必要的参数进行调用。
#
# 然后，有时参数可以在函数被调用之前提前获知。
#
# 这种情况下，一个函数有一个或多个参数预先就能用上，以便函数能用更少的参数进行调用。
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

A = partial(A,a="1",b='2');
A((1,2,3,4),b=4,c=5)


A = partial(A,a="1",b='2');
A()




def add(a, b):
    return a + b
print add(4, 2)

plus3 = partial(add,5)
print plus3(4)
