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
from DataStructures import heap as h
from ADT import map as m



def newIndexMinPQ ( size, cmpfunction):
    iminpq = {'pq':None}
    iminpq['pq'] = h.newHeap (size, cmpfunction)
    return iminpq



def isEmpty (iminpq):
    return (h.isEmpty(iminpq['pq']))



def size (iminpq):
    return (h.size(iminpq['pq']))


def insert (iminpq, key, index):
    h.insert (iminpq ['pq'], key, index) 


def delMin (iminpq):
    return (h.delMin(iminpq['pq']))


def changeKeyIndex (iminpq, key, index):
    return h.changeIndex (iminpq['pq'], key, index)


def min (iminpq):
    return h.min (iminpq['pq'])


def contains (iminpq, element):
    return h.contains (iminpq['pq'], element)


def keyOf (iminpq, index):
    pass



def increaseKey (iminpq, index, key):
    pass


"""
Funciones Helper
"""

def exchange ():
    pass

def greater ():
    pass


"""
Funciones MinPQ  
"""

def swim ():
    pass


def sink ():
    pass

