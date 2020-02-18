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
mecanismo de manejo de colisiones.  No se considera el caso de crecer
el tamaño de la tabla (resizing / rehashing)


Este código está basado en las implementaciones propuestas en:

- Algorithms, 4th Edition.  R. Sedgewick

- Data Structures and Algorithms in Java, 6th Edition.  Michael Goodrich
"""

import random as rd
from DataStructures import mapentry as me
from DataStructures import liststructure as lt


def newMap( capacity, prime):
    """
    Crea una tabla de hash con capacidad igual a capacity (idealment un numero primo).  prime es un número primo utilizado para 
    el cálculo de los codigos de hash, si no es provisto se utiliza el primo 109345121. 
    """
    scale = rd.randint(1, prime-1) + 1
    shift = rd.randint(1, prime) 
    table = lt.newList('ARRAY_LIST')
    for _ in range(capacity):
        entry = me.newMapEntry(None, None)
        lt.addLast (table, entry)
    hashtable = {'prime': prime, 'capacity': capacity, 'scale':scale, 'shift':shift, 'table':table, 'size':0,'type':'PROBING'}
    return hashtable



def put (map, key , value, comparefunction):
    """
    Ingresa una pareja llave,valor a la tabla de hash.  Si la llave ya existe en la tabla, se reemplaza el valor.
    Es necesario proveer una función de comparación para las llaves.
    """
    hash = hashValue (map, key)                            # Se obtiene el hascode de la llave 
    entry = me.newMapEntry (key,value)                  
    pos = findSlot (map, key, hash, comparefunction)       # Se encuentra la posición correspondiente a hash
    lt.changeInfo (map['table'], abs(pos), entry)          # Se reemplaza el valor anterior (puede ser None) con el nuevo valor
    map['size'] += 1




def contains (map, key, comparefunction):
    """
    Retorna True si la llave key se encuentra en la tabla de hash o False en caso contrario.  
    Es necesario proveer la función de comparación entre llaves. 
    """
    hash = hashValue (map, key)
    pos = findSlot (map, key, hash, comparefunction)
    if  (pos > 0):
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
        map['size'] -= 1



def size(map):
    """
    Retornar el numero de entradas presentes en la tabla de hash
    """
    return map['size']



def isEmpty(map ):
    """
    Informa si la tabla de hash se encuentra vacia
    """
    empty = True
    for pos in range(lt.size(map['table'])):
        entry = lt.getElement (map['table'], pos+1)
        if (entry['key']!=None and entry['key']!='__EMPTY__'):
            empty = False
            break
    return empty



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


#__________________________________________________________________
#       Helper Functions
#__________________________________________________________________


def hashValue (table, key):
    """
    Calcula un hash para una llave, utilizando el método MAD : hashValue(y) = ((ay + b) % p) % N.  Donde:
    N es el tamaño de la tabla, p es un primo mayor a N, a y b enteros aleatoreos dentro del intervalo [0,p-1], con a>0  
    """
    h = (hash(key))
    value = int ((abs( h*table['scale'] + table['shift']) % table['prime']) % table['capacity'] + 1)
    return value
    


def findSlot (map, key, hashvalue, comparefunction):
    """
    Encuentra una posición libre en la tabla de hash. 
    map: la tabla de hash
    key: la llave
    hashvalue: La posición inicial de la llave
    comparefunction: funcion de comparación para la búsqueda de la llave
    """
    avail = -1                                             # no se ha encontrado una posición aun
    searchpos = 0                                          #  
    table = map['table']
    while (searchpos!=hashvalue):                          # Se busca una posición hasta llegar al punto de partida
        if (searchpos == 0):   
            searchpos = hashvalue                          # searchpos comienza la búsqueda en la posición hashvalue
        if isAvailable (table, searchpos):                 # La posición esta disponible
            element = lt.getElement(table, searchpos)      
            if (avail == -1 ):
                avail = searchpos                          # avail tiene la primera posición disponible encontrada
            if  element['key']==None:                      # La posición nunca ha sido utilizada, luego el elemento no existe
                break
        else:                                              # la posicion no estaba disponible
            element = lt.getElement(table, searchpos)      
            if comparefunction (key, element['key']):      # La llave es exactamente la que se busca
                return searchpos                           # Se termina la busqueda y se retorna la posicion
        searchpos = (((searchpos) % map['capacity'])+1);   # Se pasa a la siguiente posición de la tabla
    return -(avail)                                        # Se retorna la primera posicion disponible, se indica 
                                                           # con un numero negativo que el elemento no estaba presente 




def isAvailable (table, pos):
    """
    Informa si la posición pos esta disponible en la tabla de hash.  Se entiende que una posición está disponible
    si su contenido es igual a None (no se ha usado esa posicion) o a __EMPTY__ (la posición fue liberada)
    """
    entry = lt.getElement (table, pos)
    if (entry['key'] == None or  entry['key']== '__EMPTY__'):
        return True
    return False