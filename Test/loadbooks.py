import config
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
loadCSVFile ('/Users/dcorreal/Develop/python/ISIS1225/Data/books.csv', lst_books)
printList (lst_books)


print ('Loading tags')
loadCSVFile ('/Users/dcorreal/Develop/python/ISIS1225/Data/tags.csv', lst_tags)
printList (lst_tags)

print ('Loading books-tags')
loadCSVFile ('/Users/dcorreal/Develop/python/ISIS1225/Data/book_tags.csv', lst_book_tags)
printList (lst_book_tags)



