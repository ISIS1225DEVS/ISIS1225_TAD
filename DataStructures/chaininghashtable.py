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


def newMap( capacity ) :
     return ht.newMap ()

def put (map, key , value):
    ht.put (map, key, value)

def get (map, key):
    return ht.get (map, key)

def remove (map , key):
    ht.remove (map, key)

def contains (map, key):
    ht.contains (map, key)

def size(map):
    ht.size (map)

def isEmpty(map ):
    return ht.isEmpty (map)

def keySet (map):
    return ht.keySet

def values(map):
    return ht.values (map)
