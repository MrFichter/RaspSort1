#! /usr/bin/python

class Name (object):

	def __init__(self, first, last):
		self.first = first
		self.last = last

	def __repr__(self):
		return '{0} {1}'.format(self.first, self.last)

nameObjectList =  [Name (*line.rsplit() ) \
for line in open ('simpleList.txt' , 'r') ]

nameObjectList.sort (key = lambda nameObject: nameObject.first)
nameObjectList.sort (key = lambda nameObject: nameObject.last)
for nameObject in nameObjectList: print nameObject
