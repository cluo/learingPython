__author__ = 'admin'
import gevent
from gevent.event import Event
evt = Event()
def setter():
	print("A:hey wat for me I havet to do something")
	gevent.sleep(3)
	print("Ok, I'm done")
	evt.set()

def waiter():
	print("I'll wait for your")
	evt.wait()
	print("It's abount time")

def main():
	gevent.joinall([
		gevent.spawn(setter),
		gevent.spawn(waiter),
		gevent.spawn(waiter),
		gevent.spawn(waiter),
	])
if __name__ == '__main__': main()



