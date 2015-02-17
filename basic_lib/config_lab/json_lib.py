#-*- coding:utf8 -*-
__author__ = 'admin'
import json


#encode json
obj= ['foo',{'bar': ('baz','none','1.0',2)}]
print json.dumps(obj)
obj = {'b':2, 'c':3 ,'a':1 }
print json.dumps(obj, sort_keys=True)



#decode json
# obj = json.loads("{'a':1,'b':2,'c':3}")
print obj
