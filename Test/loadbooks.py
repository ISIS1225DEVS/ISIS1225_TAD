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


print ('Loading books')
booksfile = cf.data_dir + 'GoodReads/books.csv'
loadCSVFile (booksfile, lst_books)
print (lst_books['size'])
printList (lst_books)


print ('Loading tags')
tagsfile = cf.data_dir + 'GoodReads/tags.csv'
loadCSVFile (tagsfile, lst_tags)
print (lst_tags['size'])
printList (lst_tags)

print ('Loading books-tags')
booktagsfile = cf.data_dir + 'GoodReads/book_tags.csv'
loadCSVFile (booktagsfile, lst_book_tags)
print (lst_book_tags['size'])
printList (lst_book_tags)



