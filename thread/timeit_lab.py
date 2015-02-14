#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cluo on 15-2-15
__author__ = 'cluo'
import timeit
# timeit 模块
#
# timeit 模块定义了接受两个参数的 Timer 类。两个参数都是字符串。
#  第一个参数是你要计时的语句或者函数。
# 传递给 Timer 的第二个参数是为第一个参数语句构建环境的导入语句。
#  从内部讲， timeit 构建起一个独立的虚拟环境， 手工地执行建立语句，然后手工地编译和执行被计时语句。
# 一旦有了 Timer 对象，最简单的事就是调用 timeit()，它接受一个参数为每个测试中调用被计时语句的次数，默认为一百万次；
# 返回所耗费的秒数。
# Timer 对象的另一个主要方法是 repeat()， 它接受两个可选参数。 第一个参数是重复整个测试的次数，
# 第二个参数是每个测试中调用被计时语句的次数。 两个参数都是可选的，它们的默认值分别是 3 和 1000000。
#  repeat() 方法返回以秒记录的每个测试循环的耗时列表。
# Python 有一个方便的 min 函数可以把输入的列表返回成最小值，如： min(t.repeat(3, 1000000))
# 你可以在命令行使用 timeit 模块来测试一个已存在的 Python 程序，而不需要修改代码。
# 具体可参见文档： http://docs.python.org/library/timeit.html

def test1():
    n=0
    for i in range(101):
        n+=i
    return n

def test2():
    return sum(range(101))

def test3():
    return sum(x for x in range(101))

if __name__=='__main__':
    from timeit import Timer
    t1=Timer("test1()","from __main__ import test1") #构建独立的虚拟环境 并且手动编译和执行语句
    t2=Timer("test2()","from __main__ import test2")
    t3=Timer("test3()","from __main__ import test3")
    print t1.timeit(1000000)
    print t2.timeit(1000000)
    print t3.timeit(1000000)   #调用语句次数
    print t1.repeat(3,1000000) #重复测试次数 调用语句的次数
    print t2.repeat(3,1000000)
    print t3.repeat(3,1000000)

#不推荐 的计算耗时的方法
from time import clock
def test():
    L=[]
    for i in range(100):
        L.append(i)
start=clock()
for i in range(1000000):
    test()
finish=clock()
print (finish-start)/1000000