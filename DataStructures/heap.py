"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
from DataStructures import liststructure as lt
from DataStructures import mapentry as me
from ADT import map as m



def newHeap (size, cmpfunction):
    """
    Crea un nuevo heap basado en un arreglo, cuyo primer elemento es inicializado en None y no será utilizado
    """
    heap = {'elements':None, 
            'indexelems': None,
            'size':0, 
            'offset':2,
            'comparefunction':cmpfunction
            }

    heap['elements'] = lt.newList (datastructure='ARRAY_LIST')
    lt.addLast (heap['elements'], None)
    heap['indexelems'] = m.newMap (numelements=size,maptype='PROBING',comparefunction=cmpfunction)
    return heap



def size (heap):
    """
    Retorna el número de elementos en el heap
    """
    return (heap['size'])



def isEmpty (heap):
    """
    Indica si el heap está vacío
    """
    return (heap['size'] == 0)



def min (heap):
    """
    Retorna el primer elemento del heap, es decir el menor elemento
    """
    if not lt.isEmpty (heap['elements']):
        return lt.getElement (heap['elements'], heap['offset'])
    return None



def insert  (heap, key, index):
    """
    Guarda el elemento 'element' en el heap. Lo guarda en la última posición y luego hace swim del elemento
    """
    node = me.newMapEntry (key, index)
    lt.insertElement (heap['elements'], node, heap['size']+heap['offset'])
    m.put (heap['indexelems'],key, heap['size']+heap['offset'])
    heap['size'] += 1
    swim (heap, heap['size'])




def delMin (heap):
    """
    Retorna el menor elemento del heap y lo elimina. Se reemplaza con el último elemento y se hace sink.
    """
    if (heap['size']>0):
        min = lt.getElement  (heap['elements'], heap['offset'])
        last = lt.getElement  (heap['elements'], heap['size']+1)
        lt.changeInfo (heap['elements'], heap['offset'],last)
        lt.changeInfo (heap['elements'], heap['size']+1,None)
        m.remove (heap['indexelems'],min['key'])
        heap ['size'] -= 1
        sink (heap, 1)
        return min
    return None



def indexOf (heap, key):
    element = m.get (heap['indexelems'],key)
    if element:
        return element ['value']
    return None



def changeIndex (heap, key, index):
    newnode = me.newMapEntry (key, index)
    elem = m.get (heap['indexelems'],key)
    pos = elem['value']
    lt.changeInfo (heap['elements'],pos,newnode)
    swim (heap, pos-1)
    sink (heap, pos-1)
    return heap


def contains (heap, key):
    return (lt.isPresent (heap['elements'], key, heap['comparefunction']) > 0)


"""
Funciones helper para garantizar las propiedades del heap
"""


def swim (heap, pos):
    """
    Ubica en el lugar indicado un elemento adicionado en la última posición
    """
    while (pos > 1):
        parent = lt.getElement (heap['elements'], int((pos/2)+1))
        element = lt.getElement (heap['elements'], int (pos+1))
        if greater ( parent, element):
            exchange(heap, pos+1, int(pos/2 +1))
        pos = pos//2




def sink (heap, pos):
    """
    Ubica en la posición correcta un elemento ubicado en la raíz del heap
    """
    size = heap['size']
    while ( (2*pos <= size)):
        j = 2*pos
        if (j < size):
            if greater(lt.getElement(heap['elements'],j+1), lt.getElement(heap['elements'],(j+1)+1)): 
                j+=1
        if (not greater(lt.getElement(heap['elements'], pos+1), lt.getElement(heap['elements'],j+1))):
            break
        exchange(heap, pos+1, j+1)
        pos = j





def greater (element1, element2):
    """
    Indica si el elemento 1 es mayor que el elemento 2
    """
    return (element1['value'] > element2['value'])



def exchange (heap, posa, posb):
    """
    Intercambia los elementos en las posiciones posa y posb del heap
    """
    elema = lt.getElement (heap['elements'], posa)
    elemb = lt.getElement (heap['elements'], posb)
    lt.exchange (heap['elements'], posa, posb) 
    m.put (heap['indexelems'], elema['key'], posb)
    m.put (heap['indexelems'], elemb['key'], posa)