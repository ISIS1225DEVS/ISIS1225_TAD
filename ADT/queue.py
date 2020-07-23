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
<<<<<<< HEAD
import config
from Utils import error as err
=======

import config
from Utils import error as error
>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70
from DataStructures import liststructure as lt

"""
  Este módulo implementa el tipo abstracto de datos cola (Queue) sobre una lista.
"""

def newQueue(datastructure='SINGLE_LINKED'):
    """ Crea una cola vacia
    Args:
        datastructure:  Indica el tipo de estructura de datos a utilizar 
                        para implementar la cola
    Returns:
        Una cola vacia
    Raises:
        Exception
    """
<<<<<<< HEAD
    Crea una cola vacia
    Args:
        datastructure 
            Indica el tipo de estructura de datos a utilizar la cola
    Return: Cola vacia
    Raises:
        Exception
    """
    try:
        return lt.newList(datastructure)
    except Exception as ex:
        err.reraise(ex, 'newQueue ')
=======
    try:
        return lt.newList(datastructure)
    except Exception as exp:
        error.reraise (exp, 'TADQueue->newQueue: ')


>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70

def enqueue (queue, element):
    """Agrega el elemento element en el tope de la pila
    Args:
        queue: La cola donde se insertará el elemento
        element:  El elemento a insertar

    Returns:
        La cola modificada
    Raises:
        Exception
    """
<<<<<<< HEAD
    Agrega el elemento element en el tope de la pila
    Args:
        queue :: list
            Indica la cola a la cual se le agregara el elemento
        element
            Elemento que será agregado en la tope de la cola
    Return: La cola modificada
    Raises: Exception
    """
    try:
        lt.addLast (queue, element)
        return queue
    except Exception as ex:
        err.reraise(ex, 'enqueue ')
=======
    try: 
        lt.addLast (queue, element)
        return queue
    except Exception as exp:
        error.reraise (exp, 'TADQueue->enqueue: ')


>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70

def dequeue (queue):
    """ Retorna el elemento en la primer posición de la cola, y lo elimina.
     Args:
        queue: La cola donde se eliminará el elemento

    Returns:
        El primer elemento de la cola
    Raises:
        Exception   
    """
<<<<<<< HEAD
    Retorna el elemento en la primer posición de la cola, y lo elimina
    Args:
        queue :: list
            Indica la cola a la cual se le eliminará el elemento
    Return: Elemento en la primera posicion de la cola, eliminandolo
    Raises: Exception
    """
    try:
        return lt.removeFirst(queue)
    except Exception as ex:
        err.reraise (ex, 'dequeue ')
=======
    try:
        return lt.removeFirst(queue)
    except Exception as exp:
        error.reraise (exp, 'TADQueue->dequeue: ')


>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70

def peek (queue):
    """ Retorna el elemento en la primer posición de la cola sin eliminarlo
    Args:
        queue: La cola  a examinar

    Returns:
        True el primer elemento de cola sin eliminarlo
    Raises:
        Exception   
    """
<<<<<<< HEAD
    Retorna el elemento en la primer posición de la cola, y lo elimina
    Args:
        queue :: list
            Indica la cola a la cual se le mostrará el primer elemento
    Return: Elemento en la primera posicion de la cola, sin eliminarlo
    
    """
    try:
        return lt.firstElement (queue)
    except Exception as ex:
        err.reraise (ex, 'peek ')  
=======
    try:
        return lt.firstElement (queue)
    except Exception as exp:
        error.reraise (exp, 'TADQueue->isEmpty: ')   


>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70

def isEmpty (queue):
    """Informa si la cola es vacía o no 
    Args:
        queue: La cola  a examinar

    Returns:
        True si la cola es vacia, False de lo contrario
    Raises:
        Exception   
    """
<<<<<<< HEAD
    Informa si la cola es vacía o no
    Retorna el elemento en la primer posición de la cola, y lo elimina
    Args:
        queue :: list
            Indica la cola que se tomará como vacia o no 
    Return:: Boolean
        True en caso de que este vacia, false en caso contrario
    """
    try:
        return lt.isEmpty(queue)
    except Exception as ex:
        err.reraise(ex,'isEmpty ')
=======
    try:
        return lt.isEmpty(queue)
    except Exception as exp:
        error.reraise (exp, 'TADQueue->isEmpty: ')



>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70

def size (queue):
    """Informa el número de elementos en la cola
    Args:
        queue: La cola  a examinar

    Returns:
        Retorna el tamaño de la cola

    Raises:
        Exception       
    """
<<<<<<< HEAD
    Informa el número de elementos en la cola
    Args:
        queue :: list
            Indica la lista cola a contar
    Return:: int
        Numero de elementos presentes en la cola
    """
    try:
        return lt.size(queue)
    except Exception as ex:
        err.reraise(exp, 'size ')
=======
    try:
        return lt.size(queue)
    except Exception as exp:
        error.reraise (exp, 'TADQueue->size: ')
>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70
