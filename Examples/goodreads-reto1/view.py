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
import sys
import controller 
import csv
from ADT import list as lt
from DataStructures import listiterator as it

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Consultar los Top x libros por promedio")
    print("4- Consultar los libros de un autor")
    print("5- Libros por género")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def printAuthorData (author):
    if author:
        print ('Autor encontrado: ' + author['name'])
        print ('Promedio: ' + str(author['average_rating']))
        print ('Total de libros: ' + str(lt.size(author['books'])))
        iterator = it.newIterator(author['books'])
        while  it.hasNext(iterator):
            book = it.next(iterator)
            print ('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
    else:
        print ('No se encontro el autor')



def printBestBooks (books):
    size = lt.size(books)
    if size:
        print (' Estos son los mejores libros: ')
        iterator = it.newIterator(books)
        while  it.hasNext(iterator):
            book = it.next(iterator)
            print ('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'] + ' Rating: ' + book['average_rating'])
    else:
        print ('No se encontraron libros')



"""
Menu principal
"""
while True:
    printMenu()
    inputs =input('Seleccione una opción para continuar\n')
    if int(inputs[0])==1:
        print("Inicializando Catálogo ....")
        catalog = initCatalog ()

    elif int(inputs[0])==2:
        print("Cargando información de los archivos ....")
        loadData (catalog)
        print ('Libros cargados: ' + str(lt.size(catalog['books'])))
        print ('Autores cargados: ' + str(lt.size(catalog['authors'])))
        print ('Géneros cargados: ' + str(lt.size(catalog['tags'])))

    elif int(inputs[0])==3:
        number = input ("Buscando los TOP ?: ")
        books = controller.getBestBooks (catalog, int(number))
        printBestBooks (books)

    elif int(inputs[0])==4:
        authorname = input("Nombre del autor a buscar: ")
        author = controller.getBooksByAuthor (catalog, authorname)
        printAuthorData (author)


    elif int(inputs[0])==5:
        label = input ("Etiqueta a buscar: ")
        resp = controller.getBooksByTag (catalog, label)
        print ('Se encontraron: ' + str(resp['total_books']) + ' Libros')
        iterator = it.newIterator (resp['books'])
        while it.hasNext (iterator):
            book = it.next (iterator)
            print (book['title'])

    else:
        sys.exit(0)
sys.exit(0)