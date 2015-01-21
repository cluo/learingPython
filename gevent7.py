__author__ = 'admin'
import gevent
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