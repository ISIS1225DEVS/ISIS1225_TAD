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
from DataStructures import bstnode as node
from ADT import list as lt


#_____________________________________________________________________
#            API
#_____________________________________________________________________



def newMap ( ) :
    """
    Crea una tabla de simbolos ordenada.
    """
    tree = node.newNode (None,None,0)
    return tree



def put (bst, key , value, comparefunction):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.
    Es necesario proveer una función de comparación para las llaves.
    """

    #El arbol esta vacio y se crea la raiz
    if (bst['key'] == None):
        bst['key'] = key
        bst['value'] = value
        bst['size'] = 1
        return bst

    #La funcion de comparación indica la relación de orden entre las llaves
    cmp = comparefunction (key, bst['key'])
    if (cmp < 0):                                            #La llave a insertar es menor que la raiz
        if (bst['left'] == None):
            bst['left'] = node.newNode (key, value, 1)
        else:
            bst['left'] = put (bst['left'], key, value, comparefunction)
    elif (cmp > 0):                                           #La llave a insertar es mayo que la raiz
        if (bst['right'] == None):
            bst['right'] = node.newNode (key, value, 1)
        else:
            bst['right']  = put (bst['right'], key, value, comparefunction)
    else:                                                      #La llave a insertar es igual que la raiz
        bst['value'] = value
    bst['size'] = 1 + size(bst['left']) + size (bst['right'])
    return bst




def get (bst, key, comparefunction):
    """
    Retorna la pareja lleve-valor con llave igual  a key
    Es necesario proveer una función de comparación para las llaves.
    """
    element = None
    if ( bst['key'] != None):
        cmp = comparefunction (key, bst['key'] )
        if (cmp < 0):
            if (bst['left'] != None):
                element =  get (bst['left'], key, comparefunction)
        elif (cmp > 0):
            if (bst['right'] != None):
                element = get (bst['right'], key, comparefunction)
        else:
            element = bst
    return element




def remove (bst , key, comparefunction):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Es necesario proveer la función de comparación entre llaves
    """
    if (bst == None):
        return None

    cmp = comparefunction (key, bst['key'])

    if (cmp < 0):
        bst['left'] = remove (bst['left'], key, comparefunction)
    elif (cmp > 0):
        bst['right'] = remove (bst['right'], key, comparefunction)
    else:
        if (bst['right']== None):
            return bst['left']
        if (bst['left']  == None):
            bst['right']
        elem = bst
        bst = min(bst['right'])
        bst['right'] = deleteMin(elem['right'])
        bst['left']  = elem['left']

    bst['size'] = 1 + size(bst['left']) + size (bst['right'])
    return bst





def contains (bst, key, comparefunction):
    """
    Retorna True si la llave key se encuentra en la tabla de hash o False en caso contrario.
    Es necesario proveer la función de comparación entre llaves.
    """
    if ( bst['key'] == None):
        return False
    else:
        return (get(bst,key,comparefunction)!= None)





def size(bst):
    """
    Retornar el número de entradas en la tabla de simbolos
    """
    if (bst == None):
        return 0
    else:
        return bst['size']





def isEmpty (bst):
    """
    Informa si la tabla de hash se encuentra vacia
    """
    return (bst['key']== None)




def keySet (bst):
    """
    Retorna una lista con todas las llaves de la tabla de hash
    """
    klist = lt.newList ()
    klist = keySetHelper (bst, klist)
    return klist



def valueSet(bst):
    """
    Retorna una lista con todos los valores de la tabla de hash
    """
    vlist = lt.newList ()
    vlist = valueSetHelper (bst, vlist)
    return vlist




def minKey (bst):
    """
    Retorna la menor llave de la tabla de simbolos
    """
    if (bst['left'] == None):
        return bst
    else:
        return minKey(bst['left'])



def maxKey (bst):
    """
    Retorna la mayor llave de la tabla de simbolos
    """
    if (bst['right'] == None):
        return bst
    else:
        return maxKey(bst['right'])



def deleteMin (bst):
    """
    Encuentra y remueve la menor llave de la tabla de simbolos y su valor asociado
    """
    if (bst['left'] == None):
        bst = bst['right']
        return bst
    else:
        bst['left'] = deleteMin(bst['left'])
    if (bst != None):
        bst['size'] = size(bst['left'] ) + size(bst['right'])  + 1
    return bst




def deleteMax (bst):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos y su valor asociado
    """
    if (bst['right'] == None):
        bst = bst['left']
        return bst
    else:
        bst['right'] = deleteMax(bst['right'])
    if (bst != None):
        bst['size'] = size(bst['left'] ) + size(bst['right'])  + 1
    return bst




def floor (bst, key, comparefunction):
    """
    Retorna la llave mas grande en la tabla de simbolos, menor o igual a la llave key
    """
    if (bst == None):
        return None

    cmp = comparefunction (key, bst['key'])

    if (cmp == 0):
        return bst
    if (cmp <  0):
        return floor (bst['left'], key, comparefunction)
    t = floor(bst['right'], key, comparefunction)
    if (t != None):
        return t
    else:
        return bst




def ceiling (bst, key, comparefunction):
    """
    Retorna la llave mas pequeña en la tabla de simbolos, mayor o igual a la llave key
    """
    if (bst == None):
        return None

    cmp = comparefunction (key, bst['key'])

    if (cmp == 0):
        return bst
    if (cmp <  0):
        t = ceiling (bst['left'], key, comparefunction)
        if (t != None):
            return t
        else:
            return bst
    return ceiling (bst['right'], key, comparefunction)




def select (bst, k):
    """
    Retorna la k-esima llave mas pequeña de la tabla
    """

    if (bst == None):
        return None

    t = 0
    if bst['left'] != None:
        t = bst['left']['size']

    if  (t > k):
        return select(bst['left'], k)
    elif (t < k):
        return select(bst['right'], k-t-1)
    else:
        return bst




def rank (bst, key, comparefunction):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    """
    if (bst == None):
        return 0

    cmp = comparefunction (key, bst['key'])

    if  (cmp < 0):
        return rank (bst['left'], key, comparefunction)
    elif (cmp > 0):
        return 1 + size(bst['left']) + rank(bst['right'], key, comparefunction)
    else:
        return size(bst['left'])


def height (bst):
    if (bst == None):
        return -1
    else:
        return 1  +  max (height (bst['left']),  height (bst['right']))


def keys(root, keylo, keyhi, comparefunction):
    pass


def valueRange(root, keylo, keyhi, comparefunction):
    pass

#_____________________________________________________________________
#            Funciones Helper
#_____________________________________________________________________




def valueSetHelper (bst, klist):
    if (bst == None):
        return klist
    valueSetHelper (bst['left'], klist)
    lt.addLast (klist, bst['value'])
    valueSetHelper (bst['right'], klist)
    return klist





def keySetHelper (bst, klist):
    if (bst == None):
        return klist
    keySetHelper (bst['left'], klist)
    lt.addLast (klist, bst['key'])
    keySetHelper (bst['right'], klist)
    return klist
