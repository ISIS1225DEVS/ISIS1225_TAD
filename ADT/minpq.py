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
from DataStructures import heap as h



def newMinPQ (size, cmpfunction):
    """
    Crea un cola de prioridad orientada a menor
    """
    pq = {'heap': None}
    pq['heap'] = h.newHeap(size,cmpfunction)
    return pq



def size (minpq):
    """
    Retorna el número de elementos en el heap
    """
    return (h.size(minpq['heap']))


def isEmpty (minpq):
    """
    Indica si el heap está vacío
    """
    return (h.isEmpty(minpq['heap']))



def min (minpq):
    """
    Retorna el primer elemento del heap, es decir el menor elemento
    """
    return h.min (minpq['heap'])



def insert  (minpq, key, index):
    """
    Guarda el elemento 'element' en el heap. Lo guarda en la última posición y luego hace swim del elemento
    """
    return h.insert (minpq['heap'], key, index)



def delMin (minpq):
    """
    Retorna el menor elemento del heap y lo elimina. Se reemplaza con el último elemento y se hace sink.
    """
    return (h.delMin(minpq['heap']))

