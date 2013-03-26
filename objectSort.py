#! /usr/bin/python

import re

class Film (object): #Shows I'm making a basic Python data type.


	def __init__(self, name, year):
		self.name = name
		self.year = year


	def __repr__(self):
		'''When I call print below, it will access repr.'''
		return self.year + ' ' + self.name


filmList = []

for line in open ("filmList.txt", "r"):

	filmList.append(line)



search = re.search('([A-z 0-9\-!\:]*) \((.*)\)' , line )

filmListObjects = [Film(*search.groups()) for re.search('([A-z 0-9\-!\:]*) \((.*)\)' , film ) for film in filmList



filmListObjects.sort (key = lambda film: film.name) #sort by name, the secondary\
#criterion.

# I created a temporary function that takes the argument movie. 

	
filmListObjects.sort (key = lambda film: film.year) #sort by year, the \
#primary criterion.


for film in filmListObjects: print film


