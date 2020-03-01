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
from ADT import orderedmap as map
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá  una lista para los libros, 
Los autores y los generos se guardaran en 
tablas de simbolos
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar todos los libros,
    Adicionalmente, crea una lista vacia para los autores y una lista vacia para los 
    generos.   Retorna el catalogo inicializado.
    """
    catalog = {'accidents':None, 'idIndex':None}
    catalog['accidents'] = lt.newList()
    catalog['idIndex'] = map.newMap ()
    return catalog


def newAccident (info):
    """
    """
    accident = info
    return accident



def addAccident (catalog, accident):
    lt.addLast(catalog['accidents'],accident)


def indexAccidentById (catalog, accident, indexfunctionn):
    catalog['idIndex']=map.put (catalog['idIndex'], accident['ID'],accident, indexfunctionn)





# Funciones de consulta


def compareBookIds (id1, id2):
    return (id1  == id2)


def mapHeight (catalog):
    omap = catalog['idIndex']
    return map.height (omap)

def numAccidents (catalog):
    return lt.size(catalog['accidents'])