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


import config 
from ADT import queue as q
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
