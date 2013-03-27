#! /usr/bin/python

names = ('Cal Cherry' , 'Alvin Apples' , 'Bob Banana' , 'Barry Banana' )

class Name (object):

	def __init__(self, first, last):
		self.first = first
		self.last = last

	def __repr__(self):
		return self.first + ' ' + self.last

nameObjectList = []

for fullName in names:
	name = Name (*fullName.rsplit())
	nameObjectList.append (name)
	
nameObjectList.sort (key = lambda nameObject: nameObject.first)
nameObjectList.sort (key = lambda nameObject: nameObject.last)

print '\n\nThe original, unsorted list is:'
for name in names: print name

print '\n\nThe sorted list is:'
for nameObject in nameObjectList: print nameObject
