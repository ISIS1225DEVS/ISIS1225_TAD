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



def newHeap ():
    """
    Crea un nuevo heap basado en un arreglo, cuyo primer elemento es inicializado en None y no será utilizado
    """
    heap = {'elements':None, 'size':0, 'offset':2}
    heap['elements'] = lt.newList (datastructure='ARRAY_LIST')
    lt.addLast (heap['elements'], None)
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



def insert  (heap, element):
    """
    Guarda el elemento 'element' en el heap. Lo guarda en la última posición y luego hace swim del elemento
    """
    lt.insertElement (heap['elements'], element, heap['size']+heap['offset'])
    heap['size'] += 1
    swim (heap)




def delMin (heap):
    """
    Retorna el menor elemento del heap y lo elimina. Se reemplaza con el último elemento y se hace sink.
    """
    if (heap['size']>0):
        min = lt.getElement  (heap['elements'], heap['offset'])
        last = lt.getElement  (heap['elements'], heap['size']+1)
        lt.changeInfo (heap['elements'], heap['offset'],last)
        lt.changeInfo (heap['elements'], heap['size']+1,None)
        heap ['size'] -= 1
        sink (heap)
        return min
    return None



"""
Funciones helper para garantizar las propiedades del heap
"""


def swim (heap):
    """
    Garantiza que no hay elementos menores después de elementos mas grandes
    """
    pos = heap['size']

    while (pos > 1):
        parent = lt.getElement (heap['elements'], int((pos/2)+1))
        element = lt.getElement (heap['elements'], int (pos+1))
        if greater ( parent, element):
            exchange(heap, pos+1, int(pos/2 +1))
        pos = pos//2



def sink (heap):
    """
    Garantiza que no hay elementos mayores antes que elementos menores
    """
    root = lt.getElement (heap['elements'], heap['offset'])
    size = heap['size']
    pos = 1

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
    return (element1 > element2)



def exchange (heap, posa, posb):
    """
    Intercambia los elementos en las posiciones posa y posb del heap
    """
    lt.exchange (heap['elements'], posa, posb) 