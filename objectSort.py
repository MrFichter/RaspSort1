#! /usr/bin/python

import re

class Movie (object): #Shows I'm making a basic Python data type.


	def __init__(self, name, year):
		self.name = name
		self.year = year

for line in open ("filmList.txt", "r"):
	search = re.search('([A-z 0-9]*) \((.*)\)' , line )# When I have \
#parentheses not preceeded by an escape character, I'm telling re to \
#be sensitive to the groups within the pattern. I can then use re.group.

#I originally used re.match, but match starts at the very beginning of \
#the file, where there was some crud. I also originally had two .* \
#expressions, but I turned the first one into square brackets followed \
#by stars to make sure it only picks up clean characters. (Anything, \
#upper or lower case, from A to Z, the space character, and digits.) \
#The star means I could have any number of them.

	print search.groups()
	

