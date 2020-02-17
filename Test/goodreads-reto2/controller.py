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
import model 
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from Sorting import mergesort as sort

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def initCatalog ():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


def loadData (catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadBooks(catalog)
    loadTags (catalog, compareTagNames)
    loadBooksTags(catalog)

#___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
#___________________________________________________


def loadBooks (catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por 
    cada uno de ellos, se crea en una tabla de simbolos de autores. A cada autor
    se le adiciona una referencia al libro que se esta procesando.
    """
    booksfile = cf.data_dir + 'GoodReads/books.csv'
    input_file = csv.DictReader(open(booksfile))
    for book in input_file:  
        # Se adiciona el libro a la lista de libros
        lt.addLast(catalog['books'],book)
        # Se obtienen los autores del libro
        authors = book['authors'].split(",")
        # Cada auto se crea en la tabla de simbolos del catalogo, y se 
        # crea un libro en la lista de dicho autor (apuntador al libro)
        for author in authors:
            model.addBookAuthor (catalog, author.strip(), book, compareAuthorsByName)
    sort.mergesort (catalog['books'],compareRatings)
    


def loadTags(catalog,compareTagNames):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + 'GoodReads/tags.csv'
    input_file = csv.DictReader(open(tagsfile))
    for tag in input_file:  
        model.addTag (catalog, tag, compareTagNames, compareIds)
    


def loadBooksTags (catalog):
    """
    Carga la información que asocia tags con libros. 
    Primero se localiza el tag y se le agrega la información leida. 
    Adicionalmente se le agrega una referencia al libro procesado.
    """
    booktagsfile = cf.data_dir + 'GoodReads/book_tags-small.csv'
    input_file = csv.DictReader(open(booktagsfile))
    for tag in input_file: 
        model.addBookTag (catalog, tag, compareIds, compareTagNames, compareGoodreadsId)


#___________________________________________________
#  Funciones para consultas
#___________________________________________________


def getBooksByAuthor (catalog, authorname):
    author = model.getBooksByAuthor (catalog, authorname, compareAuthorsByName)
    return author


def getBestBooks (catalog, number):
    books = catalog['books']
    bestbooks = lt.newList()
    for cont in range (1, number+1):
        book = lt.getElement (books, cont)
        lt.addLast (bestbooks, book)
    return bestbooks
    

def getBooksByTag (catalog, tagname):
    books = model.getBooksByTag (catalog, tagname, compareTagNames)
    return books


#___________________________________________________
#  Funciones Helper para comparación de Elementos
#___________________________________________________

def compareAuthorsByName (keyname, authorname):
    return  (keyname == authorname )    


def compareRatings (book1, book2):
    return ( float(book1['average_rating']) > float(book2['average_rating']))


def compareIds (id, tag):
    return (id  == tag['key'])


def compareGoodreadsId (id, book):
    return (id  == book['goodreads_book_id'])


def compareTagNames (name, tag):
    return (name  == tag['key'])

