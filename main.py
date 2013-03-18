#! /usr/bin/python

#sort a file full of film names

#define a function that will return the year a film was made
#split the right side of the line a the first "("
def filmYear(film):
	return film.rsplit ('(',1)[1] 
	
#load the file into a list in Python memory
#and then close the file because the content is now in memory
with open ("filmList.txt", "r") as file:
	filmList = file.read().splitlines() 

#sort by name using library function
filmList.sort()

print filmList
##my test
##You skipped typing some stuff

