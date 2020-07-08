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


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar todos los libros,
    Adicionalmente, crea una lista vacia para los autores y una lista vacia para los 
    generos.   Retorna el catalogo inicializado.
    """
    catalog = {'books':None, 'authors':None, 'tags': None}
    catalog['books'] = lt.newList('ARRAY_LIST')
    catalog['authors'] = lt.newList('ARRAY_LIST')
    catalog['tags'] = lt.newList('ARRAY_LIST')
    return catalog


def newAuthor (name):
    """
    Crea una nueva estructura para modelar los libros de un autor y su promedio de ratings
    """
    author = {'name':"", "books":None,  "average_rating":0}
    author ['name'] = name
    author ['books'] = lt.newList('ARRAY_LIST')
    return author


def newTagBook (name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido 
    marcados con dicho tag.  Se guarga el total de libros y una lista con 
    dichos libros.
    """
    tag = {'name':'', 'tag_id':'', 'total_books':0, 'books':None, 'count':0.0 }
    tag ['name'] = name
    tag ['tag_id'] = id
    tag ['books'] = lt.newList ()
    return tag


# Funciones para agregar informacion al catalogo

def addBookAuthor (catalog, authorname, book, compareauthors):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias a los libros de dicho autor
    """
    authors = catalog['authors']
    posauthor = lt.isPresent (authors, authorname, compareauthors)
    if posauthor > 0:
        author = lt.getElement (authors,posauthor)    
    else:
        author = newAuthor(authorname)
        lt.addLast (authors, author)
    lt.addLast (author['books'], book)
    if (author['average_rating']==0.0):
        author['average_rating']= float (book['average_rating'])
    else:
        author['average_rating'] = (author['average_rating'] + float(book['average_rating']) ) / 2



def addTag (catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTagBook (tag['tag_name'], tag['tag_id'])
    lt.addLast (catalog['tags'], t)



def addBookTag (catalog, tag, comparefunction, comparegoodreadsid):
    """
    Agrega una relación entre un libro y un tag asociado a dicho libro
    """
    bookid = tag['goodreads_book_id']
    tagid = tag['tag_id']
    pos = lt.isPresent(catalog['tags'], tagid, comparefunction)
    if pos:
        tagbook = lt.getElement (catalog['tags'], pos)
        tagbook ['total_books'] += 1
        tagbook ['count'] += int (tag['count'])
        posbook = lt.isPresent(catalog['books'], bookid, comparegoodreadsid)
        if posbook:
            book =  lt.getElement (catalog['books'], posbook) 
            lt.addLast (tagbook['books'], book)


# Funciones de consulta

def getBooksByAuthor (catalog, authorname, compareauthors):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    posauthor = lt.isPresent (catalog['authors'], authorname, compareauthors)
    if posauthor > 0:
        author = lt.getElement (catalog['authors'], posauthor)
        return author
    return None


