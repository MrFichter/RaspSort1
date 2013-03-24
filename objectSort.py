#! /usr/bin/python

import re

class Movie (object): #Shows I'm making a basic Python data type.


	def __init__(self, name, year):
		self.name = name
		self.year = year


	def __repr__(self):
		'''When I call print below, it will access repr.'''
		return self.year + ' ' + self.name



movies = []

for line in open ("filmList.txt", "r"):
	search = re.search('([A-z 0-9\-!\:]*) \((.*)\)' , line )# When I have \
#parentheses not preceeded by an escape character, I'm telling re to \
#be sensitive to the groups within the pattern. I can then use re.group.

#I originally used re.match, but match starts at the very beginning of \
#the file, where there was some crud. I also originally had two .* \
#expressions, but I turned the first one into square brackets followed \
#by stars to make sure it only picks up clean characters. (Anything, \
#upper or lower case, from A to Z, the space character, and digits.) \
#The star means I could have any number of them.

#I also included characters like dash, colon, and exclamation point.

	movie = Movie(*search.groups())
# The above is the same as saying Movie (search.groups()[0], \
#search.groups()[1]) , but it tells Python to automatically unpack the \
#tuple.

#calling Movie above runs the constructor function, but I have to save \
#it to a variable.
	movies.append(movie)

movies.sort (key = lambda movie: movie.name) #sort by name, the secondary\
#criterion.

# I created a temporary function that takes the argument movie. 

	
movies.sort (key = lambda movie: movie.year) #sort by year, the \
#primary criterion.


for movie in movies: print movie 


