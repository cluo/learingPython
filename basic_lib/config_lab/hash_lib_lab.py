__author__ = 'admin'
import hashlib
m = hashlib.md5()
m.update("Nobody")
print m.digest()
print m.hexdigest()
m.update("Nobody1")
print m.digest()
print m.hexdigest()