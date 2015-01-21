__author__ = 'admin'
from first import FirstClass
class SecondClass(FirstClass):
	def display(self):
		print self.name*2

C2 = SecondClass('cc')
C2.display()


class ThirdClass(SecondClass):
	def __init__(self, value):
		self.data = value
	def __add__(self, other):
		return ThirdClass(self.data + other)
	def __str__(self):
		return '[ThirdClass:%s]' % self.data
	def mul(self, other):
		self.data *= other
		return self.data
C3 = ThirdClass('abc')
print C3
print C3 + 'CCTV'
print C3.mul(4)


class Person:
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		return int(self.pay*(1+percent))
	def __str__(self):
		return '[Person:%s, %s]' %(self.name, self.job)

class Manager(Person):
	def __init__(self,name,job,pay):
		Person.__init__(self, name, job, pay)
	def giveRaise(self,pecent,bonus=10):
		return Person.giveRaise(self,pecent+bonus)

class Department:
	def __init__(self, *args):
		self.member = list(args)
	def addMember(self, person):
		self.member.append(person)
	def giveRaise(self, percent):
		list = []
		for person in self.member:
			list.append(person.giveRaise(percent))
		print list
	def showAll(self):
		for person in self.members:
			print person
	def getMember(self):
		return self.member

if __name__ == '__main__':
	bob = Person('Bob Smith','IT',pay=20)
	sue = Person('Cluo',job='ff',pay=10000000)
	print(bob.name, bob.pay,bob.job)
	print(sue.name, sue.pay,sue.job)
	print bob.lastName()
	print bob.giveRaise(.10)
	print bob
	tom = Manager('Tom jones',job='tom', pay=10)
	print tom
	print tom.name
	print tom.pay
	#print tom.giveRaise(.2, .1)
	D1 = Department(bob, sue)
	D1.addMember(tom)
	D1.giveRaise(.2)
	print D1.getMember()

	print bob.__class__
	print bob.__class__.__name__
	print list(bob.__dict__.keys())


