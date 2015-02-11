__author__ = 'admin'
import gevent
import gevent.monkey
import urllib

gevent.monkey.patch_all()
def test():
	with gevent.Timeout(2, False) as timeout:
		urllib.urlopen('http://www.twitter.com')
if __name__  == '__main__':
	g = gevent.spawn(test)
	g.join()