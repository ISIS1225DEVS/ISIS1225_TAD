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
from DataStructures import orderedmapstructure as om 



def newMap ( omaptype='RBT' ):
    """
    Crea una tabla de simbolos ordenada.
    """
    return om.newMap (omaptype)

    

def put (map, key , value, comparefunction):
    """
    Ingresa una pareja llave,valor a la tabla.  Si la llave ya existe, se reemplaza el valor.
    Es necesario proveer una función de comparación para las llaves.
    """
    return om.put (map, key, value, comparefunction)



def get (map, key, comparefunction):
    """
    Retorna la pareja llave, valor, cuya llave sea igual a key.
    Es necesario proveer una función de comparación para las llaves.
    """
    return om.get (map, key, comparefunction)




def remove (map , key, comparefunction):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Es necesario proveer la función de comparación entre llaves 
    """
    om.remove (map, key, comparefunction)



def contains (map, key, comparefunction):
    """
    Retorna True si la llave key se encuentra en la tabla o False en caso contrario.  
    Es necesario proveer la función de comparación entre llaves. 
    """
    return om.contains (map, key, comparefunction)



def size(map):
    """
    Retornar el número de entradas en la tabla
    """
    return om.size (map)



def isEmpty(map ):
    """
    Informa si la tabla  se encuentra vacia
    """
    return om.isEmpty (map)



def keySet (map):
    """
    Retorna una lista con todas las llaves de la tabla 
    """
    return om.keySet (map)



def valueSet(map):
    """
    Retorna una lista con todos los valores de la tabla 
    """
    return om.valueSet (map)


def min (map):
    """
    Retorna la menor llave de la tabla de simbolos 
    """
    return om.min (map)



def max (map):
    """
    Retorna la mayor llave de la tabla de simbolos 
    """
    return om.max (map)



def deleteMin (map):
    """
    Encuentra y remueve la menor  llave de la tabla de simbolos y su valor asociado
    """
    return om.deleteMin (map)



def deleteMax (map):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos y su valor asociado
    """
    return om.deleteMax (map)



def floor (map, key, comparefunction):
    """
    Retorna la llave mas grande en la tabla de simbolos, menor o igual a la llave key 
    """ 
    return om.floor (map, key, comparefunction)




def ceiling (map, key, comparefunction):
    """
    Retorna la llave mas pequeña en la tabla de simbolos, mayor o igual a la llave key 
    """ 
    return om.ceiling (map, key, comparefunction)




def select (map, k):
    """
    Retorna la k-esima llave mas pequeña de la tabla
    """ 
    return om.select (map, k)



def rank (map, key, comparefunction):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    """
    return om.rank (map, key, comparefunction)


def height (map):
    return om.height (map)



