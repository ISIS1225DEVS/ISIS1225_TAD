"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
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
<<<<<<< HEAD
from Utils import error as err
=======
from Utils import error as error
>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70
from DataStructures import liststructure as lt

"""
  Este módulo implementa el tipo abstracto de datos pila (Stack) sobre una lista.
"""

def newStack(datastructure = 'SINGLE_LINKED'):
    """ Crea una pila vacia.
     
    Args:
        datastructure:  Indica el tipo de estructura de datos a utilizar 
                        para implementar la pila
    Returns:
        Una pila vacia
    Raises:
        Exception
    """
<<<<<<< HEAD
    Crea una pila vacia
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
        err.reraise(ex, 'newStack ')
=======
    try:
        return lt.newList(datastructure, None)
    except Exception as exp:
        error.reraise (exp, 'TADStack->newStack: ')
>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70
    


def push (stack, element):
    """ Agrega el elemento element en el tope de la pila.

    Args:
        stack:  La pila donde se insetará el elemento
        element:  El elemento a insertar

    Returns:
        La pila modificada

    Raises: 
        Exception
    """
<<<<<<< HEAD
    Agrega el elemento element en el tope de la pila
    Args:
        stack :: list
            Indica la pila a la cual se le agregara el elemento
        element
            Elemento que será agregado en la tope de la cola
    Return: La pila modificada
    Raises: Exception
    """
    try:
        lt.addFirst (stack, element)
        return stack
    except Exception as ex:
        err.reraise(ex,'push ')
=======
    try: 
        lt.addFirst (stack, element)
        return stack
    except Exception as exp:
        error.reraise (exp, 'TADStack->Push: ')
    

>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70


def pop (stack):
    """ Retorna el elemento  presente en el tope de la pila.

     Args:
        stack:  La pila de donde se retirara el elemento

    Returns:
        El elemento del tope de la pila 

    Raises: 
        Exception   
    """
<<<<<<< HEAD
    Retorna el elemento  presente en el tope de la pila
    Args:
        stack :: list
            Indica la pila a la cual se le eliminará el elemento
    Return: Elemento en la primera posicion de la pila, eliminandolo
    Raises: Exception
    """
    try:
        return lt.removeFirst(stack)
    except Exception as ex:
        err.reraise (ex, 'pop ')
=======
    try:
        return lt.removeFirst (stack)
    except Exception as exp:
        error.reraise (exp, 'TADStack->pop: ')


>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70


def isEmpty (stack):
    """Informa si la pila es vacía o no 
     Args:
        stack:  La pila a examinar

    Returns:
        True si la pila es vacia
        False de lo contrario

    Raises: 
        Exception  
    """
<<<<<<< HEAD
    Informa si la pila es vacía o no 
    Retorna el elemento en la primer posición de la cola, y lo elimina
    Args:
        stack :: list
            Indica la pila que se tomará como vacia o no 
    Return:: Boolean
        True en caso de que este vacia, false en caso contrario
    """
    try:
        return lt.isEmpty(stack)
    except Exception as ex:
        err.reraise(ex,'isEmpty ')
=======
    try:
        return lt.isEmpty(stack)
    except Exception as exp:
        error.reraise (exp, 'TADStack->isEmpty: ')


>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70


def top (stack):
    """ Retorna el elemento en tope de la pila, sin eliminarlo de la pila 
         
    Args:
        stack:  La pila a examinar

    Returns:
        El primer elemento de la pila, sin eliminarlo

    Raises: 
        Exception  
    """
<<<<<<< HEAD
    Retorna el elemento en tope de la pila, sin eliminarlo de la pila 
    Args:
        stack :: list
            Indica la pila a la cual se le mostrará el primer elemento
    Return: Elemento en la primera posicion de la pila, sin eliminarlo
    
    """
    try:
        return lt.firstElement (stack)
    except Exception as ex:
        err.reraise (ex, 'peek ')  
=======
    try: 
        return lt.firstElement(stack)
    except Exception as exp:
        error.reraise (exp, 'TADStack->top: ')



>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70


def size (stack):
    """ Informa el número de elementos en la pila
    Args:
        stack: La pila a examinar

    Returns:
        Retorna el tamaño de la pila

    Raises:
        Exception  
    """
<<<<<<< HEAD
    Informa el número de elementos en la pila
    Args:
        stack :: list
            Indica la lista cola a contar
    Return:: int
        Numero de elementos presentes en la cola
    """
    try:
        return lt.size(stack)
    except Exception as ex:
        err.reraise(exp, 'size ')
    
=======
    try:
        return lt.size(stack)
    except Exception as exp:
        error.reraise (exp, 'TADStack->size: ')
>>>>>>> 3803d596a4d1cbce791a4e776e3584ccefd1df70
