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

"""

Implementación de una tabla de hash, utilizando linear probing como 
mecanismo de manejo de colisiones.

"""

import random as rd
from DataStructures import mapentry as me
from DataStructures import singlelinkedlist as lt


def newMap( capacity=17, prime=109345121 ):
    """
    Crea una tabla de hash con capacidad igual a capacity.  
    """
    scale = rd.randint(1, prime-1) + 1
    shift = rd.randint(1, prime) 
    table = lt.newList()
    for _ in range(capacity):
        entry = me.newMapEntry(None, None)
        lt.addLast (table, entry)
    hashtable = {'prime': prime, 'capacity': capacity, 'scale':scale, 'shift':shift, 'table':table}
    return hashtable


def hashValue (table, key):
    """
    Calcula un hash para una llave, utilizando el método MAD : hashValue(y) = ((ay + b) % p) % N.  Donde:
    N es el tamaño de la tabla, p es un primo mayor a N, a y b enteros aleatoreos dentro del intervalo [0,p-1], con a>0  
    """
    #h = (hash(key))
    #value = int ((abs( h*table['scale'] + table['shift']) % table['prime']) % table['capacity'] + 1)
    #return value
    return (int (key) % table['capacity']+1)
    

def isAvailable (lst, pos):
    entry = lt.getElement (lst, pos)
    if (entry['key'] == None or  entry['key']== '__EMPTY__'):
        return True
    return False



def findSlot (map, key, hashvalue, comparefunction):
    avail = -1
    searchpos = 0
    lst = map['table']
    while (searchpos!=hashvalue):
        if (searchpos == 0):
            searchpos = hashvalue
        if isAvailable (lst, searchpos):
            element = lt.getElement(lst, searchpos)
            if (avail == -1 ):
                avail = searchpos
            if  element['key']==None:
                break
        else:
            element = lt.getElement(lst, searchpos)
            if comparefunction (key, element['key']):
                return searchpos
        searchpos = (((searchpos) % map['capacity'])+1);  
    return -(avail)


def put (map, key , value, comparefunction):
    """
    Ingresa una pareja llave,valor a la tabla de hash.  Si la llave ya existe en la tabla, se reemplaza el valor.
    Es necesario proveer una función de comparación para las llaves.
    """
    hash = hashValue (map, key)
    entry = me.newMapEntry (key,value)
    pos = findSlot (map, key, hash, comparefunction)
    lt.changeInfo (map['table'], abs(pos), entry) 



def contains (map, key, comparefunction):
    """
    Retorna True si la llave key se encuentra en la tabla de hash o False en caso contrario.  
    Es necesario proveer la función de comparación entre llaves. 
    """
    hash = hashValue (map, key)
    pos = findSlot (map, key, hash, comparefunction)
    if pos > 0:
        return True
    else: 
        return False


def get (map, key, comparefunction):
    """
    Retorna la pareja llave, valor, cuya llave sea igual a key.
    Es necesario proveer una función de comparación para las llaves.
    """
    hash = hashValue (map, key)
    pos = findSlot (map, key, hash, comparefunction)
    if pos > 0:
        element = lt.getElement( map['table'], pos)
        return element
    else: 
        return None



def remove (map , key, comparefunction):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Es necesario proveer la función de comparación entre llaves 
    """
    hash = hashValue (map, key)
    pos = findSlot (map, key, hash, comparefunction)
    if pos > 0:
        entry = me.newMapEntry ('__EMPTY__','__EMPTY__')
        lt.changeInfo (map['table'], pos, entry) 


def size(map):
    """
    Retornar el tamaño de la tabla de hash
    """
    return lt.size (map['table'])


def isEmpty(map ):
    """
    Informa si la tabla de hash se encuentra vacia
    """
    return lt.isEmpty (map['table'])



def keySet (map):
    """
    Retorna una lista con todas las llaves de la tabla de hash
    """
    ltset = lt.newList()
    for pos in range(lt.size(map['table'])):
        entry = lt.getElement (map['table'], pos+1)
        if (entry['key']!=None and entry['key']!='__EMPTY__'):
            lt.addLast (ltset, entry['key'])
    return ltset


def valueSet(map):
    """
    Retornar una lista con todos los valores de la tabla de hash
    """
    ltset = lt.newList()
    for pos in range(lt.size(map['table'])):
        entry = lt.getElement (map['table'], pos+1)
        if (entry['value']!=None and  entry['value']!='__EMPTY__'):
            lt.addLast (ltset, entry['value'])
    return ltset
