import config 
from TAD import queue as q
from  DataStructures import listiterator as it
import csv

def loadCSVFile (file, queue):
    input_file = csv.DictReader(open(file))
    for row in input_file:  
        q.enqueue(queue,row)

def printQueue (queue):
    iterator = it.newIterator(queue)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        print (element)

print ('Creating books list')
queue_books= q.newQueue()
print ('Creating tag list')
queue_tags=  q.newQueue()
print ('Creating books-tag list')
queue_book_tags= q.newQueue()

print ('Loading books')
loadCSVFile ('/Users/dcorreal/Develop/python/ISIS1225/Data/books.csv', queue_books)
printQueue (queue_books)

print ('Loading tags')
loadCSVFile ('/Users/dcorreal/Develop/python/ISIS1225/Data/tags.csv', queue_tags)
printQueue (queue_tags)

print ('Loading books-tags')
loadCSVFile ('/Users/dcorreal/Develop/python/ISIS1225/Data/book_tags.csv', queue_book_tags)
printQueue (queue_book_tags)
