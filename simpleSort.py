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

nameObjectList = [Name (*fullName.rsplit() ) for fullName in names ]

nameObjectList.sort (key = lambda nameObject: nameObject.first)
nameObjectList.sort (key = lambda nameObject: nameObject.last)
for nameObject in nameObjectList: print nameObject

