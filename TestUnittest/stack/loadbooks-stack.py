"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import csv
from ADT import queue as q
from  DataStructures import listiterator as it


def loadCSVFile (file, queue):
    input_file = csv.DictReader(open(file))
    for row in input_file:  
        q.enqueue(queue,row)

def printQueue (queue):
    iterator = it.newIterator(queue)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        print (element)

print ('Creating books queue')
lst_books= q.newQueue()

print ('Creating tag queue')
lst_tags=  q.newQueue('ARRAY_LIST')

print ('Creating books-tag queue')
lst_book_tags= q.newQueue()

print ('Creating ratings queue')
lst_ratings= q.newQueue()

print ('Creating to-read queue')
lst_to_read= q.newQueue()

print ('Loading books')
booksfile = cf.data_dir + 'GoodReads/books.csv'
loadCSVFile (booksfile, lst_books)
print (lst_books['size'])
printQueue (lst_books)


print ('Loading tags')
tagsfile = cf.data_dir + 'GoodReads/tags.csv'
loadCSVFile (tagsfile, lst_tags)
print (lst_tags['size'])
printQueue (lst_tags)

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