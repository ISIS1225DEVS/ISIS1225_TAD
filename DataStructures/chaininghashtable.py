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

import random as rd
from DataStructures import mapentry as me
from DataStructures import singlelinkedlist as lt


def newMap( capacity=17, prime=109345121 ):
    scale = rd.randint(1, prime-1) + 1
    shift = rd.randint(1, prime) 
    table = lt.newList()
    for _ in range(capacity):
        bucket = lt.newList()
        lt.addLast (table, bucket)
    hashtable = {'prime': prime, 'capacity': capacity, 'scale':scale, 'shift':shift, 'table':table}
    return hashtable


def hashValue (table, key):
    h = (hash(key))
    value = int ((abs( h*table['scale'] + table['shift']) % table['prime']) % table['capacity'] + 1)
    return value



def contains (map, key, comparefunction):
    hash = hashValue (map, key)
    bucket = lt.getElement (map['table'], hash)
    pos = lt.isPresent (bucket, entry, comparefunction)
    if pos > 0:
        return True
    else: 
        return False


def put (map, key , value, comparefunction):
    hash = hashValue (map, key)
    bucket = lt.getElement (map['table'], hash)
    entry = me.newMapEntry (key, value)
    pos = lt.isPresent (bucket, entry, comparefunction)
    if pos > 0:
        lt.changeInfo (bucket, pos, entry)
    else: 
        lt.addLast ( bucket, entry)



def get (map, key):
    hash = hashValue (map, key)
    bucket = lt.getElement (map['table'], hash)
    pos = lt.isPresent (bucket, entry, comparefunction)
    if pos > 0:
        return lt.getElement (bucket, pos)
    else: 
        return None



def remove (map , key):
    ht.remove (map, key)



def size(map):
    ht.size (map)

def isEmpty(map ):
    return ht.isEmpty (map)

def keySet (map):
    return ht.keySet

def values(map):
    return ht.values (map)
