# __author__ = 'admin'
# from multiprocessing import Process
# def worker():
# 	print 'worder'
# 	return
# if __name__ == '__main__':
# 	jobs = []
# 	for i in range(5):
# 		p = Process(target=worker)
# 		jobs.append(p)
# 		p.start()



from multiprocessing import Process

def f(name):
    print 'hello', name

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
