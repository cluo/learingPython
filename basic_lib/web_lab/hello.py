__author__ = 'admin'
import web

urls = ('/hello',"hello")
app = web.application(urls, globals())

class hello:
	def GET(self): return 'hello'

ret = app.request('/hello').data
print ret
