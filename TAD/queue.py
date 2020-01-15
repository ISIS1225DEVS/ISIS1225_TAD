"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Dario Correal
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

from DataStructures import singlelinkedlist as lt

"""
  Este módulo implementa el tipo abstracto de datos cola (Queue) sobre una lista.
"""

def newQueue():
    """
    Crea una cola vacia
    """
    return lt.newList()

def enqueue (queue, element):
    """
    Agrega el elemento element en el tope de la pila
    """
    lt.addLast (queue, element)

def dequeue (queue):
    """
    Retorna el elemento en la primer posición de la cola, y lo elimina
    """
    lt.removeFirst(queue, element)

def peek (queue):
    """
    Retorna el elemento en la primer posición de la cola sin eliminarlo
    """
    lt.firstElement (queue)

def isEmpty (queue):
    """
    Informa si la cola es vacía o no 
    """
    return lt.isEmpty(queue)

def size (queue):
    """
    Informa el número de elementos en la cola
    """
    return lt.size(queue)

def newIterator(queue):
    """
    Inicializa un iterador para la lista
    """
    lt.newIterator(queue)


def hasNext(queue):
    """
    Informa si existe un nodo en la siguiente posicion de la lista, a partir de la posicion actual del iterador
    """
    return lt.hasNext (queue)


def next(queue):
    """
    Retorna el elemento en la posición siguiente a la indicada por el iterador
    """
    return lt.next (queue)
