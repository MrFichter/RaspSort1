#! /usr/bin/python

#sort a file full of film names

#define a function that will return the year a film was made
#split the right side of the line a the first "("
def filmYear(film):
	return film.rsplit ('(',1)[1] 
	
#load the file into a list in Python memory
#and then close the file because the content is now in memory
with open ("filmlist.txt", "r") as file:
	filmlist = file.read().splitlines() 

##You skipped typing some stuff

print filmlist ##My test.
