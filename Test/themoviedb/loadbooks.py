import config as cf
from TAD import list as lt
from DataStructures import listiterator as it
import csv

def loadCSVFile (file, lst):
    input_file = csv.DictReader(open(file))
    for row in input_file:  
        lt.addLast(lst,row)

def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)


print ('Creating movies list')
lst_movies= lt.newList()
print ('Creating casting list')
lst_casting =  lt.newList()


print ('Loading movies')
moviesfile = cf.data_dir + 'themoviedb/AllMoviesDetailsCleaned-1.csv'
loadCSVFile (moviesfile, lst_movies)
print (lst_movies['size'])
#printList (lst_books)

print ('Loading movies')
moviesfile = cf.data_dir + 'themoviedb/AllMoviesDetailsCleaned-2.csv'
loadCSVFile (moviesfile, lst_movies)
print (lst_movies['size'])
#printList (lst_books)

print ('Loading casting')
castingfile = cf.data_dir + 'themoviedb/AllMoviesCastingRaw.csv'
loadCSVFile (castingfile, lst_casting)
print (lst_casting['size'])
#printList (lst_tags)
