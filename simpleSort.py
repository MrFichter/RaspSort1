#! /usr/bin/python

names = ('Alvin Apples' , 'Bob Banana' , 'Barry Berries' , 'Cal Cherry' )
#Eventually, I'll get rid of the names list and will use:
#for line in open ('simpleList.txt', 'r'):

class Name (object):

	def __init__(self, first, last):
		self.first = first
		self.last = last

	def __repr__(self):
		return self.first + ' ' + self.last


nameObjectList = []


nameObjectList.append ( [Name (*fullName.rsplit() ) for fullName in names ] )


for nameObject in nameObjectList: print nameObject



#The reason I'm using a class is because I want, eventually, to do this:

nameObjectList.sort (key = lambda nameObject: nameObject.first)
#nameObjectList.sort (key = lambda nameObject: nameObject.last)
#for nameObject in nameObjectList: print nameObject

#error message I get:

'''
Traceback (most recent call last):
  File "simpleSort.py", line 29, in <module>
    nameObjectList.sort (key = lambda nameObject: nameObject.first)
  File "simpleSort.py", line 29, in <lambda>
    nameObjectList.sort (key = lambda nameObject: nameObject.first)
AttributeError: 'list' object has no attribute 'first'
'''
