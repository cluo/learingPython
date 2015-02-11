__author__ = 'admin'
import datetime
def get_cur_datetime():
	return "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
print datetime.datetime.now()
print get_cur_datetime()
