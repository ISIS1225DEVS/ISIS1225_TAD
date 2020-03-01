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
from ADT import map as map

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
    loadAccidents(catalog)



#___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
#___________________________________________________


def loadAccidents (catalog):
    """
    """
    #booksfile = cf.data_dir + 'USAccidents/us_accidents_small.csv'
    booksfile = cf.data_dir + 'USAccidents/us_accidents_2016.csv'
    #booksfile = cf.data_dir + 'USAccidents/US_Accidents_Dec19.csv'
    input_file = csv.DictReader(open(booksfile))
    for info in input_file:  
        accident = model.newAccident (info)
        model.addAccident (catalog, accident) 
        model.indexAccidentById (catalog, accident, idFunction)
    

#___________________________________________________
#  Funciones para consultas
#___________________________________________________




#___________________________________________________
#  Funciones Helper para comparación de Elementos
#___________________________________________________


def idFunction (key1, key2):
    if ( key1 == key2):
        return 0
    elif (key1 < key2):
        return -1
    else:
        return 1



def mapHeight(map):
    return model.mapHeight (map)


def numAccidents(catalog):
    return model.numAccidents(catalog)
