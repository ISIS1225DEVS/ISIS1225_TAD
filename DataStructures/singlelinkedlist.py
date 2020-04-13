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
from DataStructures import listnode as node 

"""
  Este módulo implementa una estructura de datos lineal, como una lista encadenada sencillamente 
  para almacenar una colección de elementos.
"""


def newList ():
    """
    Crea una lista vacia
    """
    new_list = {'first':None, 'last':None, 'size':0, 'type':'SINGLE_LINKED' }
    return new_list


def addFirst(lst, element):
    """
    Agrega un elemento en la primera posición de la lista
    """
    try:
        new_node = node.newSingleNode (element)
        new_node ['next'] = lst['first']
        lst['first'] = new_node
        if (lst['size'] == 0):
            lst ['last'] = lst['first']
        lst['size'] += 1
        return lst
    except Exception as e:
        return None



def addLast(lst, element):
    """
    Agrega un elemento en la última posición de la lista.

    lst: La lista en la que se inserta el elemento
    element: El elemento a insertar
    """
    try: 
        new_node = node.newSingleNode (element)

        if lst['size'] == 0:
            lst['first'] = new_node
        else:
            lst['last']['next'] = new_node
        lst['last']= new_node
        lst['size'] += 1
        return lst
    except Exception as e:
        return None




def isEmpty (lst):
    """
    Indica si la lista está vacía
    """
    try:
        return lst['size'] == 0
    except:
        return None


def size(lst):
    """
    Informa el número de elementos de la lista
    """
    try:
        return lst['size'] 
    except:
        return None


def firstElement (lst):
    """
    Retorna el primer elemento de la lista, sin eliminarlo.
    """
    try:
        if 'info' in lst['first']: 
            return lst['first']['info']
    except:
        return None



def lastElement (lst):
    """
    Retorna el último elemento de la lista, sin eliminarlo.
    """
    try:
        if 'info' in lst['last']:
            return lst['last']['info']
    except Exception as e:
        return None



def getElement (lst, pos):
    """
    Retorna el elemento en la posición pos de la lista.
    pos debe ser mayor que cero y menor o igual al tamaño de la lista
    la lista no esta vacia
    """
    try:
        searchpos = 1
        node = lst['first']
        while searchpos < pos:
            searchpos+=1
            node = node['next']
        return node['info']
    except Exception as e:
        return None  


def deleteElement (lst, pos):
    """
    Elimina el elemento en la posición pos de la lista.
    pos debe ser mayor que cero y menor o igual al tamaño de la lista
    la lista no esta vacia
    """
    try:
        node = lst['first']
        prev = lst['first']
        searchpos = 1
        if (pos == 1):
            lst['first'] = lst['first']['next']
        elif(pos > 1):
            while searchpos < pos:
                searchpos+=1
                prev = node
                node = node['next']
            prev['next'] = node['next']
        lst['size'] -= 1
        return lst
    except Exception as e:
        return None



def removeFirst (lst):
    """
    Remueve el primer elemento de la lista y lo retorna en caso de existir, de lo contrario retorna None
    """
    try:
        if lst['first'] != None:
            temp = lst['first']['next']
            node = lst['first'] 
            lst['first'] = temp
            lst['size'] -= 1
            if (lst['size'] == 0):
                lst['last'] = lst['first']
            return node['info']
        else:
            return None
    except Exception as e:
        return None



def removeLast (lst):
    """
    Remueve el último elemento de la lista y lo retorna en caso de existir, de lo contrario retorna None
    """
    try:
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
    except Exception as e:
        return None




def insertElement (lst, element, pos):
    """
    Inserta el elemento element en la posición pos de la lista. 

    lst: La lista en la que se va a insertar el elemento
    element: El elemento a insertar
    pos: posición en la que se va a insertar el elemento,  0 < pos <= size(lst) 
    """
    try:
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
        return lst
    except Exception as e:
        return None


def isPresent (lst, element, comparefunction):
    """
    Informa si el elemento element esta presente en la lista. Si esta presente retorna 
    la posición en la que se encuentra o cero (0) si no esta presente
    """
    try:
        size = lst ['size']
        if size > 0:
            node = lst['first']
            keyexist = False
            for keypos in range (1,size+1):
                if (comparefunction (element, node['info'] )):
                    keyexist = True
                    break
                node = node['next']
            if keyexist:
                return keypos
        return 0        
    except Exception as e:
        return None


def changeInfo (lst, pos, newinfo):
    """
    Cambia la informacion contenida en el nodo de la lista en la posicion pos
    """
    try:
        current  = lst['first']
        cont = 1
        while cont < pos:
            current = current['next']
            cont += 1
        current['info'] = newinfo
        return lst
    except Exception as e:
        return None
    

def exchange (lst, pos1, pos2):
    """
    Intercambia la informacion en las posiciones pos1 y pos2 de la lista
    """
    try:
        infopos1 = getElement (lst, pos1)
        infopos2 = getElement (lst, pos2)
        changeInfo (lst, pos1, infopos2)
        changeInfo (lst, pos2, infopos1)
        return lst
    except Exception as e:
        return None



def subList (lst, pos, numelem):
    """
    Retorna una sublista de la lista lst, partiendo de la posicion pos, con una longitud de numelem elementos
    """
    try:
        sublst = {'first':None, 'last':None, 'size':0, 'type':'SINGLE_LINKED_LIST' }
        cont = 1
        loc = pos
        while  cont <= numelem:
            elem = getElement (lst, loc)
            addLast (sublst, elem)
            loc += 1
            cont += 1
        return sublst
    except Exception as e:
        return None

