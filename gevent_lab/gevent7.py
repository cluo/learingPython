__author__ = 'admin'
import gevent
# 就像任何其他成段代码，Greenlet也可能以不同的方式运行失败。 Greenlet可能未能成功抛出异常，不能停止运行，或消耗了太多的系统资源。
#
# 一个greenlet的状态通常是一个依赖于时间的参数。在greenlet中有一些标志， 让你可以监视它的线程内部状态：
#
# started -- Boolean, 指示此Greenlet是否已经启动
# ready() -- Boolean, 指示此Greenlet是否已经停止
# successful() -- Boolean, 指示此Greenlet是否已经停止而且没抛异常
# value -- 任意值, 此Greenlet代码返回的值
# exception -- 异常, 此Greenlet内抛出的未捕获异常
def win():
	return 'you win'
def fail():
	raise Exception('You fail at failing')
winner = gevent.spawn(win)
#loser = gevent.spawn(fail)
print(winner.started)
#print(loser.started)

try:
	gevent.joinall([winner])
except Exception as e:
	print('This will never be reached')

print(winner.value)
#print(loser.value)

print(winner.ready())
#print(loser.ready())

print(winner.successful())
#print(loser.successful(()))