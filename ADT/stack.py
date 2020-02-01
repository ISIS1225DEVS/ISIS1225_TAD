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

from DataStructures import liststructure as lt

"""
  Este módulo implementa el tipo abstracto de datos pial (Stack) sobre una lista.
"""

def newStack(datastructure = 'SINGLE_LINKED'):
    """
    Crea una pila vacia
    """
    return lt.newList(datastructure)


def push (stack, element):
    """
    Agrega el elemento element en el tope de la pila
    """
    lt.addFirst (stack, element)


def pop (stack):
    """
    Retorna el elemento  presente en el tope de la pila
    """
    return lt.removeFirst (stack)


def isEmpty (stack):
    """
    Informa si la pila es vacía o no 
    """
    return lt.isEmpty(stack)


def top (stack):
    """
    Retorna el elemento en tope de la pila, sin eliminarlo de la pila 
    """
    return lt.firstElement(stack)


def size (stack):
    """
    Informa el número de elementos en la pila
    """
    return lt.size(stack)
