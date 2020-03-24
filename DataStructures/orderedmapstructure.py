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
from DataStructures import bst as bst
from DataStructures import rbt as rbt



def newMap( omaptype ) :
    """
    Crea un map (tabla de símbolos) ordenado.
    """
    if (omaptype == 'BST'):
        return bst.newMap ( )
    else:
        return rbt.newMap ( )



def put (map, key , value, comparefunction):
    """
    Ingresa una pareja llave,valor a la tabla.  Si la llave ya existe, se reemplaza el valor.
    Es necesario proveer una función de comparación para las llaves.
    """
    if (map['type'] == 'BST'):
        return bst.put (map, key, value, comparefunction)
    else:
        return rbt.put (map, key, value, comparefunction)



def get (map, key, comparefunction):
    """
    Retorna la pareja llave, valor, cuya llave sea igual a key.
    Es necesario proveer una función de comparación para las llaves.
    """
    elem = None
    if (map['type']=='BST'):
        elem = bst.get (map, key, comparefunction)
    else:
        elem = rbt.get (map, key, comparefunction)
    if elem:
        return elem['value']
    return None




def remove (map , key, comparefunction):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Es necesario proveer la función de comparación entre llaves
    """
    if (map['type']=='BST'):
        bst.remove (map, key, comparefunction)
    else:
        rbt.remove (map, key, comparefunction)



def contains (map, key, comparefunction):
    """
    Retorna True si la llave key se encuentra en la tabla  o False en caso contrario.
    Es necesario proveer la función de comparación entre llaves.
    """
    if (map['type']=='BST'):
        return bst.contains (map, key, comparefunction)
    else:
        return rbt.contains (map, key, comparefunction)



def size(map):
    """
    Retornar el número de entradas en la tabla
    """
    if (map['type']=='BST'):
        return bst.size (map)
    else:
        return rbt.size (map)


def isEmpty(map ):
    """
    Informa si la tabla  se encuentra vacia
    """
    if (map['type']=='BST'):
        return bst.isEmpty (map)
    else:
        return rbt.isEmpty (map)



def keySet (map):
    """
    Retorna una lista con todas las llaves de la tabla
    """
    if (map['type']=='BST'):
        return bst.keySet (map)
    else:
        return rbt.keySet (map)



def valueSet(map):
    """
    Retorna una lista con todos los valores de la tabla
    """
    if (map['type']=='BST'):
        return bst.valueSet (map)
    else:
        return rbt.valueSet (map)



def min (map):
    """
    Retorna la menor llave de la tabla de simbolos
    """
    if (map['type']=='BST'):
        return bst.minKey (map)
    else:
        return rbt.minKey (map)



def max (map):
    """
    Retorna la mayor llave de la tabla de simbolos
    """
    if (map['type']=='BST'):
        return bst.maxKey (map)
    else:
        return rbt.maxKey (map)



def deleteMin (map):
    """
    Encuentra y remueve la menor llave de la tabla de simbolos y su valor asociado
    """
    if (map['type']=='BST'):
        return bst.deleteMin (map)
    else:
        return rbt.deleteMin (map)




def deleteMax (map):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos y su valor asociado
    """
    if (map['type']=='BST'):
        return bst.deleteMax (map)
    else:
        return rbt.deleteMax (map)




def floor (map, key, comparefunction):
    """
    Retorna la llave mas grande en la tabla de simbolos, menor o igual a la llave key
    """
    if (map['type']=='BST'):
        return bst.floor (map, key, comparefunction)
    else:
        return rbt.floor (map, key, comparefunction)




def ceiling (map, key, comparefunction):
    """
    Retorna la llave mas pequeña en la tabla de simbolos, mayor o igual a la llave key
    """
    if (map['type']=='BST'):
        return bst.ceiling (map, key, comparefunction)
    else:
        return rbt.ceiling (map, key, comparefunction)




def select (map, k):
    """
    Retorna la k-esima llave mas pequeña de la tabla
    """
    if (map['type']=='BST'):
        return bst.select (map, k)
    else:
        return rbt.select (map, k)




def rank (map, key, comparefunction):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    """
    if (map['type']=='BST'):
        return bst.rank (map, key, comparefunction)
    else:
        return rbt.rank (map, key, comparefunction)


def keys (map, keylo, keyhi, comparefunction):
    """
    Retorna todas las llaves encontradas en el rango dado por keylo y keyhi
    """        
    if (map['type']=='BST'):
        return bst.keys (map, keylo, keyhi, comparefunction)
    else:
        return rbt.keys (map, keylo, keyhi, comparefunction)


def height (map):
    if (map['type']=='BST'):
        return bst.height (map)
    else:
        return rbt.height (map)

        
def valueRange(map, keylo, keyhi, comparefunction):
    if (map['type']=='BST'):
        return bst.valueRange(map, keylo, keyhi, comparefunction)
    else:
        return rbt.valueRange(map, keylo, keyhi, comparefunction)
