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

from ADT import map as map 


"""
Estructura que contiene la información de una cola de prioridad indexada, orientada a menor
"""

def newMinHeap (capacity, cmpFunction):
  
  #priorities = [0]*(capacity+1)
  pq = [None]*(capacity+1)
  qpMap = map.newMap(capacity,comparefunction=cmpFunction)
  minPQ = {'pq':pq, 'qpMap':qpMap, 'maxCapacity':capacity,'size':0, 'cmpFunction':cmpFunction}

  return minPQ


def isEmpty(minPQ):
    return minPQ['size'] == 0

def contains(minPQ, index):
    return map.contains(minPQ['qpMap'],index)

def size(minPQ):
    return minPQ['size']

def min(minPQ):
    minIdx = minPQ['pq'][1]
    return minIdx['index']

def minPriority(minPQ):
    minIdx=minPQ['pq'][1]
    return minIdx['priority']

def delMin(minPQ):
    minIdx = minPQ['pq'][1]
    n = minPQ['size']
    exch(minPQ, 1, n)
    minPQ['size'] = n-1
    sink(minPQ, 1)
    map.remove(minPQ['qpMap'],minIdx['index']) # delete
    minPQ['pq'][n] = 0                         # not needed #Sedgewick uses index n+1, is it wrong?
    return minIdx['index']
    

def decreasePriority(minPQ, index, priority):
    val = map.get(minPQ['qpMap'],index)
    if val==None:
        raise Exception("Index ["+index+"] doesn't exist")
    elem = minPQ['pq'][val['value']]
    elem['priority'] = priority
    minPQ['pq'][val['value']] = elem
    swim(minPQ, val['value']) 
    # this operation can be generalized by ask new_prior > old_prior
    # to do swim, sink or neither

def increasePriority(minPQ, index, priority):
    val = map.get(minPQ['qpMap'],index)
    if val==None:
        raise Exception("Index ["+index+"] doesn't exist")
    elem = minPQ['pq'][val['value']]
    elem['priority'] = priority
    minPQ['pq'][val['value']] = elem
    sink(minPQ, val['value'])


def exch(minPQ, i, j):
    element_i = minPQ['pq'][i]
    element_j = minPQ['pq'][j]
    minPQ['pq'][i] = element_j
    map.put(minPQ['qpMap'], element_i['index'], j)
    minPQ['pq'][j] = element_i
    map.put(minPQ['qpMap'], element_j['index'], i)
    #minPQ['qp'][minPQ['pq'][i]] = i
    #minPQ['qp'][minPQ['pq'][j]] = j


def insert(minPQ, index, priority):
    if contains(minPQ, index):
        raise Exception('index is already in the priority queue')
    n = minPQ['size']+1
    minPQ['size']=n
    map.put(minPQ['qpMap'],index,n)
    minPQ['pq'][n] = {'index':index, 'priority':priority}
    #minPQ['priorities'][i] = priority
    swim(minPQ, n)


def greater(minPQ, i, j):
    i_element = minPQ['pq'][i]
    j_element = minPQ['pq'][j]
    return i_element['priority'] > j_element['priority']


def swim(minPQ, k):
    while k > 1 and greater(minPQ, int(k/2), k):
        exch(minPQ, k, int(k/2))
        k = int(k/2)

def sink(minPQ, k):
    n = minPQ['size']
    while 2*k <= n:
        j = 2*k
        if j < n and greater(minPQ, j, j+1):
            j+=1
        if not greater(minPQ, k, j):
            break
        exch(minPQ, k, j)
        k = j