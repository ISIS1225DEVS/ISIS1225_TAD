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

Implementación de una tabla de hash, utilizando Separate Chaining como 
mecanismo de manejo de colisiones.  Esta implementación crea una lista
de tamaño capacity.  En cada posición de la lista, se crea una lista
vacia.

Este código está basado en las implementaciones propuestas en:

- Algorithms, 4th Edition.  R. Sedgewick

- Data Structures and Algorithms in Java, 6th Edition.  Michael Goodrich

"""

import random as rd
from DataStructures import mapentry as me
from DataStructures import liststructure as lt



def newMap( capacity, prime ):
    """
    Crea una tabla de hash con capacidad igual a capacity (idealmente un numero primo).  prime es un número primo utilizado para 
    el calculo de los codigos de hash, si no es provisto se utiliza el primo 109345121. Bucket representa 
    la lista de parejas llave,valor a guardar en cada posición de la tabla de hash.
    """
    scale = rd.randint(1, prime-1) + 1
    shift = rd.randint(1, prime) 
    table = lt.newList('ARRAY_LIST')
    for _ in range(capacity):
        bucket = lt.newList()
        lt.addLast (table, bucket)
    hashtable = {'prime': prime, 'capacity': capacity, 'scale':scale, 'shift':shift, 'table':table, 'size':0,'type':'CHAINING'}
    return hashtable




def contains (map, key, comparefunction):
    """
    Retorna True si la llave key se encuentra en la tabla de hash o False en caso contrario.  
    Es necesario proveer la función de comparación entre llaves. 
    """
    hash = hashValue (map, key)
    bucket = lt.getElement (map['table'], hash)
    pos = lt.isPresent (bucket, key, comparefunction)
    if pos > 0:
        return True
    else: 
        return False




def put (map, key , value, comparefunction):
    """
    Ingresa una pareja llave,valor a la tabla de hash.  Si la llave ya existe en la tabla, se reemplaza el valor.
    Es necesario proveer una función de comparación para las llaves.
    """
    hash = hashValue (map, key)
    bucket = lt.getElement (map['table'], hash)          #Se obtiene la lista de elementos en la posicion  hash de la tabla
    entry = me.newMapEntry (key, value)
    pos = lt.isPresent (bucket, key, comparefunction)  
    if pos > 0:                                          #La pareja ya exista, se reemplaza el valor con la nueva información
        lt.changeInfo (bucket, pos, entry)
    else: 
        lt.addLast ( bucket, entry)                      #La llave no existia, se crea una nueva entrada
        map['size'] += 1                     



def get (map, key, comparefunction):
    """
    Retorna la pareja llave, valor, cuya llave sea igual a key.
    Es necesario proveer una función de comparación para las llaves.
    Si la llave no esta presente se retorna None
    """
    hash = hashValue (map, key)
    bucket = lt.getElement (map['table'], hash)
    pos = lt.isPresent (bucket, key, comparefunction)
    if pos > 0:
        return lt.getElement (bucket, pos)
    else: 
        return None



def remove (map , key, comparefunction):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Es necesario proveer la función de comparación entre llaves 
    """
    hash = hashValue (map, key)
    bucket = lt.getElement (map['table'], hash)
    pos = lt.isPresent (bucket, key, comparefunction)
    if pos > 0:
        lt.deleteElement (bucket, pos)
        map['size'] -= 1  
    else: 
        return None


def size(map):
    """
    Retornar el número de elementos presentes en la tabla de hash
    """
    return map['size']



def isEmpty(map ):
    """
    Informa si la tabla de hash se encuentra vacia
    """
    bucket = lt.newList()
    empty = True
    for pos in range(lt.size(map['table'])):
        bucket = lt.getElement (map['table'], pos+1)
        if lt.isEmpty(bucket)== False:
            empty = False
            break
    return empty



def keySet (map):
    """
    Retorna una lista con todas las llaves de la tabla de hash
    """
    ltset = lt.newList()
    for pos in range(lt.size(map['table'])):
        bucket = lt.getElement (map['table'], pos+1)
        for element in range (lt.size(bucket)):
           entry = lt.getElement (bucket, element+1)
           lt.addLast (ltset, entry['key'])
    return ltset



def valueSet(map):
    """
    Retornar una lista con todos los valores de la tabla de hash
    """
    ltset = lt.newList()
    for pos in range(lt.size(map['table'])):
        bucket = lt.getElement (map['table'], pos+1)
        for element in range (lt.size(bucket)):
           entry = lt.getElement (bucket, element+1)
           lt.addLast (ltset, entry['value'])
    return ltset



#__________________________________________________________________
#       Helper Functions
#__________________________________________________________________



def hashValue (table, key):
    """
    Calcula un hash para una llave, utilizando el método MAD : hashValue(y) = ((ay + b) % p) % N.  Donde:
    N es el tamaño de la tabla, p es un primo mayor a N, a y b enteros aleatoreos dentro del intervalo [0,p-1], con a>0  
    """
    h = hash(key)
    value = int ((abs( h*table['scale'] + table['shift']) % table['prime']) % table['capacity'] + 1)
    return value


