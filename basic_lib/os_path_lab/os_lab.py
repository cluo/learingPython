__author__ = 'admin'
import os.path
import sys
logfile = os.path.join('logs', os.path.basename(os.path.realpath(sys.argv[0])).replace('.py','.log'))
print logfile

#logs/os_lab.log