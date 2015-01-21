__author__ = 'admin'
import gevent
from gevent.queue import Queue , Empty
from gevent.pywsgi import WSGIServer
import json

data_source = Queue()
def producer():
	while True:
		data_source.put_nowait('Hello world')
		gevent.sleep(1)

def ajax_endpoint(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type','application/json')
	]
	start_response(status, headers)
	while True:
		try:
			datum = data_source.get(timeout=5)
			yield json.dumps(datum)+'\n'
		except Empty:
			pass

gevent.spawn(producer)

WSGIServer(('',8085),ajax_endpoint).serve_forever()