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
import csv
from ADT import list as lt
from DataStructures import listiterator as it
import controller 

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
    print("3- Infracciones en una fecha específica")
    print("4- Infracciones en un rango de fechas")
    print("5- Infracción mas frecuente")
    print("6- Zona geográfica con más infraccioes")
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




"""
Menu principal
"""
while True:
    printMenu()
    inputs =input('Seleccione una opción para continuar\n')
    if int(inputs[0])==1:
        print("Inicializar sistema de analisis....")
        catalog = initCatalog ()

    elif int(inputs[0])==2:
        print("Cargando información de los archivos ....")
        loadData (catalog)
        altura = controller.mapHeight(catalog)
        elems = controller.numAccidents(catalog)
        print ('Elementos cargados: ' + str (elems))
        print ('Altura del arbol: ' + str(altura))


    elif int(inputs[0])==3:
        number = input ("Infracciones por fecha: ")
    #   books = controller.getBestBooks (catalog, int(number))

    elif int(inputs[0])==4:
        authorname = input("Infracciones por rango de fechas: ")
    #    author = controller.getBooksByAuthor (catalog, authorname)


    elif int(inputs[0])==5:
        label = input ("Infracción mas frecuente: ")
    #    resp = controller.getBooksByTag (catalog, label)


    elif int(inputs[0])==6:
        label = input ("Zona geográfica mas accidentada: ")
    #    resp = controller.getBooksByTag (catalog, label)


    else:
        sys.exit(0)
sys.exit(0)