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



import config as cf
from ADT import list as lt
from DataStructures import listnode as node

"""

"""


def partition (lst, lo, hi, lessequalfunction):
    follower = leader = lo
    while leader < hi:
        if (lessequalfunction (lt.getElement(lst, leader), lt.getElement(lst, hi))):
            lt.exchange (lst, follower, leader)
            follower += 1
        leader +=1
    lt.exchange(lst, follower, hi)
    return follower



def sort (lst, lo, hi, lessequalfunction):
    if (lo >= hi ):
        return
    pivot = partition (lst, lo, hi, lessequalfunction)
    sort (lst, lo, pivot-1, lessequalfunction)
    sort (lst, pivot+1, hi, lessequalfunction)



def quickSort(lst, lessequalfunction):
    sort (lst, 1, lt.size(lst), lessequalfunction)

