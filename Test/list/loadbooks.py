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


print ('Creating books list')
lst_books= lt.newList()
print ('Creating tag list')
lst_tags=  lt.newList()
print ('Creating books-tag list')
lst_book_tags= lt.newList()
print ('Creating ratings list')
lst_ratings= lt.newList()
print ('Creating to-read list')
lst_to_read= lt.newList()

print ('Loading books')
booksfile = cf.data_dir + 'GoodReads/books.csv'
loadCSVFile (booksfile, lst_books)
print (lst_books['size'])
#printList (lst_books)


print ('Loading tags')
tagsfile = cf.data_dir + 'GoodReads/tags.csv'
loadCSVFile (tagsfile, lst_tags)
print (lst_tags['size'])
#printList (lst_tags)

print ('Loading books-tags')
booktagsfile = cf.data_dir + 'GoodReads/book_tags.csv'
loadCSVFile (booktagsfile, lst_book_tags)
print (lst_book_tags['size'])
#printList (lst_book_tags)

print ('Loading ratings')
ratingsfile = cf.data_dir + 'GoodReads/ratings.csv'
loadCSVFile (ratingsfile, lst_ratings)
print (lst_ratings['size'])
#printList (lst_ratings)

print ('Loading books to read')
toreadfile = cf.data_dir + 'GoodReads/to_read.csv'
loadCSVFile (toreadfile, lst_to_read)
print (lst_to_read['size'])
#printList (lst_to_read)

