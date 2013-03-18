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
##Me: This is one way to sort.
filmList.sort()

#sort by year using key to library function - the film list 
#must end with a year in the format (NNNN)
filmList.sort(key=filmYear)
##Me: This is another way to sort.
##'key =' expects a function. Many times, people use lambda
##notation to quickly create a function. The function is called
##'exactly once for each input record.' wiki.python.org/moin/HowTo/Sorting
##More on lambda notation: htt://tinyurl.com/pylambda

for film in filmList:
	print (film)
