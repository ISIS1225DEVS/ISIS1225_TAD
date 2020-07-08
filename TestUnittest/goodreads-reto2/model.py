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

from ADT import list as lt
from ADT import map as map
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá  una lista para los libros, 
Los autores y los generos se guardaran en 
tablas de simbolos
"""

# Construccion de modelos

def newCatalog(compareBookIds, compareAuthorsByName, compareTagNames, compareIds):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar todos los libros,
    Adicionalmente, crea una lista vacia para los autores y una lista vacia para los 
    generos.   Retorna el catalogo inicializado.
    """
    catalog = {'books':None, 'bookIds':None, 'authors':None, 'tags': None, 'tagIds': None}
    catalog['books'] = lt.newList('ARRAY_LIST')
    catalog['bookIds'] = map.newMap (20011, maptype='PROBING', comparefunction=compareBookIds)
    catalog['authors'] = map.newMap (12007, maptype='PROBING', comparefunction=compareAuthorsByName )
    catalog['tags'] = map.newMap (17021, maptype='CHAINING', comparefunction=compareTagNames)
    catalog['tagIds'] = map.newMap (17021, maptype='CHAINING', comparefunction=compareIds)
    return catalog


def newAuthor (name):
    """
    Crea una nueva estructura para modelar los libros de un autor y su promedio de ratings
    """
    author = {'name':"", "books":None,  "average_rating":0}
    author ['name'] = name
    author ['books'] = lt.newList('SINGLE_LINKED')
    return author

def newBook (bookRow):
    """
    Crea una nueva estructura para modelar los libros y su promedio de ratings
    """
    book = {"book_id": bookRow['book_id'], "title":bookRow['title'], "average_rating":bookRow['average_rating'], "ratings_count":bookRow['ratings_count']}
    return book



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

def addBookAuthor (catalog, authorname, book):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias a los libros de dicho autor
    """
    authors = catalog['authors']
    existauthor = map.contains (authors, authorname)

    if existauthor:
        entry = map.get (authors,authorname)  
        author =  entry['value'] 
    else:
        author = newAuthor(authorname)
        map.put (authors, authorname, author)
    lt.addLast (author['books'], book)

    # Se crea un indice para buscar libros x id
    map.put(catalog['bookIds'], book['goodreads_book_id'], book )

    if (author['average_rating']==0.0):
        author['average_rating']= float (book['average_rating'])
    else:
        author['average_rating'] = (author['average_rating'] + float(book['average_rating']) ) / 2



def addTag (catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTagBook (tag['tag_name'], tag['tag_id'])
    map.put (catalog['tags'], tag['tag_name'], t)
    map.put (catalog['tagIds'], tag['tag_id'], t)



def putMapBook (catalog, bookRow):
    book= newBook(bookRow)
    map.put (catalog['bookIds'], book['book_id'],book )



def addBookTag (catalog, tag):
    """
    Agrega una relación entre un libro y un tag asociado a dicho libro
    """
    bookid = tag['goodreads_book_id']
    tagid = tag['tag_id']
    entry = map.get(catalog['tagIds'], tagid)

    if entry:
        tagbook = map.get (catalog['tags'], entry['value']['name'])
        tagbook ['value']['total_books'] += 1
        tagbook ['value']['count'] += int (tag['count'])
        book = map.get (catalog['bookIds'],bookid)
        if book:
            lt.addLast (tagbook['value']['books'], book['value'])

#==============================
# Funciones de consulta
#==============================

def getBooksByAuthor (catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    author = map.get (catalog['authors'], authorname)
    if author:
        return author['value']
    return None


def getBooksByTag (catalog, tagname):
    """
    Retornar la lista de libros asociados a un tag 
    """    
    tag = map.get (catalog['tags'], tagname)
    books = None
    if tag:
        books = tag['value']['books']
    return books


def compareBookIds (id1, id2):
    return (id1  == id2)
