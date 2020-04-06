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
import math
from ADT import map as map 
from DataStructures import liststructure as lt
from DataStructures import listiterator as it
from DataStructures import edge as e


def newGraph( size, cmpfunction ):
    """
    Crea un grafo vacio. Los vertices son guardados en un map de tipo linear probing
    """
    prime = nextPrime (size * 2)
    graph = {'vertices':None, 
             'edges':0, 
             'type':'ADJ_LIST',
             'comparefunction':cmpfunction}

    graph ['vertices'] = map.newMap(capacity=prime, maptype='PROBING',comparefunction=cmpfunction)

    return graph



def insertVertex ( graph, vertex ):
    """
    Inserta el vertice vertex en el grafo graph
    """ 
    edges = lt.newList()
    map.put (graph['vertices'], vertex, edges)
    return graph



def removeVertex ( graph, vertex):
    """
    Remueve el vertice vertex del grafo graph
    """ 
    # TODO
    pass


def numVertex (graph):
    """
    Retorna el numero de vertices en el  grafo graph
    """ 
    return map.size(graph['vertices'])


def numEdges (graph):
    """
    Retorna el numero de arcos en el  grafo graph
    """ 
    return (graph['edges'])


def vertices (graph):
    """
    Retorna una lista con todos los vertices del grafo graph
    """ 
    lstmap = map.keySet(graph['vertices'])
    return lstmap



def edges (graph):
    """
    Retorna una lista con todos los arcos del grafo graph
    """ 
    lstmap = map.valueSet(graph['vertices'])
    lstresp = lt.newList ()
    itervertex = it.newIterator (lstmap)
    while it.hasNext (itervertex):
        lstedge = it.next (itervertex)
        iteredge = it.newIterator (lstedge)
        while (it.hasNext (iteredge)):
            edge = it.next (iteredge)
            if not (lt.isPresent (lstresp,edge, e.compareedges)):
                lt.addLast (lstresp,edge)
    return lstresp

    


def degree (graph, vertex):
    """
    Retorna el numero de arcos asociados al vertice vertex
    """ 
    element = map.get (graph['vertices'], vertex)
    lst = element['value']
    return (lt.size(lst))



def getEdge (graph, vertexa, vertexb):
    """
    Retorna el arco asociado a los vertices vertexa ---- vertexb
    """ 
    element = map.get (graph['vertices'], vertexa)
    lst = element['value']
    itvertex = it.newIterator (lst)
    while (it.hasNext(itvertex)):
        edge = it.next (itvertex)
        if ( e.either(edge) == vertexa or (e.other(edge,e.either(edge) )== vertexa ) ):
            if ( e.either(edge) == vertexb or (e.other(edge,e.either(edge) )== vertexb ) ):
                return edge
    return None



def addEdge (graph, vertexa, vertexb, weight):
    """
    Agrega un arco entre los vertices vertexa ---- vertexb, con peso weight
    """ 
    # Se crea el arco
    edge =  e.newEdge (vertexa,vertexb, weight)

    #Se obtienen las listas de adyacencias de cada vertice
    entrya = map.get (graph['vertices'], vertexa)
    entryb = map.get (graph['vertices'], vertexb)
    
    #Se anexa a cada lista el arco correspondiente
    lt.addLast (entrya['value'], edge)
    lt.addLast (entryb['value'], edge)

    graph['edges'] += 1



def adjacents (graph, vertex ):
    """
    Retorna una lista con todos los vertices adyacentes al vertice vertex
    """ 
    element = map.get (graph['vertices'], vertex)
    lst = element['value']
    lstresp = lt.newList()
    iter=it.newIterator (lst)
    while (it.hasNext(iter)):
        edge = it.next (iter)
        v = e.either(edge)
        if (v == vertex):
            lt.addLast (lstresp, e.other(edge, v))
        else:
            lt.addLast (lstresp, v)
    return lstresp




# ====================
#  Funciones Helper
# ====================


# Function that returns True if n  
# is prime else returns False 
# This code is contributed by Sanjit_Prasad  
def isPrime(n): 
      
    # Corner cases  
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
      
    # This is checked so that we can skip  
    # middle five numbers in below loop  
    if(n % 2 == 0 or n % 3 == 0): 
        return False
      
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
      
    return True
  
# Function to return the smallest  
# prime number greater than N 
# # This code is contributed by Sanjit_Prasad  
def nextPrime(N): 
  
    # Base case  
    if (N <= 1): 
        return 2
  
    prime = N 
    found = False
  
    # Loop continuously until isPrime returns  
    # True for a number greater than n  
    while(not found): 
        prime = prime + 1
  
        if(isPrime(prime) == True): 
            found = True
  
    return prime 

    