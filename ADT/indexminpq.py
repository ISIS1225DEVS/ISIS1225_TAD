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
from DataStructures import minheap as h
from ADT import map as m

def newIndexMinPQ ( capacity, cmpfunction):
    iminpq= h.newMinHeap (capacity, cmpfunction)
    return iminpq

def isEmpty (iminpq):
    return (h.isEmpty(iminpq))


def size (iminpq):
    return (h.size(iminpq))


def insert (iminpq, key, index):
    h.insert (iminpq, key, index) 


def delMin (iminpq):
    return (h.delMin(iminpq))


def decreasePriority (iminpq, key, index):
    return h.decreasePriority (iminpq, key, index)

def increasePriority (iminpq, key, index):
    return h.increasePriority (iminpq, key, index)


def min (iminpq):
    return h.min (iminpq) 


def contains (iminpq, element):
    return h.contains (iminpq, element)


def keyOf (iminpq, index):
    pass
