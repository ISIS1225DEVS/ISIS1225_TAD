"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Dario Correal
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
from DataStructures import listnode as node 

"""
  Este módulo implementa una estructura de datos lineal, como una lista encadenada sencillamente 
  para almacenar una colección de elementos.
"""


def newList ():
    """
    Crea una lista vacia
    """
    new_list = {'first':None, 'last':None, 'size':0 }
    return (new_list)


def addFirst(lst, element):
    """
    Agrega un elemento en la primera posición de la lista
    """
    new_node = node.newSingleNode (element)
    new_node ['next'] = lst['first']
    lst['first'] = new_node
    if (lst['size'] == 0):
        lst ['last'] = lst['first']
    lst['size'] += 1



def addLast(lst, element):
    """
    Agrega un elemento en la última posición de la lista.

    lst: La lista en la que se inserta el elemento
    element: El elemento a insertar
    """
    new_node = node.newSingleNode (element)

    if lst['size'] == 0:
        lst['first'] = new_node
    else:
        lst['last']['next'] = new_node
    lst['last']= new_node
    lst['size'] += 1


def isEmpty (lst):
    """
    Indica si la lista está vacía
    """
    return lst['size'] == 0


def size(lst):
    """
    Informa el número de elementos de la lista
    """
    return lst['size'] 


def firstElement (lst):
    """
    Retorna el primer elemento de la lista, sin eliminarlo.
    """
    return lst['first']['info']



def lastElement (lst):
    """
    Retorna el último elemento de la lista, sin eliminarlo.
    """
    return lst['last']['info']



def getElement (lst, pos):
    """
    Retorna el elemento en la posición pos de la lista.
    pos debe ser mayor que cero y menor o igual al tamaño de la lista
    la lista no esta vacia
    """
    searchpos = 1
    node = lst['first']
    while searchpos < pos:
        searchpos+=1
        node = node['next']
    return node['info']  


def removeFirst (lst):
    """
    Remueve el primer elemento de la lista y lo retorna en caso de existir, de lo contrario retorna None
    """
    if lst['first'] != None:
        temp = lst['first']['next']
        node = lst['first'] 
        lst['first'] = temp
        lst['size'] -= 1
        return node['info']
    else:
        return None

def removeLast (lst):
    """
    Remueve el último elemento de la lista y lo retorna en caso de existir, de lo contrario retorna None
    """
    if lst['size'] != 0:
        if lst['first'] == lst['last']:
            node = lst['first'] 
            lst['last'] = None
            lst['first'] = None
        else:
            temp = lst['first']    
            while temp['next'] != lst['last']:
                temp = temp['next']
            node = lst['last']
            lst['last'] = temp
            lst['last']['next'] = None
        lst['size'] -= 1
        return node['info']
    else:
        return None

def insertElement (lst, element, pos):
    """
    Inserta el elemento element en la posición pos de la lista. 

    lst: La lista en la que se va a insertar el elemento
    element: El elemento a insertar
    pos: posición en la que se va a insertar el elemento,  0 < pos <= size(lst) 
    """
    new_node = node.newSingleNode (element)

    if (pos == 1):
        new_node['next'] = lst['first']
        lst['first'] = new_node
    else:
        cont = 1
        prev = lst['first']
        current  = lst['first']
        while cont < pos:
            prev = current
            current = current['next']
            cont += 1
        new_node['next'] = current
        prev['next'] = new_node
    lst['size'] += 1
        
