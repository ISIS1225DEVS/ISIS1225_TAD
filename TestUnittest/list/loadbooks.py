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
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
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
lst_tags=  lt.newList('ARRAY_LIST')

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

